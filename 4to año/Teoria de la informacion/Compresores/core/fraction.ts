import assert from "assert";

const gdc = (a: bigint, b: bigint): bigint => b ? gdc(b, a % b) : a;

/*
function gdc( a: bigint, b:bigint ): bigint {
	if(a < 0n && b < 0n) return gdc(-a, -b);
	if(a < 0n || b < 0n) return gdc(-a, b);
	if (a === 0n) return b;
	if (b === 0n) return a;

	let k = 1n, t: bigint;
	while (a % 2n === 0n && b % 2n === 0n ) {
		a /= 2n;
		b /= 2n;
		k *= 2n;
	}

	while (a % 2n === 0n) {
		a /= 2n;
	}

	while (b) {
		while (b % 2n === 0n) {
			b /= 2n; // right shift
		}

		if (a > b) {
			t = b;
			b = a;
			a = t;
		}

		b -= a; // b=0 iff b=a
	}
	
	return k * a;
}
*/

function log10(bigint: bigint): number {
	if (bigint < 0) throw new Error("Negative numbers don't have logarithms");
	const s = bigint.toString(10);
  
	return s.length + Math.log10(Number("0." + s))
}

const log10of2 = log10(2n);

type FractionLike = Fraction | bigint | number;
export default class Fraction {
	constructor(numerator: bigint | number, denominator: bigint | number = 1) {
		this.numerator = BigInt(numerator);
		this.denominator = BigInt(denominator);

		// simplify
		const gcd = gdc(this.numerator, this.denominator);
		this.numerator /= gcd;
		this.denominator /= gcd;
	}
	public readonly numerator: bigint;
	public readonly denominator: bigint;

	public add(fraction: FractionLike): Fraction {
		fraction = Fraction.from(fraction);

		return new Fraction(
			this.numerator * fraction.denominator + fraction.numerator * this.denominator,
			this.denominator * fraction.denominator
		);
	}

	get isZero(): boolean {
		return this.numerator === 0n || this.numerator === -0n;
	}

	get isNegative(): boolean {
		return (
			(this.numerator < 0 && this.denominator > 0) ||
			(this.numerator > 0 && this.denominator < 0)
		);
	}

	public subtract(fraction: FractionLike): Fraction {
		fraction = Fraction.from(fraction);

		return new Fraction(
			this.numerator * fraction.denominator - fraction.numerator * this.denominator,
			this.denominator * fraction.denominator
		);
	}

	public multiply(fraction: FractionLike): Fraction {
		fraction = Fraction.from(fraction);

		return new Fraction(
			this.numerator * fraction.numerator,
			this.denominator * fraction.denominator
		);
	}

	public divide(fraction: FractionLike): Fraction {
		fraction = Fraction.from(fraction);

		return new Fraction(
			this.numerator * fraction.denominator,
			this.denominator * fraction.numerator
		);
	}

	public inverse(): Fraction {
		return new Fraction(this.denominator, this.numerator);
	}

	public log2(): Fraction {
		return Fraction.from(
			log10(this.numerator) - log10(this.denominator)
		).divide(log10of2);
	}

	public pow(exp: FractionLike): Fraction {
		exp = Fraction.from(exp);

		if(exp.denominator !== 1n) throw new Error('Exponent must be an integer');

		return new Fraction(
			this.numerator ** exp.numerator,
			this.denominator ** exp.numerator
		);
	}

	public neg(): Fraction {
		return new Fraction(-this.numerator, this.denominator);
	}

	public abs(): Fraction {
		if(this.numerator < 0) return this.neg();
		return this;
	}

	public compare(fraction: FractionLike): number {
		fraction = Fraction.from(fraction);

		const diff = this.subtract(fraction);

		if(diff.isZero) return 0;
		return diff.isNegative ? -1 : 1;
	}

	public bigger(fraction: FractionLike): boolean {
		return this.compare(fraction) > 0;
	}

	public smaller(fraction: FractionLike): boolean {
		return this.compare(fraction) < 0;
	}

	public smallerOrEqual(fraction: FractionLike): boolean {
		return this.compare(fraction) <= 0;
	}

	public biggerOrEqual(fraction: FractionLike): boolean {
		return this.compare(fraction) >= 0;
	}

