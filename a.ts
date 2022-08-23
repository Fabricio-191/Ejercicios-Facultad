class a{
	abc(a: number, b: number): number {
		return a + b;
	}
}

abstract class b{
	abstract abc(a: number, b: number): number;
	def(a: number, b: number): number {
		return a + b;
	}
}

interface c {
	abc(a: number, b: number): number;
	def(a: number, b: number): number;
}