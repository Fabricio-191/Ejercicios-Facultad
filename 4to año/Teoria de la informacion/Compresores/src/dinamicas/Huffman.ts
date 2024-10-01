import { assert } from "console";
import { CodificationWithOne } from "../core/base";
import { ASCII } from "../estaticas/ASCII";

class HuffmanNode {
	constructor(
		public weight = 0,
		public parent: HuffmanNode | null = null,
		public symbol: string | null = null
	) {}
	public right: HuffmanNode | null = null;
	public left: HuffmanNode | null = null;

	public replace(a: HuffmanNode, b: HuffmanNode): void {
		if(this.right === a){
			this.right = b;
		}else if(this.left === a){
			this.left = b;
		}else{
			throw new Error('Node not found');
		}
	}

	get isLeaf(): boolean {
		return this.left === null && this.right === null;
	}
  
	get code(): string {
	  return this.parent ? this.parent.code + (this.parent.right === this ? '1' : '0') : ''
	}
}

class HuffmanTree {
	constructor() {
		this.emptyNode = this.root = new HuffmanNode()
		this.nodes = {}
	}
	public emptyNode: HuffmanNode;
	public root: HuffmanNode;
	public nodes: Record<string, HuffmanNode>;

	protected getCodeForSymbol(c: string): string | null {
		return this.nodes[c]?.code || null;
	}

	protected getNodeFromCode(code: string): HuffmanNode {
		let p: HuffmanNode = this.root;
		if(p.isLeaf) return p;

		for(const bit of code){
			p = bit === '1' ? p.right! : p.left!;

			if(p.isLeaf) return p; // will not reach the end of the code
		}

		if(!p.isLeaf) throw new Error('Invalid code');

		return p;
	}

	protected addNew(c: string): string {
		const code = this.emptyNode.code || '0';

		const parent = this.emptyNode;
		const rightNode = new HuffmanNode(0, parent, c);
		const leftNode = new HuffmanNode(0, parent);

		this.nodes[c] = rightNode;
		parent.right = rightNode;
		parent.left = leftNode;
		this.emptyNode = leftNode;
		
		return code;
	}
	  
	protected update(node: HuffmanNode | null) {
		while(node) {
			const leader = this._leaderOfWeight(node.weight);

			if(leader !== node && leader !== node.parent){
				HuffmanTree.swap(leader, node);
			}
				
			node.weight++;
			node = node.parent;
		}
	}

	protected close(): void {
		// eliminate empty node
		const parent = this.emptyNode.parent!;
		const parentParent = parent.parent;
		const sibling = parent.left === this.emptyNode ? parent.right! : parent.left!;

		if(parentParent){
			parentParent!.replace(parent, sibling);
			sibling.parent = parentParent;
		}
	}
	
	private _leaderOfWeight(w: number): HuffmanNode {
		const list = [this.root];
	
		for(const node of list){
			if(node.weight === w) return node;
			if(!node.isLeaf) list.push(node.right!, node.left!);
		}
	
		throw new Error('Never should reach here');
	}

	private static swap(a: HuffmanNode, b: HuffmanNode): void {
		const temp = b.parent!.right;

		a.parent!.replace(a, b);
		
		if(temp === b){
			b.parent!.right = a;
		}else{
			b.parent!.left = a;
		}

		[a.parent, b.parent] = [b.parent, a.parent];
	}

	public print(): void {
		require('print-tree')(
			this.root,
			(node: HuffmanNode) => {
				if(node === this.emptyNode) return 'EMPTY';
				if(node.isLeaf) return `${node.weight} (${node.symbol}: ${node.code})`;

				return node.weight.toString();
			},
			(node: HuffmanNode) => node.isLeaf ? [] : [node.right!, node.left!],
		);
	}
}

const ALL_ASCII: string[] = Array.from({length: 256}, (_, i) => String.fromCharCode(i));

class AdaptiveHuffmanEncoder extends HuffmanTree {
	constructor(
		public defaultCode: CodificationWithOne<string> = ASCII,
		allSymbols: string[] | string = ALL_ASCII
	) {
		super();
		this.allSymbols = new Set(allSymbols);
	}
	private allSymbols: Set<string>;

	encode(str: string): string {
		let encoded = '';
		for(const char of str) {
			encoded += this.encodeOne(char);
			// this.print();
		}

		return encoded;
	}
  