	public ceil(): Fraction {
		if(this.numerator % this.denominator === 0n) return this;
			
		return new Fraction(this.numerator / this.denominator + 1n);
	}

	valueOf(): number {
		return Number(this.numerator) / Number(this.denominator);
	}

	toFraction(): string {
		return `${this.numerator}/${this.denominator}`;
	}

	toString(base = 10): string {
		// do manual calculations
		let num = this.numerator;
		let den = this.denominator;
		let str = this.isNegative ? '-' : '';

		const whole = num / den;
		num = num % den;

		str += whole.toString(base);

		if(num === 0n) return str;

		const digits: string[] = [];
		const seen = new Map<bigint, number>();

		let i = 0;
		while(num !== 0n) {
			if(seen.has(num)) {
				const index = seen.get(num)!;
				digits.splice(index, 0, '(');
				digits.push(')');
				break;
			}

			seen.set(num, i);
			num *= BigInt(base);
			const digit = num / den;
			num = num % den;

			digits.push(digit.toString(base));
			i++;
		}

		return str + '.' + digits.join('');
	}

	[Symbol.for('nodejs.util.inspect.custom')](): unknown {
		return this.valueOf();
	}

	static from(num: number | bigint | string | Fraction): Fraction {
		if(num instanceof Fraction) return num;
		if(typeof num === 'bigint') return new Fraction(num);

		const str = num.toString();

		const [whole, decimal] = str.split('.') as [string, string?];
		if(!decimal) return new Fraction(BigInt(whole));
		
		const denominator = 10n ** BigInt(decimal.length);
		const numerator = BigInt(whole + decimal);

		return new Fraction(numerator, denominator);
	}

	static fromBase2(str: string): Fraction {
		const [intStr, decStr] = str.split('.') as [string, string?];
	
		const int = BigInt('0b' + intStr);

		if(!decStr) return new Fraction(int);

		const dec = BigInt('0b' + decStr);
		const decLen = BigInt(decStr.length);

		return new Fraction(
			int * 2n ** decLen + dec,
			2n ** decLen
		);
	}

	static sum(arr: Fraction[]): Fraction {
		return arr.reduce((acc, curr) => acc.add(curr), new Fraction(0));
	}

	static zero = new Fraction(0);
	static one = new Fraction(1);
	static infinity = new Fraction(1, 0);
}

if (require.main === module) {
	// make tests
	const f1 = new Fraction(1, 2);
	const f2 = new Fraction(7, 3);

	assert.strictEqual(f1.add(f2).toFraction(), '17/6');
	assert.strictEqual(f1.subtract(f2).toFraction(), '-11/6');
	assert.strictEqual(f1.multiply(f2).toFraction(), '7/6');
	assert.strictEqual(f1.divide(f2).toFraction(), '3/14');
	assert.strictEqual(f1.inverse().toFraction(), '2/1');
	
	// assert.strictEqual(Fraction.from(2).log2().toString(), '1/1');
	// assert.strictEqual(Fraction.from(3).log2().toString(), '9542425094393248/6020599913279625');
	// assert.strictEqual(f1.log2().toString(), '-1/1');
	assert.strictEqual(f2.log2().toFraction(), '36797678529459443/30102999566398125');

}

// testNum(0.70252); // 17563/25000
// // testNum(0.7026921187594828); // 8577784652825717/12207031250000000
// 
// function binaryToFraction(str: string): Fraction {
// 	const [intStr, decStr] = str.split('.') as [string, string?];
// 	const int = BigInt('0b' + intStr);
// 
// 	if(!decStr) return new Fraction(int);
// 
// 	let decimalPart = Fraction.zero;
// 
// 	let n = 1n; // ????
// 	for(const bit of decStr){
// 		if(bit === '1'){
// 			decimalPart = decimalPart.add(Fraction.from(2).pow(n).inverse());
// 		}
// 		n++;
// 	}
// 
// 	return new Fraction(int).add(decimalPart);
// }
// 
// function testNum(num: number){
// 	const binary = num.toString(2);
// 
// 	// const fraction = Fraction.fromBase2(binary);
// 	const fraction = new Fraction(17563, 25000);
// 	console.log(fraction.toFraction());
// 	console.log(fraction.toString());
// 	console.log(fraction.toString(2));
// 	console.log(binaryToFraction(binary).toFraction());
// }
