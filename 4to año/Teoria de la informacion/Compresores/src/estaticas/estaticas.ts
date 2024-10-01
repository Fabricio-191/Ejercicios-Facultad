import assert from "assert";
import { SubstitutionCodification, Codification, Source } from "../../core/base";
import { mapObject } from "../../core/utils";
import Fraction from "../../core/fraction";

class MySymbol {
	constructor(symbol: string, probability: Fraction) {
		this.symbol = symbol;
		this.probability = probability;
		this.code = '';
	}
	public symbol: string;
	public probability: Fraction;
	public code: string;

	addCode(code: string, reverse = false): void {
		if(reverse) this.code = this.code + code;
		else this.code = code + this.code;
	}
}

class MyGroup {
	constructor(childs: Array<MySymbol | MyGroup>) {
		this.childs = childs;
		this.probability = Fraction.sum(childs.map(child => child.probability));
	}
	public childs: Array<MySymbol | MyGroup>;
	public probability: Fraction;

	addCode(code: string): void {
		this.childs.forEach(child => child.addCode(code));
	}
}

export class Huffman extends SubstitutionCodification {
	_makeCodes(): void {
		const huffmanSymbols = this.source.symbols
			.map((symbol) => new MySymbol(symbol, this.source.probabilities[symbol]!));

		const huffmanGroups: Array<MyGroup | MySymbol> = [...huffmanSymbols];
		if(huffmanGroups.length === 1) {
			huffmanSymbols[0]!.addCode('0');
		}

		while(huffmanGroups.length > 1) {
			huffmanGroups.sort((a, b) => a.probability.compare(b.probability));

			const childs = huffmanGroups.splice(0, this.base);
			childs.forEach((child, index) => child.addCode(index.toString()));

			const newGroup = new MyGroup(childs);
			huffmanGroups.push(newGroup);
		}

		for(const symbol of huffmanSymbols) {
			this.codes[symbol.symbol] = symbol.code;
		}
	}
}

export class Fano extends SubstitutionCodification {
	_divisionInGroups(fanoSymbols: MySymbol[], prob: Fraction): void {
		if(fanoSymbols.length === 1) return;
		if(fanoSymbols.length > 20) {
			let minDifference: Fraction = new Fraction(Infinity);
			let minIndex = 0;
			for(let i = 0; i < fanoSymbols.length; i++) {
				const left = fanoSymbols.slice(0, i);
				const right = fanoSymbols.slice(i);
				const difference = left.reduce((acc, curr) => acc.add(curr.probability), Fraction.from(0))
					.subtract(right.reduce((acc, curr) => acc.add(curr.probability), Fraction.from(0))).abs();

				if(difference.compare(minDifference) < 0) {
					minDifference = difference;
					minIndex = i;
				}
			}

			const left = fanoSymbols.slice(0, minIndex);
			const right = fanoSymbols.slice(minIndex);

			left.forEach(symbol => symbol.addCode('0', true));
			right.forEach(symbol => symbol.addCode('1', true));

			this._divisionInGroups(left, prob.divide(this.base));
			this._divisionInGroups(right, prob.divide(this.base));
			return;
		}

		let minDifference = Infinity;
		let minCombination = '';
		for(let combination = 0n; combination < this.base ** fanoSymbols.length; combination++) {
			const probabilities = Array(this.base).fill(prob);
			const comb = combination.toString(this.base).padStart(fanoSymbols.length, '0');

			for(let i = 0; i < fanoSymbols.length; i++) {
				probabilities[Number(comb[i])] = probabilities[Number(comb[i])].subtract(fanoSymbols[i]!.probability);
			}

			const difference = probabilities.reduce((acc, curr) => acc + Math.abs(curr), 0);
			if(difference < minDifference) {
				minDifference = difference;
				minCombination = comb;
			}
		}

		for(let i = 0; i < this.base; i++) {
			const group = fanoSymbols.filter((_, j) => minCombination[j] === i.toString());
			group.forEach(symbol => symbol.addCode(i.toString(), true));

			if(group.length > 1) this._divisionInGroups(group, prob.divide(this.base));
		}
	}

