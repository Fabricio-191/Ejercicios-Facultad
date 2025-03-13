import { assert } from "console";

const DEFAULT_ALPHABET = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ".split('');
const DEFAULT_ALPHABET2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split('');
const isPermutationOf = (source: unknown[], target: unknown[]) => (new Set(target)).size === target.length && source.every(n => target.includes(n));
const subdivide = (iterable: string, size: number) => {
	const result = [];

	for(let i = 0; i < iterable.length; i += size) {
		result.push(iterable.slice(i, i + size));
	}

	return result;
}
const frecuencies = (text: string) => {
	const freq: Record<string, number> = {};
	for(const char of text) {
		freq[char] = (freq[char] ?? 0) + 1;
	}

	return freq;
}

const mostFrequent = (text: string) => {
	const freq = frecuencies(text);
	return Object.entries(freq).reduce((acc, [char, count]) => count > acc[1] ? [char, count] : acc, ['', 0])[0];
}

function* range(start: number, end: number) {
	for(let i = start; i < end; i++) yield i;
}

const xor = (a: string, b: string) => a == b ? '0' : '1';

interface Cipher {
	cipher(text: string, ...args: unknown[]): string;
	decipher(text: string, ...args: unknown[]): string;
	forceDecipher?(text: string, ...args: unknown[]): string;
	findKey?(cipheredText: string, ...args: unknown[]): string;
};

const invertTranspositionKey = (key: number[]) => key.map((_, i) => key.indexOf(i + 1) + 1);

const ROT = {
	cipher(text: string, rot = 13, alphabet = DEFAULT_ALPHABET): string {
		while(rot < 0) rot += alphabet.length;

		return text.split('').map(char => {
			const index = alphabet.indexOf(char.toUpperCase());
			if(index === -1) return char;

			const newIndex = (index + rot) % alphabet.length;
			return alphabet[newIndex];
		}).join('');
	},
	decipher(text: string, rot = 13, alphabet = DEFAULT_ALPHABET): string {
		return this.cipher(text, -rot, alphabet);
	},
	forceDecipher(text: string, mostFrequentSymbol = 'E', alphabet = DEFAULT_ALPHABET): string {
		const pivot = mostFrequent(text);
		const rot = (alphabet.indexOf(pivot) - alphabet.indexOf(mostFrequentSymbol) + alphabet.length) % alphabet.length;
	
		return ROT.decipher(text, rot, alphabet);
	}
} as const;

const Vigenere = {
	cipher(text: string, key: string, alphabet = DEFAULT_ALPHABET): string {
		return text.split('').map((char, i) => {
			const index = alphabet.indexOf(char.toUpperCase());
			if(index === -1) return char;

			const keyIndex = alphabet.indexOf(key[i % key.length]!.toUpperCase());
			const newIndex = (index + keyIndex) % alphabet.length;
			return alphabet[newIndex];
		}).join('');
	},
	decipher(text: string, key: string, alphabet = DEFAULT_ALPHABET): string {
		return text.split('').map((char, i) => {
			const index = alphabet.indexOf(char.toUpperCase());
			if(index === -1) return char;

			const keyIndex = alphabet.indexOf(key[i % key.length]!.toUpperCase());
			const newIndex = (index - keyIndex + alphabet.length) % alphabet.length;
			return alphabet[newIndex];
		}).join('');
	},
	findKey(cipherText: string, cleanText: string, keyLength: number, alphabet = DEFAULT_ALPHABET): string {
		let key = '';

		for(let i = 0; i < keyLength; i++) {
			const diff = alphabet.indexOf(cipherText[i]!) - alphabet.indexOf(cleanText[i]!);
			const keyIndex = (diff + alphabet.length) % alphabet.length;

			key += alphabet[keyIndex];
		}		

		return key;
	},
} as const;

function transpositionKey(key: number[]): number[] {
	if(!isPermutationOf([...range(1, key.length)], key)) {
		throw new Error('Key must be a permutation of 1 to key.length');
	}

	return key.map(n => n - 1);
}

const SIMPLE_TRANSPOSITION = {
	cipher(text: string, key: number[]): string {
		if(text.length % key.length !== 0) throw new Error('Text length must be multiple of key length');
		key = transpositionKey(key);

		return subdivide(text, key.length).map(text => key.map(val => text[val]).join('')).join('');
	},
	decipher(text: string, key: number[]): string {
		return this.cipher(text, invertTranspositionKey(key));
	}
} as const;

