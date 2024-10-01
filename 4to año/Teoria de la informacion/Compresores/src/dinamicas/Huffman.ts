import { assert } from "console";

class HuffmanNode {
	constructor(
		public weight = 0,
		public parent: HuffmanNode | null = null,
		public symbol: string | null = null
	) {}
	public right: HuffmanNode | null = null;
	public left: HuffmanNode | null = null;

	replace(a: HuffmanNode, b: HuffmanNode): void {
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
		this._emptyNode = this._root = new HuffmanNode()
		this._dict = {}
	}
	public _emptyNode: HuffmanNode;
	public _root: HuffmanNode;
	public _dict: Record<string, HuffmanNode>;

	getCode(c: string): string | null {
		return this._dict[c]?.code || null;
	}

	getNodeFromCode(code: string): HuffmanNode {
		let p: HuffmanNode = this._root;
		for(const bit of code){
			p = bit === '1' ? p.right! : p.left!;
			if(p.isLeaf) return p; // will not reach the end of the code
		}

		if(!p.isLeaf) throw new Error('Invalid code');

		return p;
	}

	addNew(c: string): string {
		const code = this._emptyNode.code || '0';

		const parent = this._emptyNode;
		const rightNode = new HuffmanNode(0, parent, c);
		const leftNode = new HuffmanNode(0, parent);

		this._dict[c] = rightNode;
		parent.right = rightNode;
		parent.left = leftNode;
		this._emptyNode = leftNode;
		
		return code;
	}
	  
	update(c: string) {
		let p: HuffmanNode | null = this._dict[c]!;
		while(p) {
			const leader = this._leaderOfWeight(p.weight);

			if(leader !== p && leader !== p.parent){
				HuffmanTree.swap(leader, p);
			}
				
			p.weight++;
			p = p.parent;
		}
	}

	close(): void {
		// eliminate empty node
		const parent = this._emptyNode.parent!;
		const parentParent = parent.parent;
		const sibling = parent.left === this._emptyNode ? parent.right! : parent.left!;

		if(parentParent){
			parentParent!.replace(parent, sibling);
			sibling.parent = parentParent;
		}
	}
	
	_leaderOfWeight(w: number): HuffmanNode {
		const list = [this._root];
	
		for(const node of list){
			if(node.weight === w) return node;
			if(!node.isLeaf) list.push(node.right!, node.left!);
		}
	
		throw new Error('Never should reach here');
	}

	static swap(a: HuffmanNode, b: HuffmanNode): void {
		const temp = b.parent!.right;

		a.parent!.replace(a, b);
		
		if(temp === b){
			b.parent!.right = a;
		}else{
			b.parent!.left = a;
		}

		[a.parent, b.parent] = [b.parent, a.parent];
	}

	print(): void {
		require('print-tree')(
			this._root,
			(node: HuffmanNode) => {
				if(node === this._emptyNode) return 'EMPTY';
				if(node.isLeaf) return `${node.symbol}: ${node.code} (${node.weight})`;

				return node.weight.toString();
			},
			(node: HuffmanNode) => node.isLeaf ? [] : [node.left!, node.right!],
		);
	}
}

const ASCII_ENCODE = (c: string) => c.charCodeAt(0).toString(2).padStart(8, '0');
const ASCII_DECODE = (c: string) => String.fromCharCode(parseInt(c, 2));
const ALL_ASCII: string[] = Array.from({length: 256}, (_, i) => String.fromCharCode(i));

class AdaptiveHuffmanEncoder {
	constructor(
		public defaultCode = ASCII_ENCODE,
		allSymbols: string[] | string = ALL_ASCII
	) {
		this._tree = new HuffmanTree();
		this.defaultCode = defaultCode || ASCII_ENCODE;
		this.allSymbols = new Set(allSymbols);
	}
	public _tree: HuffmanTree;
	private allSymbols: Set<string>;

	encode(str: string): string {
		let encoded = '';
		for(const char of str) {
			encoded += this.encodeOne(char);
		}

		this._tree.print();
		return encoded;
	}
  
