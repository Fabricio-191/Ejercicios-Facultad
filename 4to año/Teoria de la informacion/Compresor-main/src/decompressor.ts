// Clase para leer bits de un string binario
class BinaryReader {
	constructor(
		private str: string
	) {}
	private offset = 0; // se lleva la cuenta de cuantos bits se han leido

	// se lee un numero de bits y se convierte a entero
	public readNumber(length: number): number {
		this.offset += length;
		
		if(this.offset > this.str.length) {
			throw new Error('Out of bounds');
		}

		return parseInt(this.str.slice(this.offset - length, this.offset), 2);
	}

	public readByte(): number {
		return this.readNumber(8);
	}

	public readChar(): string {
		return String.fromCharCode(this.readByte());
	}

	public readCode(length: number): string {
		this.offset += length;
		return this.str.slice(this.offset - length, this.offset);
	}

	// se devuelve los bits que no se han leido en forma de string
	public remaining(): string {
		return this.str.slice(this.offset);
	}
}

// Clase para descomprimir Shannon
class ShannonDecompressor {
	constructor(
		public readonly codes: Record<string, string>, // diccionario de symbolos a codigos
	) {}

    get symbols(): string[] {
        return Object.keys(this.codes); // devuelve una lista de simbolos
    }

	public decodeOne(str: string): [string, string] {
		const symbol = this.symbols.find(symbol => str.startsWith(this.codes[symbol]!));
		// se busca el simbolo cuyo codigo sea el prefijo de la cadena
		// nota: no hay ambiguedad porque los codigos son prefijos unicos

		if(!symbol) throw new Error('Invalid symbol');
		
		return [symbol, this.codes[symbol]!]; // se devuelve el simbolo y su codigo
	}

	// se obtiene la codificacion de shannon a partir de el binario
	public static fromBinary(reader: BinaryReader, pseudoASCII: Record<string, string>, minSymbolLength: number): ShannonDecompressor {
		const symbolsAmount = reader.readNumber(minSymbolLength); // se lee la cantidad de simbolos
		const codes: Record<string, string> = {};

		for(let i = 0; i < symbolsAmount; i++) { // por cada simbolo
			const symbol = reader.readCode(minSymbolLength); // se lee el PseudoASCII del simbolo
			const codeLength = reader.readNumber(minSymbolLength); // se lee la longitud del codigo
			const code = reader.readCode(codeLength); // se lee el codigo
			codes[pseudoASCII[symbol]!] = code; // se guarda el codigo en el diccionario
		}

		return new ShannonDecompressor(codes); // se devuelve el descompresor
	}
}

class MarkovDecompressor {
	constructor(
		public readonly symbols: string[], // lista de simbolos
		public readonly minSymbolLength: number, // longitud minima de los codigos del PseudoASCII
		public readonly pseudoASCII: Record<string, string>, // diccionario simbolos y su pseudoASCII
		public readonly codifications: { // diccionario de codificaciones de Shannon
			[key: string]: ShannonDecompressor,
		},
	) {}

	// se decodifica un simbolo a partir de su PseudoASCII
    private decodeASCII(str: string): [string, string] {
        const code = str.slice(0, this.minSymbolLength);
        const symbol = this.pseudoASCII[code];

		if(!symbol) throw new Error('Invalid symbol');

        return [symbol, code]; // se devuelve el simbolo y su PseudoASCII
    }

	// se decodifica una cadena en binario
	public decode(str: string): string {
		let decoded = '';

		while(str.length) {
			const [symbol, code] = decoded.length < 2 ? 
				this.decodeASCII(str) : // Se decodifican los primeros 2 simbolos a partir de su PseudoASCII
				this.codifications[decoded.slice(-2)]!.decodeOne(str); // Se decodifican los demas simbolos a partir de las codificaciones de Shannon
				
			decoded += symbol; // se agrega el simbolo decodificado
			str = str.slice(code.length); // se elimina el codigo del simbolo decodificado
		}

		return decoded;
	}

	// se obtiene el descompresor de Markov a partir del binario
	static fromBinary(reader: BinaryReader): [MarkovDecompressor, string] {
		const symbols: string[] = []; // lista de simbolos
		const codifications: Record<string, ShannonDecompressor> = {}; // diccionario de codificaciones de Shannon

		const symbolsAmount = reader.readByte(); // se lee la cantidad de simbolos
		for(let i = 0; i < symbolsAmount; i++) {
			symbols.push(reader.readChar()); // se lee cada simbolo ASCII
		}

		// se recrea el pseudoASCII a partir de los simbolos
		const minSymbolLength =  Math.ceil(Math.log2(symbolsAmount)); 
		const pseudoASCII: Record<string, string> = {};
		for(let i = 0; i < symbols.length; i++) {
			const symbol = symbols[i]!;
			const code = i.toString(2).padStart(minSymbolLength, '0');

            pseudoASCII[code] = symbol;
        };

		const codificationsAmount = reader.readNumber(16); // se lee la cantidad de codificaciones

		for(let i = 0; i < codificationsAmount; i++) {
			const key = // se leen 2 simbolos los cuales son la clave de la codificacion (predecesor)
				pseudoASCII[reader.readCode(minSymbolLength)]! +
				pseudoASCII[reader.readCode(minSymbolLength)]!;
			
			// se obtiene y guarda la codificacion de Shannon en el diccionario
			codifications[key] = ShannonDecompressor.fromBinary(reader, pseudoASCII, minSymbolLength);
		}

		// se crea el descompresor de Markov y se devuelve junto con el resto de la cadena
		const decompressor = new MarkovDecompressor(
			symbols, 
			minSymbolLength,
			pseudoASCII,
			codifications,
		);

		return [decompressor, reader.remaining()];
	}
}

export default function decode(buffer: Buffer): string {
	const encoded = [...buffer].map(byte => byte.toString(2).padStart(8, '0')).join(''); // convierte el buffer a un string binario
	// TODO: dejar de usar strings binarias y usar un bit buffer

	const reader = new BinaryReader(encoded); // se crea un lector binario
	const filler = reader.readNumber(3); // se lee cuantos bits hay de relleno
	if(filler !== 0) {
		// si hay relleno, se lee el relleno y se verifica que sean 0's
		if(reader.readNumber(filler) !== 0) throw new Error('Invalid filler');
	}

	// se crea un descompresor de Markov a partir de los datos serializados y se devuelve el resto de la cadena
	const [decompressor, str] = MarkovDecompressor.fromBinary(reader);
	// se decodifica la cadena y se devuelve
	return decompressor.decode(str);
}