	encodeOne(c: string): string {
		let code = this.getCodeForSymbol(c);
		if(!code){
			code = this.addNew(c) + this.defaultCode.encode(c);

			this.allSymbols.delete(c);
			if(this.allSymbols.size === 0) this.close();
		}

		this.update(this.nodes[c] || null);
		return code;
	}
}

class AdaptiveHuffmanDecoder extends HuffmanTree {
	constructor(
		public defaultCode: CodificationWithOne<string> = ASCII,
		allSymbols?: string[] | string
	) {
		super();
		this.allSymbols = new Set(allSymbols);
		if(!this.defaultCode.decodeOne) throw new Error('DecodeOne not implemented');
	}
	private allSymbols: Set<string>;

	decode(str: string): string {
		let decoded = '';
		let i = 0;
		
		while(i < str.length){
			const [symbol, code] = this.decodeOne(str.slice(i));
			decoded += symbol;
			i += code.length;
			
			this.print();
		}

		return decoded;
	}

	decodeOne(str: string): [string, string] {
		const node = this.getNodeFromCode(str);
		
		if(node.symbol){
			this.update(node);
			return [node.symbol, node.code];
		}
		if(node !== this.emptyNode){
			throw new Error('Invalid code');
		}

		str = str.slice(node.code.length);

		const emptyNodeCode = this.emptyNode.code || '0';
		const [symbol, code] = this.defaultCode.decodeOne!(str);

		this.addNew(symbol);
		this.update(this.nodes[symbol] || null);
		this.allSymbols.delete(symbol);
		if(this.allSymbols.size === 0) this.close();

		return [symbol, emptyNodeCode + code];
	}
}

const MY_ASCII = new ASCII({
	'A': '000',
	'B': '001',
	'R': '010',
	'C': '011',
	'D': '100',
});

function test(testStr: string, ascii: Codification<string>, r: string) {
	const encoded = new AdaptiveHuffmanEncoder(
		ascii,
		testStr,
	).encode(testStr);
	
	assert(r === encoded);

	const decoded = new AdaptiveHuffmanDecoder(
		ascii,
		testStr,
	).decode(encoded);

	console.log(decoded);
	assert(decoded === testStr);
}

test('ABRACADABRA', MY_ASCII, '000000010001001000110110010001101100');
test('ABRACADABRA', ASCII, '0010000010010000100001010010010001000011011000100010001101100');


/*
ABR
4
├─┬ 2
│ ├── 1 (B: 11)
│ └─┬ 1
│   ├── 1 (R: 101)
│   └── EMPTY
└── 2 (A: 0)
5
├─┬ 3
│ ├─┬ 2
│ │ ├── 1 (R: 111)
│ │ └─┬ 1
│ │   ├── 1 (C: 1101)
│ │   └── EMPTY
│ └── 1 (B: 10)
└── 2 (A: 0)
6
├─┬ 3
│ ├─┬ 2
│ │ ├── 1 (R: 111)
│ │ └─┬ 1
│ │   ├── 1 (C: 1101)
│ │   └── EMPTY
│ └── 1 (B: 10)
└── 3 (A: 0)
7
├─┬ 4
│ ├─┬ 2
│ │ ├── 1 (R: 111)
│ │ └── 1 (B: 110)
│ └─┬ 2
│   ├── 1 (C: 101)
│   └── 1 (D: 100)
└── 3 (A: 0)
8
├─┬ 4
│ ├─┬ 2
│ │ ├── 1 (R: 111)
│ │ └── 1 (B: 110)
│ └─┬ 2
│   ├── 1 (C: 101)
│   └── 1 (D: 100)
└── 4 (A: 0)
9
├─┬ 5
│ ├─┬ 3
│ │ ├── 2 (B: 111)
│ │ └── 1 (R: 110)
│ └─┬ 2
│   ├── 1 (C: 101)
│   └── 1 (D: 100)
└── 4 (A: 0)
10
├─┬ 6
│ ├─┬ 4
│ │ ├── 2 (B: 111)
│ │ └── 2 (R: 110)
│ └─┬ 2
│   ├── 1 (C: 101)
│   └── 1 (D: 100)
└── 4 (A: 0)
11
├─┬ 6
│ ├─┬ 4
│ │ ├── 2 (B: 111)
│ │ └── 2 (R: 110)
│ └─┬ 2
│   ├── 1 (C: 101)
│   └── 1 (D: 100)
└── 5 (A: 0)
*/