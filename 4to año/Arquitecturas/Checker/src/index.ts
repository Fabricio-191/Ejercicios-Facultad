const code = `
        ADDI r1, r0, #a      ; r1 = 0x1000
        ADDI r2, r0, #b      ; r2 = 0x1100
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

class Instruction2 {
	private static regex = /^\s*((?<label>\w+):)?\s*((?<instr>\w+)\s*(?<operands>.+?)?)\s*(;\s*(?<comment>.+))?\s*$/;

	constructor(line: string) {
		const match = line.match(Instruction2.regex);
		if(!match?.groups?.['instr']) throw new Error(`Invalid line: ${line}`);

		this.line = line;
		this.label = match.groups['label'] || null;
		this.comment = match.groups['comment'] || null;
		this.instruction = match.groups['instr'];
		this.operands = match.groups['operands']?.split(',').map(operand => operand.trim()) || [];
	}
	public readonly line: string;
	public readonly label: string | null;
	public readonly instruction: string;
	public readonly operands: string[] ;
	public readonly comment: string | null;
}


abstract class Runner {
	constructor() {
		this.memory = new Memory(10000);
		this.registers = new Registers();
		this.pc = 0;
	}

	public readonly memory: Memory;
	public readonly registers: Registers;
	public pc: number;

	public abstract run(): void;
}

class UnicicleRunner extends Runner {
	public run(code: string): void {
		const instructions = code.split('\n')
			.map(line => line.trim())
			.filter(line => line !== '')
			.map(line => new Instruction2(line));

		while(this.pc < instructions.length) {
			this.pc++;
			instructions[this.pc]!.run(this);
		}
	}
}

function runUnicycle(instructions: Instruction2[]) {
	const state = new ComputerState();
	while(state.pc < instructions.length) {
		state.pc++;
		instructions[state.pc]!.run(state);
	}
}