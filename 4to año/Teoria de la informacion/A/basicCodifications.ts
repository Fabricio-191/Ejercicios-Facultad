const round2 = (num: number, decimals: number) => Math.round(num * 10 ** decimals) / 10 ** decimals;

export class Source {
	constructor(symbols: string[], probabilities: number[]) {
		if(symbols.length !== probabilities.length) {
			throw new Error('Symbols and probabilities must have the same length');
		}else if(Math.abs(probabilities.reduce((acc, curr) => acc + curr) - 1) > 0.0001) {
			throw new Error('Probabilities must sum 1');
		}

		this.symbols = symbols;
		this.probabilities = probabilities;
	}
	public symbols: string[];
	public probabilities: number[];

	entropy() {
		let entropy = 0;
		for(const prob of this.probabilities) {
			entropy += prob * Math.log2(1 / prob);
		}

		return entropy;
	}

	extend(){
		const newSymbols: string[] = [];
		const newProbabilities: number[] = [];
		for(const i in this.symbols) {
			for(const j in this.symbols) {
				newSymbols.push(this.symbols[i] + this.symbols[j]);
				newProbabilities.push(this.probabilities[i] * this.probabilities[j]);
			}
		}
		
		return new Source(newSymbols, newProbabilities);
	}

	static fromString(str: string) {
		const counts = {};
		
		for (let i = 0; i < str.length; i++) {
			// @ts-ignore
			counts[str[i]] = (counts[str[i]] || 0) + 1;
		}

		const symbols = Object.keys(counts).sort();
		// @ts-ignore
		const probabilities: number[] = symbols.map(symbol => counts[symbol] / str.length);

		return new Source(symbols, probabilities);
	}
}

export abstract class Codification {
	constructor(source: Source, base: number = 2) {
		this.source = source;
		this.base = base;

		this.codes = this._getCodes();

		if(source.symbols.length !== this.codes.length) {
			throw new Error('Symbols and codes must have the same length');
		}
		
		for(const code of this.codes) {
			if(this.codes.some(c => code.startsWith(c) && code !== c)) {
				throw new Error('Codes must be prefix-free');
			}
		}
	}
	source: Source;
	codes: string[];
	base: number;

	abstract _getCodes(): string[];

	encode(str: string): string {
		let encoded = '';
		let currentSymbol = '';
		for(const char of str) {
			currentSymbol += char;
			const symbolIndex = this.source.symbols.indexOf(currentSymbol);
			if(symbolIndex !== -1) {
				encoded += this.codes[symbolIndex];
				currentSymbol = '';
			}
		}

		return encoded
	};

	decode(str: string): string {
		let decoded = '';
		let currentCode = '';
		for(const char of str) {
			currentCode += char;
			const symbolIndex = this.codes.indexOf(currentCode);
			if(symbolIndex !== -1) {
				decoded += this.source.symbols[symbolIndex];
				currentCode = '';
			}
		}

		return decoded;
	};

	kraftInequality() {
		return this.codes.reduce((acc, curr) => acc + (1 / this.base) ** curr.length, 0);
	}

	averageLength() {
		return this.codes
			.map((code, i) => code.length * this.source.probabilities[i])
			.reduce((acc, curr) => acc + curr);
	}

	show(){
		console.log('Entropy:', round2(this.source.entropy(), 4));

		const table: unknown[] = [];
		for(let i = 0; i < this.source.symbols.length; i++){
			table.push({
				symbol: this.source.symbols[i],
				probability: round2(this.source.probabilities[i], 4),
				code: this.codes[i]
			});
		}

		console.table(table);
		console.log('Average length:', round2(this.averageLength(), 4));
		console.log()
		console.log()
	}
}

export class MySymbol {
	constructor(symbol: string, probability: number) {
		this.symbol = symbol;
		this.probability = probability;
		this.code = '';
	}
	symbol: string;
	probability: number;
	code: string;

	addCode(code: string, reverse = false) {
		if(reverse) this.code = this.code + code;
		else this.code = code + this.code;
		return this;
	}
}

export class MyGroup {
	constructor(childs: Array<MySymbol | MyGroup>) {
		this.childs = childs;
		this.probability = childs.reduce((acc, curr) => acc + curr.probability, 0);
	}
	childs: Array<MySymbol | MyGroup>;
	probability: number;

	addCode(code: string) {
		this.childs.forEach(child => child.addCode(code));
		return this;
	}
}

export class Huffman extends Codification {
	_getCodes(): string[] {
		const huffmanSymbols = this.source.symbols
			.map((symbol, i) => new MySymbol(symbol, this.source.probabilities[i]));
		const huffmanGroups: Array<MyGroup | MySymbol> = [...huffmanSymbols];

		while(huffmanGroups.length > 1) {
			huffmanGroups.sort((a, b) => a.probability - b.probability);

			const childs = huffmanGroups.splice(0, this.base);
			childs.forEach((child, index) => child.addCode(index.toString()));

			const newGroup = new MyGroup(childs);
			huffmanGroups.push(newGroup);
		}

		return huffmanSymbols.map(symbol => symbol.code);
	}
}

