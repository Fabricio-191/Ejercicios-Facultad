const fs = require('fs');

const csvContent = fs.readFileSync('D:/Programacion/Ejercicios-Facultad/4to año/IA/Practico/Ejercicio 4/PYGAD.csv', 'utf8');

const csvLines = csvContent.split('\r\n');

const data = csvLines.map(line => line.split(',').slice(2));

// num_parents_mating, crossover_probability, mutation_probability, mutation_type, crossover_type

const frecuencies = data.reduce((acc, [num_parents_mating, crossover_probability, mutation_probability, mutation_type, crossover_type]) => {
	acc.num_parents_mating[num_parents_mating] = (acc.num_parents_mating[num_parents_mating] || 0) + 1;
	acc.crossover_probability[crossover_probability] = (acc.crossover_probability[crossover_probability] || 0) + 1;
	acc.mutation_probability[mutation_probability] = (acc.mutation_probability[mutation_probability] || 0) + 1;
	acc.mutation_type[mutation_type] = (acc.mutation_type[mutation_type] || 0) + 1;
	acc.crossover_type[crossover_type] = (acc.crossover_type[crossover_type] || 0) + 1;
	return acc;
}, {
	num_parents_mating: {},
	crossover_probability: {},
	mutation_probability: {},
	mutation_type: {},
	crossover_type: {}
});

console.log(data)
console.log(frecuencies);