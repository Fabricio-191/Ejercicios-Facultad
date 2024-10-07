class Memory {
	constructor(size: number) {
		this.data = new Array(size).fill(0);
	}

	private readonly data: number[];

	public read(address: number): number {
		if(address < 0 || address >= this.data.length) throw new Error(`Invalid address: ${address}`);

		return this.data[address]!;
	}

	public write(address: number, value: number) {
		if(address < 0 || address >= this.data.length) throw new Error(`Invalid address: ${address}`);
		this.data[address] = value;
	}
}

class Registers extends Memory {
	constructor() {
		super(32);
	}

	public write(register: number, value: number) {
		if(register === 0) throw new Error('Cannot write to register 0');
		super.write(register, value);
	}
}


type Register = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31;
type RegisterAnnotation = `r${Register}`;

type Address = number;
type ImmediateAnnotation = `${number}` | `#${number}` | `0x${string}`;
type AddressAnnotation = `${ImmediateAnnotation}(${RegisterAnnotation})`;

interface Instruction<T extends unknown[]> {
	name: string;
	type: 'R' | 'I' | 'J';
	run: (...args: T) => void;
};

interface Instruction<T extends unknown[]> {
	name: string;
	type: 'R' | 'I' | 'J';
	accessMemory?: boolean;
	run: (...args: T) => void;
	operands: Array<'register' | 'address' | 'immediate'>;
};


const instructions: Instruction<any[]>[] = [
	{
		name: 'SW', // Store Word
		type: 'I',
		accessMemory: true,
		operands: ['address', 'register'],
		run(state: Runner, address: Address, register: Register){
			const registerValue = state.registers.read(register);
			state.memory.write(address, registerValue);
		},
	},
	{
		name: 'LW', // Load Word
		type: 'I',
		operands: ['register', 'address'],
		run(state: Runner, register: Register, address: Address){
			const registerValue = state.registers.read(register);
			state.memory.write(address, registerValue);
		},
	},
	{
		name: 'ADDI', // Add Immediate
		type: 'I',
		operands: ['register', 'register', 'immediate'],
		run(state: Runner, dest: Register, source: Register, immediate: number){
			const sourceValue = state.registers.read(source);
			state.registers.write(dest, sourceValue + immediate);
		},
	},
	{
		name: 'ADD', // Add
		type: 'R',
		operands: ['register', 'register', 'register'],
		run(state: Runner, dest: Register, source1: Register, source2: Register){
			const source1Value = state.registers.read(source1);
			const source2Value = state.registers.read(source2);
			state.registers.write(dest, source1Value + source2Value);
		},
	},
	{
		name: 'NOP',
		type: 'J',
		operands: [],
		run(state: Runner){
			// do nothing
		},
	},
	{
		name: 'JAL', // Jump and Link
		type: 'J',
		operands: ['address'],
		run(state: Runner, address: Address){
			state.registers.write(31, state.pc);
			state.pc = address;
		},
	},
	{
		name: 'JR', // Jump Register
		type: 'J',
		operands: ['register'],
		run(state: Runner, register: Register){
			state.pc = state.registers.read(register);
		},
	},
	{
		name: 'BEQZ', // Branch if Equal to Zero
		type: 'I',
		operands: ['register', 'address'],
		run(state: Runner, register: Register, address: Address){
			const registerValue = state.registers.read(register);
			if(registerValue === 0) state.pc = address;
		},
	},
	{
		name: 'BNEZ', // Branch if Not Equal to Zero
		type: 'I',
		operands: ['register', 'address'],
		run(state: Runner, register: Register, address: Address){
			const registerValue = state.registers.read(register);
			if(registerValue !== 0) state.pc = address;
		},
	},
	{
		name: 'TRAP',
		type: 'J',
		operands: ['immediate'],
		run(state: Runner, immediate: number){
			// do nothing
		},
	},
]

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