	encodeOne(c: string): string {
		let code = this._tree.getCode(c);
		if(!code){
			code = this._tree.addNew(c) + this.defaultCode(c);

			this.allSymbols.delete(c);
			if(this.allSymbols.size === 0) this._tree.close();
		}

		this._tree.update(c)
		return code;
	}
}

class AdaptiveHuffmanDecoder {
	constructor(
		public defaultCode = ASCII_DECODE,
		allSymbols?: string[] | string
	) {
		this._tree = new HuffmanTree();
		this.allSymbols = new Set(allSymbols);
	}
	public _tree: HuffmanTree;
	private allSymbols: Set<string>;

	decode(str: string): string {
		let decoded = '';
		while(str.length){
			const [symbol, code] = this.decodeOne(str);
			decoded += symbol;
			str = str.slice(code.length);
		}

		return decoded;
	}

	decodeOne(str: string): [string, string] {
		
	}
}

// const testStr = require('fs').readFileSync('F:\\Programacion\\Ejercicios-Facultad\\4to año\\Teoria de la informacion\\Compresores\\dinamicas\\Huffman.ts', 'utf8');
const MY_ASCII = (c: string) => ({
	'A': '000',
	'B': '001',
	'R': '010',
	'C': '011',
	'D': '100',
}[c]!);

function test(testStr: string, A: (a: string) => string, symbols?: string) {
	const encoded = new AdaptiveHuffmanEncoder(
		A,
		symbols,
	).encode(testStr);

	const encoded2 = (function() {
		class HuffmanNode {
			constructor(weight = 0, parent) {
			  this.weight = weight
			  this.parent = parent
			  this.right = this.left = null
			}
		  
			get path() {
			  return this.parent ? this.parent.path + (this.parent.right === this ? '1' : '0') : ''
			}
		  }
		  
		  class HuffCoder {
			constructor(defaultCode) {
			  this._NYT = this._root = new HuffmanNode()
			  this._dict = {}
			  this.defaultCode = defaultCode || (c => c.charCodeAt().toString(2).padStart(8, '0'))
			}
		  
			encode(c) {
			  if (this._dict[c]) var code = this._dict[c].path
			  else {
				code = (this._NYT.path || '0') + this.defaultCode(c)
				this._dict[c] = this._NYT.right = new HuffmanNode(0, this._NYT)
				this._NYT = this._NYT.left = new HuffmanNode(0, this._NYT)
			  }
			  this._updateTree(c)
			  return code
			}
	
			encodeMany(str: string): string {
				let encoded = '';
				for(const char of str) {
					encoded += this.encode(char);
				}
		
				return encoded;
			}
		  
			_updateTree(c) {            // increase weight and swap nodes
			  for (let p = this._dict[c]; p; p.weight++, p = p.parent) {
				let leader = this._leaderOfWeight(p.weight)
				![p, p.parent, undefined].includes(leader) && HuffCoder._swap(leader, p)
			  }
			}
		  
			_leaderOfWeight(w) {
			  for (let q = [this._root], p; p = q.shift(); p.left && q.push(p.right, p.left)) {
				if (p.weight === w) return p
			  }
			}
		  
			static _swap(leader, p) {
			  const temp = p.parent.right           // prevent p and leader are siblings
			  leader.parent.right === leader ? leader.parent.right = p : leader.parent.left = p
			  temp === p ? p.parent.right = leader : p.parent.left = leader
			  leader.parent = [p.parent, p.parent = leader.parent][0]
			}
		  }
	
		return new HuffCoder(A).encodeMany(testStr);
	})()
	
	assert(encoded2 === encoded);
}

test('ABRACADABRA', MY_ASCII, 'ABRACADABRA');
test('ABRACADABRA', ASCII_ENCODE, 'ABRACADABRA');
test(
	require('fs').readFileSync('F:\\Programacion\\Ejercicios-Facultad\\4to año\\Teoria de la informacion\\Compresores\\dinamicas\\Huffman.ts', 'utf8')
	,
	ASCII_ENCODE,
);

const testStr = 'ABRACADABRA';
const encoded = new AdaptiveHuffmanEncoder(MY_ASCII, testStr).encode(testStr);
const decoded = new AdaptiveHuffmanDecoder(MY_ASCII, testStr).decode(encoded);

console.log(decoded === testStr);