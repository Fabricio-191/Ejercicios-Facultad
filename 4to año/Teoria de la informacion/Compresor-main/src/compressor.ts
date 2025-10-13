const sum = (arr: number[]): number => arr.reduce((a, b) => a + b, 0); // suma de los elementos de un array
const subdivideString = (str: string, order: number): string[] => { // divide un string en substrings de un tamaño dado, ej: subdivideString('hola', 2) => ['ho', 'ol', 'la']
	const substrings: string[] = [];
	for (let i = 0; i < str.length - order + 1; i++) {
		substrings.push(str.slice(i, i + order));
	}

	return substrings;
}

// Clase para escribir bits en un buffer de bytes
class BinaryWriter {
	private str: string = ''; // string que contiene los bits TODO: cambiar a Buffer

	get size(): number {
		return this.str.length;
	}

	// Añade un número a la cadena de bits con una longitud dada
	public addNumber(num: number, length: number): void {
		if(num > 2 ** length) {
			throw new Error('Number too big');
		}

		this.str += num.toString(2).padStart(length, '0');
	}

	public addByte(byte: number): void {
		this.addNumber(byte, 8);
	}

	public addChar(char: string): void {
		this.addByte(char.charCodeAt(0));
	}

	public addCode(str: string): void {
		this.str += str;
	}

	// Devuelve la cadena de bits
	public toString(): string {
		return this.str;
	}

	// Devuelve un buffer con los bits escritos (debe ser múltiplo de 8)
	public toBuffer(): Buffer {
		if(this.str.length % 8) {
			throw new Error('Buffer length must be multiple of 8');
		}

		const buffer = Buffer.alloc(this.str.length / 8);

		for(let i = 0; i < this.str.length; i += 8) {
			buffer[i / 8] = parseInt(this.str.slice(i, i + 8), 2);
		}

		return buffer;
	}
}

// Clase para comprimir un conjunto de símbolos con el algoritmo de Shannon
class ShannonCompressor {
	constructor(probabilities: Record<string, number>) { // recibe un objeto con las probabilidades de cada símbolo, ej: { 'a': 0.5, 'b': 0.25, 'c': 0.25 }
		if(Math.abs(sum(Object.values(probabilities)) - 1)  > 0.01) { // revisa que la suma de las probabilidades sea 1
			throw new Error('Probabilities must sum 1');
		}
		this.probabilities = probabilities; // guarda las probabilidades

		this._makeCodes(); // genera los códigos de Shannon
		const codesList = Object.values(this.codes); // lista de códigos

		for(const symbol of this.symbols) { // revisa que los códigos sean prefijo-libres
			if(!this.codes[symbol]) { // si un símbolo no tiene código, lanza un error
				throw new Error('All symbols must have a code');
			}

			const code = this.codes[symbol];
			if(codesList.some(c => code.startsWith(c) && code !== c)) { // si un código es prefijo de otro, lanza un error
				throw new Error('Codes must be prefix-free');
			}
		}
	}
	public readonly probabilities: Record<string, number>; // objeto (diccionario) con las probabilidades de cada símbolo
	public readonly codes: Record<string, string> = {}; // objeto (diccionario) con los códigos de Shannon de cada símbolo

    get symbols(): string[] {
        return Object.keys(this.probabilities); // devuelve una lista con los símbolos
    }

	// Codifica un caracter con los códigos de Shannon
	public encodeOne(str: string): string {
		const code = this.codes[str[0]!]; // busca el primer símbolo de la string

		if(!code) throw new Error('Invalid symbol'); // si no hay símbolo, lanza un error
		
		return code; // devuelve el código del símbolo
	}

	// Codifica un string con los códigos de Shannon
	public encode(str: string): string {
		return str.split('').map(char => this.encodeOne(char)).join(''); // codifica cada caracter y los une
	}

