import { SubstitutionCodification, Codification, Source, CodificationWithOne } from "../core/base";
import { mapObject, substringCounts } from "../core/utils";
import Fraction from "../core/fraction";

export class ASCII implements CodificationWithOne<string> {
	constructor(codes: Record<string, string>) {
		this._codes = codes;
	}
	private _codes: Record<string, string>;

	encode(str: string): string {
		return str.split('').map(c => this._codes[c]).join('');
	}

	decodeOne(str: string): [string, string] {
		const result = Object.entries(this._codes).find(([_, code]) => str.startsWith(code));

		if(!result) throw new Error('Invalid code');

		return result;
	}

	decode(str: string): string {
		let decoded = '';
		let i = 0;
		while(i < str.length) {
			const [symbol, code] = this.decodeOne(str.slice(i));
			decoded += symbol;
			i += code.length;
		}

		return decoded;
	}

	static encode(str: string): string {
		return str.split('').map(c => c.charCodeAt(0).toString(2).padStart(8, '0')).join('');
	}

	static decodeOne(str: string): [string, string] {
		return [String.fromCharCode(parseInt(str.slice(0, 8), 2)), str.slice(0, 8)];
	}

	static decode(str: string): string {
		let decoded = '';
		for(let i = 0; i < str.length; i += 8) {
			decoded += String.fromCharCode(parseInt(str.slice(i, i + 8), 2));
		}

		return decoded;
	}
}

export class MinASCII extends SubstitutionCodification {
	_makeCodes(): void {
		const l = Math.ceil(Math.log2(this.source.symbols.length));

		let code = 0;
		for(const symbol of this.source.symbols) {
			this.codes[symbol] = code.toString(2).padStart(l, '0');
			code++;
		}
	}

	public static fromString(str: string): MinASCII {
		const prob = new Fraction(1, Array.from(new Set(str)).length);

		const probabilities = mapObject(
			substringCounts(str),
			() => prob,
		);

		return new MinASCII(new Source(probabilities));
	}
}