const COLUMN_TRANSPOSITION = {
	cipher(text: string, key: number[]): string {
		if(text.length % key.length !== 0) throw new Error('Text length must be multiple of key length');
		key = transpositionKey(key);

		const rows = subdivide(text, key.length);

		let result = '';
		for(const val of key) {
			for(const row of rows) {
				result += row[val];
			}
		}

		return result;
	},
	decipher(text: string, key: number[]): string {
		if(text.length % key.length !== 0) throw new Error('Text length must be multiple of key length');
		key = transpositionKey(invertTranspositionKey(key));

		const columnLength = text.length / key.length;
		const columns = subdivide(text, columnLength);

		let result = '';
		for(let i = 0; i < columnLength; i++) {
			result += key.map(val => columns[val]![i]).join('');
		}

		return result;
	}
} as const;

const SHIFT_REGISTERS = {
	generate(seed: string = '0001', feedbackFn: (registers: string) => string): string {
		let registers = seed;
		let result = '';
		while(true){
			const feedback = feedbackFn(registers);
			if(feedback.length !== 1) throw new Error('Feedback function must return a single character');
			registers = feedback + registers.slice(0, -1);

			if(registers === seed) break;

			result += feedback;
		}

		return result;
	},
	cipher(text: string, seed: string, feedbackFn: (registers: string) => string): string {
		const keystream = this.generate(seed, feedbackFn);
		const binaryText = text.split('').map(char => char.charCodeAt(0).toString(2).padStart(8, '0')).join('');

		return binaryText.split('')
			.map((char, i) => xor(char, keystream[i % keystream.length]!))
			.join('');
	},
	decipher(binaryText: string, seed: string, feedbackFn: (registers: string) => string): string {
		const keystream = this.generate(seed, feedbackFn);

		return subdivide(binaryText, keystream.length).map((char, i) => xor(char, keystream[i % keystream.length]!)).join('');
	}
}

if(require.main === module) {
	function testCipher(
		cipher: Cipher,
		text: string,
		result: string | null = null,
		cipherArgs: unknown[] = [],
		forceDecipherArgs: unknown[] = []
	) {
		const encrypted = cipher.cipher(text, ...cipherArgs);
		if(result) assert(result === encrypted, 'Encrypted text does not match expected result');
	
		const decrypted = cipher.decipher(encrypted, ...cipherArgs);
		assert(text === decrypted, 'Decrypted text does not match original text');
	
		if(cipher.forceDecipher) {
			const decrypted2 = cipher.forceDecipher(encrypted, ...forceDecipherArgs);
			assert(text === decrypted2, 'Decrypted (forced) text does not match original text');
		}
	}

	// Cipher, text, result | null, cipherArgs, forceDecipherArgs
	testCipher(ROT                 , 'HOLAAMIGOS'           , null          , []       , ['O'])
	testCipher(ROT                 , 'AHIVALABOMBA'         , null          , []       , ['A']);
	testCipher(Vigenere            , 'HOLAAMIGOS'           , 'JWPRAÑPLGS'  , ['CIFRA']);
	testCipher(Vigenere            , 'ESLOINESPERADOLOQUESIEMPREOCURRE', 'GHVDAFYLRSCOVHFHSJOHAWGITSZQNKMW', ['COLOSSUS']);
	testCipher(SIMPLE_TRANSPOSITION, 'AHIVALABOMBA'         , 'IAVHAABLBOAM', [[3, 1, 4, 2]]);
	testCipher(SIMPLE_TRANSPOSITION, 'NO POR MUCHO MADRUGAR', null, [[3, 7, 2, 6, 4, 1, 5]]);
	testCipher(COLUMN_TRANSPOSITION, 'AHIVALABOMBA'         , 'VBAHLMIABAAO', [[4, 2, 3, 1]]);
	testCipher(COLUMN_TRANSPOSITION, 'NO POR MUCHO MADRUGAR', null, [[3, 7, 2, 6, 4, 1, 5]]);
	// testCipher(SHIFT_REGISTERS, 'HOLAAMIGOS', null, ['1001', (registers: string) => xor(registers[0]!, registers[3]!)]);

	assert(ROT.forceDecipher('MXDQLWR', 'J', DEFAULT_ALPHABET2) === 'JUANITO');
	assert(Vigenere.findKey('JWPRAÑPLGS', 'HOLAAMIGOS', 5) === 'CIFRA');
	assert(Vigenere.findKey('GHVDAFYLRSCOVHFHSJOHAWGITSZQNKMW', 'ESLOINESPERADOLOQUESIEMPREOCURRE', 8) === 'COLOSSUS');
}
