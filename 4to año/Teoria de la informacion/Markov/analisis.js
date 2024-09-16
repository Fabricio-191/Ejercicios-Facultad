const str = 'COMOQUIERESQUETEQUIERASIQUIENQUIEROQUEMEQUIERA';
const symbols = [...new Set(str.split(''))].sort();
const counts = {};

const round = (num, digits) => Math.round(num * Math.pow(10, digits)) / Math.pow(10, digits);

for(const symbol of symbols) {
  counts[symbol] = {};
  for(const symbol2 of symbols) {
	counts[symbol][symbol2] = 0;
  }
}

for (let i = 0; i < str.length - 1; i++) {
	const symbol = str[i];
	const symbol2 = str[i + 1];
	counts[symbol][symbol2]++;
}

console.log(counts);


const probabilities = {};
for(const symbol of symbols) {
	let count = 0;
	for(const symbol2 of symbols) {
		count += counts[symbol][symbol2];
	}

	probabilities[symbol] = {};
	for(const symbol2 of symbols) {
		probabilities[symbol][symbol2] = round(counts[symbol][symbol2] / count, 2);
	}

	probabilities[symbol]['total'] = count;
}

console.table(probabilities);