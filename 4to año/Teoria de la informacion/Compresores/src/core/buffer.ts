export const ascii = (str: string) => str.charCodeAt(0); // Returns the ASCII code of the first character of the string
export const chr = (num: number) => String.fromCharCode(num); //

abstract class BitBuffer {
	constructor(bits: bigint, length: number) {
		if(bits.toString(2).length > length) {
			throw new Error('The length is too small for the given bits');
		}

		this.bits = bits;
		this.length = length;
	}

	protected bits: bigint;
	public length: number;
}

export class BitBufferWriter extends BitBuffer {
	constructor(bits: bigint = 0n, length: number = 0) {
		super(bits, length);
	}

	addBits(value: number, length: number): void {
		if(2 ** length <= value) {
			throw new Error('Value is too big for the given length');
		}	

		this.bits = this.bits << BigInt(length) | BigInt(value);
		this.length += length;
	}

	addBit(value: boolean): void {
		this.addBits(value ? 1 : 0, 1);
	}

	addByte(value: number): void {
		this.addBits(value, 8);
	}

	addChar(value: string): void {
		if(value.length !== 1) {
			throw new Error('The value must be a single character');
		}

		this.addByte(ascii(value));
	}

	toString(base: number): string {
		return this.bits.toString(base).padStart(this.length, '0');
	}
}

export class BitBufferReader extends BitBuffer {
	private offset = 0;

	get remaining(): number {
		if(this.offset > this.length) {
			throw new Error('The offset is greater than the length');
		}
		return this.length - this.offset;
	}

	readBits(length: number): number {
		if(length > 53) {
			throw new Error('The length must be less than 54');
		}

		const mask = (1n << BigInt(length)) - 1n;
		const value = Number(this.bits >> BigInt(this.length - this.offset - length) & mask);

		this.offset += length;
		return value
	}

	readBit(): boolean {
		return Boolean(this.readBits(1));
	}

	readByte(): number {
		return this.readBits(8);
	}

	readChar(): string {
		return chr(this.readByte());
	}

	static fromBinary(str: string): BitBufferReader {
		return new BitBufferReader(BigInt('0b' + str), str.length);
	}
}


if(require.main === module) {
	const bufferWriter = new BitBufferWriter();
	bufferWriter.addBits(0b100, 3);
	bufferWriter.addBit(true);
	bufferWriter.addBit(false);
	bufferWriter.addByte(0b1000111);

	console.log(bufferWriter.toString(2) === '1001001000111');
	console.log(bufferWriter.length === 13);

	const bufferReader = BitBufferReader.fromBinary(bufferWriter.toString(2));

	console.log(bufferReader.readBits(3) === 0b100);
	console.log(bufferReader.readBit() === true);
	console.log(bufferReader.readBit() === false);
	console.log(bufferReader.readByte() === 0b1000111);
}