	_makeCodes(): void {
		if(this.base !== 2) throw new Error('Fano only works with base 2 (yet)');

		const fanoSymbols = this.source.symbols
			.map((symbol) => new MySymbol(symbol, this.source.probabilities[symbol]!));

			if(fanoSymbols.length === 1) {
				fanoSymbols[0]!.addCode('0');
			}

		this._divisionInGroups(fanoSymbols, new Fraction(1, this.base));
		
		for(const symbol of fanoSymbols) {
			this.codes[symbol.symbol] = symbol.code;
		}
	}
}

export class Shannon extends SubstitutionCodification {
	private _makeCode(length: number): string {
		let num = 0;
		
		while(num < this.base ** length) {
			const code = num.toString(this.base).padStart(length, '0');
			if(!Object.values(this.codes).some(c => code.startsWith(c) || c.startsWith(code))) {
				return code;
			}
			num++;
		}

		throw new Error('No code found');
	}

	protected _makeCodes(): void {
		if(this.kraftInequality().valueOf() > 1) throw new Error('Kraft inequality not satisfied');

		for(const symbol of this.source.symbols) {
			const length = Math.ceil(-Math.log2(
				this.source.probabilities[symbol]!.valueOf()
			));
			// const length = this.probabilities[symbol]!.log2().neg().ceil().valueOf();;

			this.codes[symbol] = this._makeCode(length);
		};
	}
}

export class Arithmetic implements Codification<Fraction> {
	constructor(source: Source) {
		this.source = source;
		
		let prev = Fraction.zero;
		this.cumulProb = mapObject(
			this.source.probabilities,
			(prob) => {
				const cumul = { low: prev, high: prev.add(prob) };
				prev = cumul.high;
				return cumul;
			}
		);

		this.cumulProb = {
			'a': { low: Fraction.from(0.6), high: Fraction.from(1) },
			'o': { low: Fraction.from(0.4), high: Fraction.from(0.6) },
			'e': { low: Fraction.from(0.25), high: Fraction.from(0.4) },
			'u': { low: Fraction.from(0.1), high: Fraction.from(0.25) },
			'i': { low: Fraction.from(0), high: Fraction.from(0.1) },
		}
	}
	private source: Source;
	private cumulProb: Record<string, { low: Fraction, high: Fraction }>;

	public encode(str: string): Fraction {
		let low = Fraction.zero;
		let high = Fraction.one;

		for(const symbol of str) {
			const range = high.subtract(low);
			const prob = this.cumulProb[symbol]!;
			
			high = low.add(prob.high.multiply(range));
			low = low.add(prob.low.multiply(range));
		}

		return low;
	}

	public decode(encoded: Fraction): string {
		let num = encoded;
		let decoded = '';

		while(!num.isZero) {
			for(const [symbol, { low, high }] of Object.entries(this.cumulProb)) {
				if(low.smallerOrEqual(num) && num.smaller(high)) {
					decoded += symbol;
					num = num.subtract(low).divide(high.subtract(low));
					break;
				}
			}
		}

		return decoded;
	}
}

if (require.main === module) {
	// const testStr = 'PABLOPABLITOCLAVOUNCLAVITO';
	const testStr = 'aeiouaaaeouaiaaoeoua';
	const testSource = Source.fromString(testStr);

	const test = (codification: Codification<any>, testStr: string) => {
		const encoded = codification.encode(testStr);
		console.log(`${codification.constructor.name}: ${encoded.valueOf()} (${encoded.length})`);

		assert.strictEqual(codification.decode(encoded), testStr);
	}

	console.log(`Original size: ${testStr.length * 8} bits`);

	test(new Huffman(testSource), testStr);
	test(new Fano(testSource), testStr);
	test(new Shannon(testSource), testStr);
	test(new Arithmetic(testSource), testStr);
	

	// ejemplos del profesor
	assert.strictEqual(
		new Shannon(Source.fromString("aaaaaaaaabbbbbccccdd")).encode('abcd'),
		'00011001010'
	)

	assert.strictEqual(
		new Huffman(Source.fromString("aaaaaaaaabbbbbccccdd")).encode('abcd'),
		'010111110'
	)

	assert.strictEqual(
		new Fano(Source.fromString("aaaaaaaaabbbbbbbcccccddeefg")).encode('abcdefg'),
		'0010011100111011011111'
	)
}
