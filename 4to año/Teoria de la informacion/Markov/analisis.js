const str = 'COMOQUIERESQUETEQUIERASIQUIENQUIEROQUEMEQUIERA';
const symbols = [...new Set(str.split(''))].sort();
const counts = str.split('').reduce((acc, symbol) => {
	acc[symbol] = (acc[symbol] || 0) + 1;
 	return acc;
}, {});
const probabilities1 = Object.entries(counts).reduce((acc, [symbol, count]) => {
	acc[symbol] = count / str.length;
	return acc;
}, {});
const counts2 = {};

const round = (num, digits) => Math.round(num * Math.pow(10, digits)) / Math.pow(10, digits);

for(const symbol of symbols) {
  counts2[symbol] = {};
  for(const symbol2 of symbols) {
	counts2[symbol][symbol2] = 0;
  }
}

for (let i = 0; i < str.length - 1; i++) {
	const symbol = str[i];
	const symbol2 = str[i + 1];
	counts2[symbol][symbol2]++;
}

console.log(counts2);

const probabilities = {};
for(const symbol of symbols) {
	let count = 0;
	for(const symbol2 of symbols) {
		count += counts2[symbol][symbol2];
	}

	probabilities[symbol] = {};
	for(const symbol2 of symbols) {
		probabilities[symbol][symbol2] = round(counts2[symbol][symbol2] / count, 2);
	}

	probabilities[symbol]['total'] = count;
}

console.table(probabilities);

// calcular entropia de markov
let entropy = 0;
const maxEntropy = Math.log2(symbols.length);

for(const symbol of symbols) {
	let sum = 0;
	for(const symbol2 of symbols) {
		const p = probabilities[symbol][symbol2];
		if(p > 0) {
			sum += p * -Math.log2(p);
		}
	}

	entropy += sum * probabilities1[symbol];
}

console.log('Entropia de Markov:', entropy);
console.log('Entropia maxima:', round(maxEntropy, 2));