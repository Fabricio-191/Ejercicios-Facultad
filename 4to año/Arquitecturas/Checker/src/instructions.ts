import { State } from './index';

export class Memory {
	constructor(size: number) {
		this.data = new Array(size).fill(0);
	}

	private readonly data: number[];

	public readByte(address: number): number {
		if(address < 0 || address >= this.data.length) throw new Error(`Invalid address: ${address}`);

		return this.data[address]!;
	}

	public writeByte(address: number, value: number) {
		if(address < 0 || address >= this.data.length) throw new Error(`Invalid address: ${address}`);

		if(value < 0 || value > 255) throw new Error(`Invalid value: ${value}`);

		this.data[address] = value;
	}

	public readWord(address: number): number {
		if(address < 0 || address >= this.data.length) throw new Error(`Invalid address: ${address}`);

		return (this.data[address]! << 24) +
			(this.data[address + 1]! << 16) +
			(this.data[address + 2]! << 8) +
			this.data[address + 3]!;
	}

	public writeWord(address: number, value: number) {
		if(address < 0 || address >= this.data.length) throw new Error(`Invalid address: ${address}`);

		if(value < 0 || value > 0xFFFFFFFF) throw new Error(`Invalid value: ${value}`);

		this.data[address] = (value >> 24) & 0xFF;
		this.data[address + 1] = (value >> 16) & 0xFF;
		this.data[address + 2] = (value >> 8) & 0xFF;
		this.data[address + 3] = value & 0xFF;
	}

	[Symbol.for('nodejs.util.inspect.custom')]() {
		let str = `Memory[${this.data.length}]`;

		for(let i = 0; i < this.data.length; i += 4) {
			const value = this.readWord(i);
			str += `\n${i.toString(16).padStart(4, '0')}: ${value.toString(16).padStart(8, '0')}`;
		}

		return str;
	}
}

export class Registers {
	constructor() {
		this.registers = new Array(32).fill(0);
	}
	private readonly registers: number[];

	public write(register: number, value: number) {
		if(register === 0) throw new Error('Cannot write to register 0');
		if(register < 0 || register >= this.registers.length) throw new Error(`Invalid register: ${register}`);

		this.registers[register] = value;
	}

	public read(register: number): number {
		if(register < 0 || register >= this.registers.length) throw new Error(`Invalid register: ${register}`);

		return this.registers[register]!;
	}
}


export type Register = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31;
export type RegisterAnnotation = `r${Register}`;

export type Immediate = number;
export type Address = number;
export type ImmediateAnnotation = `${number}` | `#${number}` | `0x${string}`;
export type AddressAnnotation = `${ImmediateAnnotation}(${RegisterAnnotation})`;

export interface Instruction<T extends unknown[]> {
	name: string;
	type: 'R' | 'I' | 'J';
	accessMemory?: boolean;
	run: (...args: T) => void;
	operands: Array<'register' | 'address' | 'immediate'>;
};

export const validateOperands = {
	register(operand: string): Register {
		if(!operand.startsWith('r')) throw new Error(`Invalid register: ${operand}`);
		const register = Number(operand.slice(1));

		if(register < 0 || register > 31) throw new Error(`Invalid register: ${operand}`);
		return register as Register;
	},
	immediate(operand: string): number {
		if(operand.startsWith('#')) return Number(operand.slice(1));
		if(operand.startsWith('0x')) return parseInt(operand.slice(2), 16);
		return Number(operand);
	},
	address(operand: string): Address {
		const match = operand.match(/^(\d+)\((r\d+)\)$/) as null | [string, string, string];
		if(!match) throw new Error(`Invalid address: ${operand}`);
		const offset = Number(match[1]);
		const register = validateOperands.register(match[2]);
		return offset + register;
	},
}