export class Shannon extends Codification {
	_getCodes(): string[] {
		const shannonLengths = this.source.probabilities.map(p => Math.ceil(-Math.log2(p)));
		const shannonCodes: string[] = [];

		for(let i = 0; i < this.source.symbols.length; i++) {
			let num = 0;
			while(num < this.base ** shannonLengths[i]) {
				const code = num.toString(this.base).padStart(shannonLengths[i], '0');
				if(!shannonCodes.some(c => code.startsWith(c)) && !shannonCodes.some(c => c.startsWith(code))) {
					shannonCodes.push(code);
					break;
				}
				num++;
			}
		}

		return shannonCodes;
	}
}

export class Fano extends Codification {
	_divisionInGroups(fanoSymbols: MySymbol[], prob: number): void {
		if(fanoSymbols.length === 1) return;
		if(fanoSymbols.length > 20) {
			let minDifference = Infinity;
			let minIndex = 0;
			for(let i = 0; i < fanoSymbols.length; i++) {
				const left = fanoSymbols.slice(0, i);
				const right = fanoSymbols.slice(i);
				const difference = Math.abs(
					left.reduce((acc, curr) => acc + curr.probability, 0) - right.reduce((acc, curr) => acc + curr.probability, 0)
				);

				if(difference < minDifference) {
					minDifference = difference;
					minIndex = i;
				}
			}

			const left = fanoSymbols.slice(0, minIndex);
			const right = fanoSymbols.slice(minIndex);

			left.forEach(symbol => symbol.addCode('0', true));
			right.forEach(symbol => symbol.addCode('1', true));

			this._divisionInGroups(left, prob / this.base);
			this._divisionInGroups(right, prob / this.base);
			return;
		}

		let minDifference = Infinity;
		let minCombination = '';
		for(let combination = 0n; combination < this.base ** fanoSymbols.length; combination++) {
			const probabilities = Array(this.base).fill(prob);
			const comb = combination.toString(this.base).padStart(fanoSymbols.length, '0');

			for(let i = 0; i < fanoSymbols.length; i++) {
				probabilities[Number(comb[i])] -= fanoSymbols[i].probability;
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

			if(group.length > 1) this._divisionInGroups(group, prob / this.base);
		}
	}

	_getCodes(): string[] {
		if(this.base !== 2) throw new Error('Fano only works with base 2 (yet)');

		const fanoSymbols = this.source.symbols
			.map((symbol, i) => new MySymbol(symbol, this.source.probabilities[i]));

		this._divisionInGroups(fanoSymbols, 1/this.base);
		
		return fanoSymbols.map(symbol => symbol.code);
	}
}

if (require.main === module) {
	const source = new Source(
		['s1', 's2', 's3', 's4', 's5', 's6'],
		[0.1, 0.1, 0.2, 0.4, 0.1, 0.1]
	);

	console.log('Huffman');
	new Huffman(source).show();

	console.log('Shannon');
	new Shannon(source).show();

	console.log('Fano');
	new Fano(source).show();


	/*
	const source2 = new Source(
		['s1', 's2', 's3', 's4'],
		[9/20, 5/20, 4/20, 2/20]
	);

	console.log('Huffman');
	new Huffman(source2).show();

	console.log('Shannon');
	new Shannon(source2).show();

	console.log('Shannon');
	new Shannon(new Source(
		['s1', 's2', 's3'],
		[0.5, 0.25, 0.25],
	)).show();

	console.log('Fano');
	new Fano(new Source(
		['s1', 's2', 's3', 's4', 's5', 's6', 's7'],
		[9/27, 7/27, 5/27, 2/27, 2/27, 1/27, 1/27],
	)).show();

	console.log('Huffman (base 3)');
	new Huffman(
		new Source(
			['s1', 's2', 's3', 's4', 's5', 's6', 's7'],
			[1/3, 1/3, 1/9, 1/9, 1/27, 1/27, 1/27],
		),
		3
	)
	.show();
	*/

	/*
		const source1 = Source.fromString('PABLOPABLITOCLAVOUNCLAVITO');
	const source2 = source1.extend();

	new Fano(source1).show();
	const fano = new Fano(source2);
	console.log(fano.averageLength());
	let str = '';
	const columnsQty = 4;

	for(let i = 0; i < fano.codes.length; i += columnsQty) {
		const chunk = fano.codes.slice(i, i + columnsQty);

		for(let j = 0; j < chunk.length; j++) {
			str += source2.symbols[i + j] + ` (${source2.probabilities[i + j].toFixed(4)}): ` + chunk[j] + '\t';
		}

		str += '\n';
	}

	console.log(str);

	console.log(fano.encode('PABLOPABLITOCLAVOUNCLAVITO'));
	*/
}
