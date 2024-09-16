const str = 'COMOQUIERESQUETEQUIERASIQUIENQUIEROQUEMEQUIERA';
const symbols = [...new Set(str.split(''))].sort();
console.log(symbols)
const symbolsCount = symbols.length;
const tabla = {
	A: { S: '0' },
	C: { O: '0' },
	E: { M: '0000', N: '0001', Q: '001', R: '01', S: '1000', T: '1001' },
	I: { E: '1', Q: '000' },
	M: { E: '0', O: '1' },
	N: { Q: '0' },
	O: { M: '10', Q: '0' },
	Q: { U: '0' },
	R: { A: '0', E: '10', O: '11' },
	S: { I: '0', Q: '1' },
	T: { E: '0' },
	U: { E: '00', I: '1' },
};

let result = [
	symbols.indexOf(str[0]).toString(2).padStart(Math.log2(symbolsCount) + 1, '0'),
];
for(let i = 0; i < str.length - 1; i++) {
	const a = str[i];
	const b = str[i + 1];

	if(tabla[a][b] === undefined){
		console.log('No se puede continuar', a, b);
		break;
	}
	
	result.push(tabla[a][b]);
}

console.log(result.join(' '));
