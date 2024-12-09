import { assert } from "console";

function arrayAsTriangle<T>(arr: T[]): T[][] {
	const firstRowLength = (-1 + Math.sqrt(1 + 8 * arr.length)) / 2;
	if(!Number.isInteger(firstRowLength)) throw new Error('Invalid arr length');

	let n = firstRowLength;
	const triangle = [];

	let index = 0;
	while(index < arr.length){
		triangle.push(arr.slice(index, index + n));
		index += n;
		n--;
	}

	return triangle;
}

function calcParityBits(triangle: number[][]): number[] {
	const parityBits = [];

	for(let i = 0; i < triangle.length; i++){
		const j = triangle.length - i - 1;

		let parity = 0;
		for(const elem of triangle[i]!){ 
			parity ^= elem; // elements in row
		}

		for(const row of triangle){
			if(row[j] !== undefined){
				parity ^= row[j]; // elements in column
			}
		}

		parityBits.push(parity);
	}

	return parityBits;
}

const triangle = {
	encode(data: string): string {
		const triangle = arrayAsTriangle(data.split('').map(Number));
		triangle.push([]);
		
		const parityBits = calcParityBits(triangle);
	
		for(let i = 0; i < parityBits.length; i++){
			triangle[i]!.push(parityBits[i]!);
		}
	
		return triangle.map(x => x.join('')).join('');
	},
	decode(data: string): string {
		const triangle = arrayAsTriangle(data.split('').map(Number));
	
		const parityBits = triangle.map(row => row.pop()!);
		const parityBitsCalc = calcParityBits(triangle);
	
		for(let i = 0; i < parityBits.length; i++){
			if(parityBits[i] !== parityBitsCalc[i]){
				console.log(`Error con el bit de paridad ${i}`);
			}
		}
	
		return triangle.flat().join('');
	}
};

const chunkArray = (arr: any[], chunkSize: number): any[] => {
	const chunkedArr = [];
	let index = 0;
	while(index < arr.length){
		chunkedArr.push(arr.slice(index, index += chunkSize));
	}
	return chunkedArr;
}

const rectangle = {
	encode(data: string, rows: number, columns: number): string {
		const dataMatrix = chunkArray(data.split('').map(Number), columns);
	
		const colParities = Array(columns).fill(0);
	
		for (let i = 0; i < rows; i++) {
			let rowParity = 0;
			for (let j = 0; j < columns; j++) {
				rowParity ^= dataMatrix[i]![j]!;
				colParities[j] ^= dataMatrix[i]![j]!;
			}
	
			dataMatrix[i]!.push(rowParity);
		}
	
		dataMatrix.push(colParities);
	
		return dataMatrix.map(row => row.join('')).join('');
	},
	decode(data: string, rows: number, columns: number): string {
		const dataMatrix = chunkArray(data.split('').map(Number), columns + 1);
		let result = '';
	
		const colParities = Array(columns).fill(0);
	
		for(let i = 0; i < rows; i++) {
			let rowParity = 0;
			for(let j = 0; j < columns; j++) {
				rowParity ^= dataMatrix[i]![j]!;
				colParities[j] ^= dataMatrix[i]![j]!;
				result += dataMatrix[i]![j]!;
			}
	
			if(rowParity !== dataMatrix[i]![columns]!) {
				console.log(`Error en la fila ${i}`);
			}
		}
	
		for(let i = 0; i < columns; i++) {
			if(colParities[i] !== dataMatrix[rows]![i]!) {
				console.log(`Error en la columna ${i}`);
			}
		}
	
		return result;
	}
}

if(require.main === module){
	function testCoding(encoding: unknown, data: string, encodedData: string, ...args: unknown[]){
		// @ts-ignore
		const encoded = encoding.encode(data, ...args);
		// @ts-ignore
		const decoded = encoding.decode(encoded, ...args);

		assert(data === decoded, `Error en ${data} -> ${encoded} -> ${decoded}`);
		assert(encoded === encodedData, `Error en ${data} -> ${encoded} -> ${decoded}`);
	}

	testCoding(rectangle, '01001101011001010101', '01001010101110010010101111011', 4, 5);
	testCoding(triangle, '101111001101001', '101110100111010000110');

	console.log(triangle.encode('101111001101001'))
	console.log(triangle.decode('101110100111010000110'))
}