	// Genera un código de Shannon de una longitud dada
	private _makeCode(length: number): string {
		let num = 0;
		
		// basicamente buscamos que num en binario no sea prefijo de ningun otro codigo
		while(num < 2 ** length) {
			const code = num.toString(2).padStart(length, '0'); // num en binario = codigo
			if(!Object.values(this.codes).some(c => code.startsWith(c) || c.startsWith(code))) { // si no es prefijo de ningun otro codigo
				return code; // devolvemos el codigo
			}
			num++; // si no, probamos con el siguiente
		}

		throw new Error('No code found');
	}

	// Genera los códigos de Shannon para cada símbolo
	private _makeCodes(): void {
		for(const symbol of this.symbols) { // recorre los símbolos
			const length = Math.ceil(-Math.log2(
				this.probabilities[symbol]!.valueOf()
			)); // calcula la longitud del código

			this.codes[symbol] = this._makeCode(length); // genera el codigo en base a la longitud
		};
	}

	// Serializa los códigos de Shannon
	public toBinary(writer: BinaryWriter, pseudoASCII: Record<string, string>, minSymbolLength: number): void {
		const entries = Object.entries(this.codes);
		writer.addNumber(entries.length, minSymbolLength); // cantidad de simbolos

		for(const symbol in this.codes) { // recorre los símbolos
			const code = this.codes[symbol]!; 
			writer.addCode(pseudoASCII[symbol]!); // escribe el pseudoASCII del simbolo

			if(code.length > 255) {
				throw new Error('Code too long');
			}

			writer.addNumber(code.length, minSymbolLength); // longitud del codigo
			writer.addCode(code); // escribe el codigo
		}
	}
}

// Clase para comprimir un string con el algoritmo de Markov
class MarkovCompressor  {
	constructor(str: string) {
		this.symbols = Array.from(new Set(str.split(''))).sort(); // crea una lista de símbolos ordenados alfabéticamente sin repeticiones

        this.minSymbolLength = Math.ceil(Math.log2(this.symbols.length)); // calcula la longitud mínima de los símbolos del pseudoASCII
        this.pseudoASCII = {};
		for(let i = 0; i < this.symbols.length; i++) { // genera el pseudoASCII de cada símbolo
			const symbol = this.symbols[i]!;
			const code = i.toString(2).padStart(this.minSymbolLength, '0');

            this.pseudoASCII[symbol] = code; // guarda el pseudoASCII
        };

		this._makeCodes(str); // genera los códigos de Shannon
	}
	private readonly symbols: string[]; // lista de símbolos del string
	private readonly minSymbolLength: number; // longitud mínima de los símbolos del pseudoASCII
	private readonly pseudoASCII: Record<string, string>; // diccionario con el pseudoASCII de cada símbolo
	private readonly codifications: { // diccionario con los compresores de Shannon de cada par de símbolos
		[key: string]: ShannonCompressor,
	} = {};

	private _makeCodes(str: string): void {
		const divisions = subdivideString(str, 3); // divide el string en substrings de longitud 3
		const keys = [...new Set(divisions.map(str => str.slice(0, -1)))]; // de todas las divisiones de 3 caracteres, se toman los primeros 2 caracteres de cada una, y se eliminan las repeticiones

		// entonces keys es una lista de todos los 2 caracteres que preceden a un caracter

		for(const key of keys) {
			const uses = divisions.filter(str => str.startsWith(key)); // se toman todas las divisiones que empiezan con el key
			const probabilities: Record<string, number> = {}; // se crea un objeto con las probabilidades de cada símbolo

			for(const use of uses) { // se recorren todas las divisiones
				const symbol = use.slice(-1); // se toma el último caracter de la división
				probabilities[symbol] = (probabilities[symbol] || 0) + 1; // se aumenta en 1 el contador de ese símbolo
			}

			for(const symbol in probabilities) {
				// se convierten los contadores en probabilidades
				probabilities[symbol] = probabilities[symbol]! / uses.length;
			}

			this.codifications[key] = new ShannonCompressor(probabilities); // se crea un compresor de Shannon con las probabilidades para esa key
		}
		// en resumidas cuentas, dividimos la string de entrada en pares de 3 caracteres 'abc'
		// donde 'ab' es la key y 'c' es el valor
		// para generar la codificacion de shannon para 'ab' buscamos los lugares donde 'ab' es el prefijo y vemos que simbolo sigue
		// hacemos contadores para los simbolos siguientes y los convertimos en probabilidades
	}

