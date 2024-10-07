
interface DataAction {
	type: 'READ' | 'WRITE' | null;
	register: Register;
}
