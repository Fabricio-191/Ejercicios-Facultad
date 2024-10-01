import { assert } from "console";

export default class BurrowsWheelerTransform {
	public static encode(str: string, indicator = '$'): string {
		str += indicator;
		const rotations = Array(str.length).fill(0).map((_, i) => str.slice(i) + str.slice(0, i));
		const sorted = rotations.sort();
		const encoded = sorted.map(str => str[str.length - 1]).join('');

		return encoded;
	}

	public static decode(str: string, indicator = '$'): string {
		const l_shift = Array.from(str).map((_, i) => i).sort((a, b) => str[a]!.localeCompare(str[b]!));
		const decoded = Array(str.length);

		let x = str.indexOf(indicator);
		for (let i = 0; i < str.length; i++) {
			x = l_shift[x]!;
			decoded[i] = str[x]!;
		}
	 
		return decoded.join('').slice(0, -1);
	}
	
	public static encodeNoIndicator(str: string): [string, number] {
		const rotations = Array(str.length).fill(0).map((_, i) => str.slice(i) + str.slice(0, i));
		const sorted = rotations.sort();

		const rotationIndex = sorted.indexOf(str);
		const encoded = sorted.map(str => str.slice(-1)).join('');

		return [encoded, rotationIndex];
	}

	public static decodeNoIndicator(str: string, rotationIndex: number): string {
		const table = str.split('');
	
		for (let i = 0; i < str.length - 1; i++) {
			table.sort();
			for (let j = 0; j < str.length; j++) {
				table[j] = str[j] + table[j];
			}
		}
	
		console.log(table, rotationIndex);
	
		return table[rotationIndex].slice(1) + table[rotationIndex][0];
	}
}

const test = (testStr: string) => {
	const encoded = BurrowsWheelerTransform.encode(testStr);
	const decoded = BurrowsWheelerTransform.decode(encoded);

	assert(testStr === decoded);

	const encoded2 = BurrowsWheelerTransform.encodeNoIndicator(testStr);
	const decoded2 = BurrowsWheelerTransform.decodeNoIndicator(...encoded2);

	assert(testStr === decoded2);
}

if(require.main === module) {
	test('banana');
	test('abracadabra');
	// test('abracadabra'.repeat(100));
}
