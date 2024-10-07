import {
	Instruction,
	Register,
	Immediate,
	Address,
	Memory,
	Registers,
	instructions,
	validateOperands
} from './instructions';

const instructionRegex = /^\s*((?<label>\w+):)?\s*((?<instr>\w+)\s*(?<operands>.+?)?)\s*(;\s*(?<comment>.+))?\s*$/;

class ParsedInstruction {
	private static regex = /^\s*((?<label>\w+):)?\s*((?<instr>\w+)\s*(?<operands>.+?)?)\s*(;\s*(?<comment>.+))?\s*$/;

	constructor(line: string) {
		const match = line.match(ParsedInstruction.regex);
		if(!match?.groups?.['instr']) throw new Error(`Invalid line: ${line}`);

		this.line = line;
		this.label = match.groups['label'] || null;
		// this.comment = match.groups['comment'] || null;
		this.instruction = match.groups['instr'];
		this.operands = match.groups['operands']?.split(',').map(operand => operand.trim()) || [];

		this.instructionData = instructions.find(x => x.name === this.instruction)!;
		if(!this.instructionData) throw new Error(`Invalid instruction: ${this.instruction}`);
		if(this.operands.length !== this.instructionData.operands.length) throw new Error(`Invalid operands: ${this.operands}`);
	}
	public readonly line: string;
	public readonly label: string | null;
	public readonly instruction: string;
	public readonly operands: string[];
	public readonly parsedOperands: Array<Register | Immediate | Address> = [];
	public readonly instructionData: Instruction<any>;

	public run(state: State) {

		for(const [i, operand] of this.operands.entries()) {
			const operandType = this.instructionData.operands[i]!;
			this.parsedOperands[i] = validateOperands[operandType](operand);
		}

		this.instructionData.run(state, ...this.parsedOperands);
	}

	static parseCode(code: string): ParsedInstruction[] {
		const instructions = code.split('\n')
			.map(x => x.trim())
			.filter(x => x !== '')
			.map(line => new ParsedInstruction(line));

		const labels = instructions.reduce((acc, instr, i) => {
			if(instr.label) acc[instr.label] = i;
			return acc;
		}, {} as Record<string, number>);

		
	}
}

function parseLine(line: string){
	const match = line.match(instructionRegex);
	if(!match?.groups?.['instr']) throw new Error(`Invalid line: ${line}`);

	return {
		line,
		label: match.groups['label'] || null,
		comment: match.groups['comment'] || null,
		instruction: match.groups['instr'],
		operands: match.groups['operands']?.split(',').map(operand => operand.trim()) || [],
	}
}

function runInstruction(state: State, line: string){
	const instruction = parseLine(line);
}

export class State {
	constructor(
		public readonly memory: Memory = new Memory(10000),
		public readonly registers: Registers = new Registers(),
		public pc: number = 0,
	) {}
}

function runUnicycle(code: string, memory?: Memory) {
	const instructions = ParsedInstruction.parseCode(code);
	const state = new State(memory);
	while(state.pc < instructions.length) {
		state.pc++;
		instructions[state.pc]!.run(state);
	}

	return state;
}

const code = `
        ADDI r1, r0, #0      ; r1 = 0x1000
        ADDI r2, r0, 0x100      ; r2 = 0x1100
        ADDI r2, r2, #76     ; r2 = b + 19 * 4 = b + 76
        ADDI r3, r0, #20     ; r3 = 20

LOOP:   LW r4, 0(r1)         ; r4 = a[0]
        LW r5, 0(r2)         ; r5 = b[19]
        SW 0(r2), r4         ; b[19] = a[0]
        SW 0(r1), r5         ; a[0] = b[19]
        ADDI r1, r1, #4      ; r1++
        SUBI r2, r2, #4      ; r2--
        SUBI r3, r3, #1      ; r3--
        BNEZ r3, LOOP        ; if r3 != 0 goto LOOP
		NOP
        TRAP 0 
`

const memory = new Memory(0x200);

for(let i = 0; i < 20; i++) {
	memory.writeWord(0x000 + i * 4,  i * 4);
	memory.writeWord(0x100 + 19 * 4 - i * 4, i * 4);
}

console.log(
	runUnicycle(code, memory)
)