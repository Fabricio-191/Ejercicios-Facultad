import { Codification, Source } from './basicCodifications.ts';

const subdivideString = (str: string, order: number): string[] => {
	const substrings: string[] = [];
	for (let i = 0; i < str.length - order + 1; i++) {
		substrings.push(str.slice(i, i + order));
	}

	return substrings;
}

const count = (arr: string[]): { [key: string]: number } => arr.reduce((acc, curr) => {
	acc[curr] = (acc[curr] || 0) + 1;
	return acc;
}, {});

class Markov {
	constructor(str: string) {
		this.str = str;
		this.symbols = Array.from(new Set(str.split(''))).sort();
	}
	public readonly str: string;
	public readonly symbols: string[];
	public readonly order: number;

	public getMarkovSource(order: number = 1): Source {
		const divisions = subdivideString(this.str, order + 1);
		const counts = count(divisions);
		const keysCount = count(divisions.map((el) => el.slice(0, -1)));

		const symbols = Object.keys(counts).sort();
		const probabilities = symbols.map(k => counts[k] / keysCount[k.slice(0, -1)]);
		
		return new Source(symbols, probabilities);
	}
}

const markovSorce = new Markov('abracadabra');

console.log(markovSorce.getMarkovSource(1));
console.log(markovSorce.getMarkovSource(2));