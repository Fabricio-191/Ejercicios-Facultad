import assert from "assert";
import { BitBufferReader, BitBufferWriter } from "../../core/buffer";
import { Codification } from "../../core/base";

const ascii = (str: string) => str.charCodeAt(0); // Returns the ASCII code of the first character of the string
const chr = (num: number) => String.fromCharCode(num); // Returns the character of the ASCII code

export class LZW implements Codification<string> {
	constructor(windowSize: number) {
		this.windowSize = windowSize;

		assert((windowSize & (windowSize - 1)) === 0, 'The window size must be a power of 2');
	}
	public readonly windowSize: number;

	public encode(str: string): string {
        const dict: Record<string, number> = {};
        let phrase = str[0] as string;

        const out: number[] = [];
        let code = 256;

	    for (const currChar of str.slice(1)) {
            if (dict[phrase + currChar]) {
                phrase += currChar;
            }else {
                out.push(phrase.length > 1 ? dict[phrase]! : ascii(phrase));
                dict[phrase + currChar] = code;
                code++;
                phrase = currChar;
            }
        }

        out.push(phrase.length > 1 ? dict[phrase]! : ascii(phrase));

        return out.map(chr).join("");
	}

	public decode(str: string): string {
        const dict: Record<string, string> = {};
        let currChar = str[0] as string;
        let oldPhrase = currChar;
        const out = [currChar];
		
        let code = 256;
        let phrase;
		for(const char of str.slice(1)) {
			const currCode = ascii(char);

			if (currCode < 256) {
				phrase = char;
			}else{
				phrase = dict[currCode] ?? (oldPhrase + currChar);
			}

			out.push(phrase);
			currChar = phrase.charAt(0);
			dict[code] = oldPhrase + currChar;
			code++;
			oldPhrase = phrase;
		}
		
        return out.join("");
	}
}

export class LZ implements Codification<string> {
	constructor(windowSize: number) {
		this.windowSize = windowSize;

		assert((windowSize & (windowSize - 1)) === 0, 'The window size must be a power of 2');
		
		this.numSize = Math.log2(this.windowSize);
	}
	public readonly windowSize: number;
	private readonly numSize: number;

	public encode(str: string): string {
		const bitBuffer = new BitBufferWriter();

		for(const char of str.slice(0, this.windowSize)) {
			bitBuffer.addChar(char);
		}

		for(let i = this.windowSize; i < str.length; i++) {
			const window = str.slice(i - this.windowSize, i);
			const char = str[i]!;

			const index = window.indexOf(char);

			if(index === -1) {
				bitBuffer.addBit(true);
				bitBuffer.addChar(char);
			}else {
				let count = 1;
				while(str[i + 1] === char) {
					count++;
					i++;
				}

				bitBuffer.addBit(false);
				bitBuffer.addBits(index, this.numSize);
				bitBuffer.addBits(count, this.numSize);
			}
		}

		return bitBuffer.toString(2);
	}

	public decode(str: string): string {
		const bitBuffer = BitBufferReader.fromBinary(str);

		let decoded = '';
		for(let i = 0; i < this.windowSize; i++) {
			decoded += bitBuffer.readChar();
		}

		let i = 0;
		while(bitBuffer.remaining) {
			if(bitBuffer.readBit()) {
				decoded += bitBuffer.readChar();
				i++;
			}else {
				const index = bitBuffer.readBits(this.numSize);
				const count = bitBuffer.readBits(this.numSize);

				decoded += decoded[i + index]!.repeat(count);
				i += count;
			}
		}

		return decoded;
	}
}

if (require.main === module) {
	const testStr = 'a cada chancho le llega su san martin';
	console.log(`Original size: ${testStr.length * 8} bits`);

	const lz = new LZ(16);
	const lzEncoded = lz.encode(testStr);
	assert(lz.decode(lzEncoded) === testStr);
	console.log(`LZ: ${lzEncoded} (${lzEncoded.length} bits)`);

	const lzw = new LZW(16);
	const lzwEncoded = lzw.encode(testStr);
	assert(lzw.decode(lzwEncoded) === testStr);
	console.log(`LZW: ${lzwEncoded} (${lzwEncoded.length * 8} bits)`);
}
