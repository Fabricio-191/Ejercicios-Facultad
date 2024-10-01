import { substringCounts } from '../../core/utils.ts';

export default abstract class SucesiveSymbolsEncoding {
	static encode(str: string, encoding: (s: string) => number): [string, number, number] {
		const pairs: [string, number][] = [];

		const charsVariety = new Set(str).size;
		const biggestCount = Math.max(...Object.values(substringCounts(str)));

		const charBits = Math.ceil(Math.log2(charsVariety));
		const countBits = Math.ceil(Math.log2(biggestCount));

		for(let i = 0; i < str.length; i++) {
			const char = str[i]!;
			let count = 1;
			while(str[i + count] === char) {
				count++;
			}
			i += count;

			pairs.push([char, count]);
		}

		const encoded = pairs.map(
			([char, count]) =>
				encoding(char).toString(2).padStart(charBits, '0') +
				count.toString(2).padStart(countBits, '0')
		).join('');

		return [
			encoded,
			charBits,
			countBits
		];
	}

	static decode(str: string, charBits: number, countBits: number): string {
		const pairs: [string, number][] = [];

		let i = 0;
		while(i < str.length) {
			const char = String.fromCharCode(parseInt(str.slice(i, i + charBits), 2));
			i += charBits;

			const count = parseInt(str.slice(i, i + countBits), 2);
			i += countBits;

			pairs.push([char, count]);
		}

		return pairs.map(([char, count]) => char.repeat(count)).join('');
	}
}

console.log(SucesiveSymbolsEncoding.encode('aab'));