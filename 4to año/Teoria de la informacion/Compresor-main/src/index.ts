import readline from 'readline';
import compress from './compressor.ts';
import decompress from './decompressor.ts';
import * as fs from 'fs';

function selectFile(message: string): Promise<string> {
	// TODO: Implementar la seleccion de un archivo por medio de un dialogo como https://www.npmjs.com/package/select-files-cli (en español)
	return new Promise((resolve, reject) => {
		rl.question(message, (filePath) => {
			if(!filePath) {
				reject('No se ingreso una ruta');
				return;
			}

			// validar que el archivo exista
			if(!fs.existsSync(filePath)) {
				reject('El archivo no existe');
				return;
			}

			// validar que sea un archivo y no una carpeta
			if(!fs.statSync(filePath).isFile()) {
				reject('El archivo no existe');
				return;
			}

			resolve(filePath);
		});
	})
}

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

rl.question('Que desea hacer?\n1. Comprimir\n2. Descomprimir\n3. Test\n\n', async (answer) => {
	answer = answer.toLowerCase().trim();
	if(answer === 'comprimir' || answer === '1') {
		const filePath = await selectFile('Ingrese la ruta al archivo a comprimir: ');
		
		const data = fs.readFileSync(filePath, 'binary');
		const buffer = compress(data);

		console.log('Archivo comprimido:', filePath + '.shannon');
		fs.writeFileSync(filePath + '.shannon', buffer, 'binary');

		console.log()
	} else if(answer === 'descomprimir' || answer === '2') {
		const filePath = await selectFile('Ingrese la ruta al archivo descomprimir: ');
		const data = Buffer.from(fs.readFileSync(filePath));

		const decompressed = decompress(data);
		const outputFilePath = filePath.replace('.shannon', '.decompressed');

		fs.writeFileSync(outputFilePath, decompressed, 'binary');
		console.log('Archivo descomprimido:', outputFilePath);
		console.log()
	} else if(answer === 'test' || answer === '3') {
		const filePath = await selectFile('Ingrese la ruta al archivo a comprimir: ');
		
		const data = fs.readFileSync(filePath, 'utf8');
		const buffer = compress(data);

		fs.writeFileSync(filePath + '.shannon', buffer, 'binary');

		console.log()
		console.log('Archivo comprimido:', filePath + '.shannon');
		console.log()

		const data2 =  Buffer.from(fs.readFileSync(filePath + '.shannon'));
		const decompressed = decompress(data2);

		console.log('Es igual al original:', data === decompressed);
		
		const outputFilePath = filePath + '.decompressed';
		fs.writeFileSync(outputFilePath, decompressed, 'utf8');

		console.log('Archivo descomprimido:', outputFilePath);
		console.log()
	} else {
		console.log('Opcion invalida');
	}

	rl.close();
});