export const instructions: Instruction<any[]>[] = [
	{
		name: 'SW', // Store Word
		type: 'I',
		accessMemory: true,
		operands: ['address', 'register'],
		run(state: State, address: Address, register: Register){
			const registerValue = state.registers.read(register);
			state.memory.writeWord(address, registerValue);
		},
	},
	{
		name: 'LW', // Load Word
		type: 'I',
		operands: ['register', 'address'],
		run(state: State, register: Register, address: Address){
			const value = state.memory.readWord(address);
			state.registers.write(register, value);
		},
	},
	{
		name: 'ADDI', // Add Immediate
		type: 'I',
		operands: ['register', 'register', 'immediate'],
		run(state: State, dest: Register, source: Register, immediate: number){
			const sourceValue = state.registers.read(source);
			state.registers.write(dest, sourceValue + immediate);
		},
	},
	{
		name: 'ADD', // Add
		type: 'R',
		operands: ['register', 'register', 'register'],
		run(state: State, dest: Register, source1: Register, source2: Register){
			const source1Value = state.registers.read(source1);
			const source2Value = state.registers.read(source2);
			state.registers.write(dest, source1Value + source2Value);
		},
	},
	{
		name: 'SUB', // Subtract
		type: 'R',
		operands: ['register', 'register', 'register'],
		run(state: State, dest: Register, source1: Register, source2: Register){
			const source1Value = state.registers.read(source1);
			const source2Value = state.registers.read(source2);
			state.registers.write(dest, source1Value - source2Value);
		},
	},
	{
		name: 'SUBI', // Subtract Immediate
		type: 'I',
		operands: ['register', 'register', 'immediate'],
		run(state: State, dest: Register, source: Register, immediate: number){
			const sourceValue = state.registers.read(source);
			state.registers.write(dest, sourceValue - immediate);
		},
	},
	{
		name: 'NOP',
		type: 'J',
		operands: [],
		run(state: State){
			// do nothing
		},
	},
	{
		name: 'JAL', // Jump and Link
		type: 'J',
		operands: ['address'],
		run(state: State, address: Address){
			state.registers.write(31, state.pc);
			state.pc = address;
		},
	},
	{
		name: 'JR', // Jump Register
		type: 'J',
		operands: ['register'],
		run(state: State, register: Register){
			state.pc = state.registers.read(register);
		},
	},
	{
		name: 'BEQZ', // Branch if Equal to Zero
		type: 'I',
		operands: ['register', 'address'],
		run(state: State, register: Register, address: Address){
			const registerValue = state.registers.read(register);
			if(registerValue === 0) state.pc = address;
		},
	},
	{
		name: 'BNEZ', // Branch if Not Equal to Zero
		type: 'I',
		operands: ['register', 'address'],
		run(state: State, register: Register, address: Address){
			const registerValue = state.registers.read(register);
			if(registerValue !== 0) state.pc = address;
		},
	},
	{
		name: 'TRAP',
		type: 'J',
		operands: ['immediate'],
		run(state: State, immediate: number){
			// do nothing
		},
	},
] as const;

/*

const instructionsTypes = [
	{ // tipo R, 2 operadores
		list: [
			'MOVF', 'MOVD',
		],
		operands: [
			['register', 'WRITE'],
			['register', 'READ' ],
		],
	},
	{ // tipo I, 3 operadores
		list: [
			'ADDI', 'ADDUI', 'SUBI', 'SUBUI',
			'ANDI', 'ORI', 'XORI',
			'SLLI', 'SRLI', 'SRAI',
			'SLTI', 'SGTI', 'SLEI', 'SGEI', 'SEQI', 'SNEI',
		],
		operands: [
			['register', 'WRITE'],
			['register', 'READ'],
			['immediate', null],
		],
	},
	{ // tipo R, 3 operadores
		list: [
			'ADD', 'ADDU', 'SUB', 'SUBU', 'MULT', 'MULTU', 'DIV', 'DIVU',
			'AND', 'OR', 'XOR',
			'SLL', 'SRL', 'SRA',
			'SLT', 'SGT', 'SLE', 'SGE', 'SEQ', 'SNE',
		],
		operands: [
			['register', 'WRITE'],
			['register', 'READ' ],
			['register', 'READ' ],
		],
	},
	{ // BRANCH
		list: [
			'BEQZ', 'BNEZ',
		],
		operands: [
			['register', 'READ'],
			['label', null],
		],
	},
	{ // JUMP (tipo I)
		list: [
			'JR', 'JALR',
		],
		operands: [
			['register', 'READ'],
		],
	},
	{ // tipo J
		list: [
			'J', 'JAL', // JUMP
			'TRAP', 'RFE',
		],
		operands: [
			['label', null],
		],
	},
	{
		list: [
			'NOP',
		],
		operands: [],
	},
] as const;

*/