	public encode(str: string): string {
		let encoded = '';
		let key = str.slice(0, 2); // se toman los primeros 2 caracteres de la string

		for(let i = 0; i < str.length; i++) {
			if(i < 2) { // si estamos en los primeros 2 caracteres
				encoded += this.pseudoASCII[str[i]!]; // se añade el pseudoASCII del caracter
			}else{
				const codification = this.codifications[key]; // se obtiene la codificación de shannon para ese par de caracteres

				if(!codification) throw new Error('Invalid key'); // si no hay codificación, lanza un error

				encoded += codification.encodeOne(str[i]!); // se añade la codificación de shannon del caracter actual
				key = key[1]! + str[i]!; // se actualiza la key
			}
		}

		return encoded;
	}

	public toBinary(): string {
		const writer = new BinaryWriter(); // crea un escritor de bits

		writer.addByte(this.symbols.length); // se agrega la cantidad de símbolos en un byte (máximo 255 símbolos)
		for(const symbol of this.symbols) {
			writer.addChar(symbol); // se añade el ascii de cada símbolo (recordar que los simbolos estan ordenados alfabeticamente)
		}

		// el pseudoASCII no se envia porque se puede generar a partir de los simbolos
		// para enviar el pseudoASCII hay que enviar el simbolo + el pseudoASCII de cada simbolo lo cual es redundante

		const entries = Object.entries(this.codifications);
		writer.addNumber(entries.length, 16); // cantidad de codificaciones de shannon (maximo 65535)

		console.log('Tamaño antes de las codificaciones de shannon:', writer.size);
		console.log('Cantidad de codificaciones de shannon:', entries.length);
		for(const [key, codification] of entries) { // recorre las codificaciones de shannon
			writer.addCode(this.pseudoASCII[key[0]!]!); // se añade el pseudoASCII del primer caracter de la key
			writer.addCode(this.pseudoASCII[key[1]!]!); // se añade el pseudoASCII del segundo caracter de la key
	
			codification.toBinary(writer, this.pseudoASCII, this.minSymbolLength); // se escribe la codificación de shannon
		}
		console.log('Tamaño despues de las codificaciones de shannon:', writer.size);

		return writer.toString(); // devuelve la cadena de bits
	}
}

export default function encode(str: string): Buffer {
	const markovShannon = new MarkovCompressor(str); // crea un compresor de Markov

	const header = markovShannon.toBinary(); // serializa el compresor de Markov (en una string binaria)
	const encoded = markovShannon.encode(str); // codifica el string (en una string binaria)
	const all = header + encoded; // une la cabecera y el texto codificado

	const writer = new BinaryWriter(); // crea un escritor de bits
	let fillAmount = 8 - ((all.length + 3) % 8);
	// calcula la cantidad de bits que faltan para completar un byte, sin embargo se toma en cuenta que se añadirán 3 bits más para indicar cuántos bits se añadieron
	if(fillAmount === 8) fillAmount = 0; // si es 8, es que ya está completo
	
	writer.addNumber(fillAmount, 3); // añade la cantidad de bits que faltan para completar un byte
	if(fillAmount) writer.addCode('0'.repeat(fillAmount)); // si hay bits que faltan, se añaden 0's
	writer.addCode(all); // añade la cabecera y el texto codificado

	console.log('Tamaño original (en bits):', str.length * 8);
	const compressionRateAll = (all.length / (str.length * 8) * 100).toFixed(1);
	console.log('Tamaño comprimido (en bits):', all.length, `(% ${compressionRateAll} del tamaño original)`);
	console.log('Tamaño de la cabecera (en bits):', header.length);
	const compressionRate = (encoded.length / (str.length * 8) * 100).toFixed(1);
	console.log('Tamaño del texto comprimido (en bits):', encoded.length, `(% ${compressionRate} del tamaño original)`);

	return writer.toBuffer();
}

// encode(require('fs').readFileSync('F:\\Programacion\\Compresor\\prueba.txt', 'binary'));


