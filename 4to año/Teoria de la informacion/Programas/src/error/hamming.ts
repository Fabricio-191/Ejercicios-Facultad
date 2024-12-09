import { assert } from "console";

const INDEXES = [1, 2, 4, 8, 16, 32, 64, 128] as const;

function addCheckBits(data: number[]): void {
	for(const i of INDEXES){
		if(i > data.length) break;
		data.splice(i - 1, 0, 0); // Add control bits
	}
}

function removeCheckBits(data: number[]): void {
	for(let i = INDEXES.length - 1; i >= 0; i--){
		const index = INDEXES[i]!;
		if(index > data.length) continue;
		data.splice(index - 1, 1); // Remove control bits
	}
}

function calcCheckBits(data: number[]): number[] {
	// Regla general para la posición n es: salta n-1 bits, comprueba n bits, salta n bits, comprueba n bits... Y así sucesivamente.
	const checkBits: number[] = [];

	for(const n of INDEXES) {
		if(n > data.length) break;
		let checkBit = 0;

		let pos = n - 1;
		while(pos < data.length) {
			for(let j = 0; j < n && pos < data.length; j++) {
				checkBit ^= data[pos]!;
				pos++;
			}

			pos += n;
		}

		checkBits.push(checkBit);
	}

	return checkBits;
}

function hammingEncode(data: string | number[]): number[] {
	if(typeof data === 'string') data = data.split('').map(Number);
	data = data.slice(); // Copy the array

	addCheckBits(data);

	const checkBits = calcCheckBits(data);

	let j = 0;
	for(const n of INDEXES){
		if(n > data.length) break;
		data[n - 1] = checkBits[j++]!;
	}

	return data;
}

function hammingDecode(data: string | number[]): number[] {
	if(typeof data === 'string') data = data.split('').map(Number);
	data = data.slice(); // Copy the array

	const checkBits = calcCheckBits(data);

	const errorPos = checkBits.reduce((acc, bit, i) => acc + bit * Math.pow(2, i), 0);
	if(errorPos !== 0){
		data[errorPos - 1]! ^= 1;
	}

	removeCheckBits(data);

	return data;
}

if(require.main === module){
	for(let i = 0; i < 16; i++){
		const data = i.toString(2).padStart(4, '0').split('').map(Number);

		const encoded = hammingEncode(data);
		const decoded = hammingDecode(encoded);

		assert(data.join('') === decoded.join(''), `Error en ${data.join('')} -> ${encoded.join('')} -> ${decoded.join('')}`);

		for(let i = 0; i < 7; i++){
			const corrupted = encoded.slice();
			corrupted[i]! ^= 1;

			const decoded = hammingDecode(corrupted);

			assert(data.join('') === decoded.join(''), `Error en ${data.join('')} -> ${corrupted.join('')} -> ${decoded.join('')}`);
		}
	}
}

console.log(hammingDecode('1001111').join(''))