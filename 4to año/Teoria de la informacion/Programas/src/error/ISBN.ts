const ISBN10 = {
	sumDigits(numbers: string[]): number {
		return numbers
			.map((char, i) => {
				if(char === '?') return 0;
				return Number(char) * (10 - i);
			})
			.reduce((acc, val) => acc + val, 0);
	},
	check(isbn: string): boolean {
		const nums = isbn.match(/\d/g)!;
		if(nums.length !== 10) throw new Error(`ISBN must have 10 digits`);

		const sum = ISBN10.sumDigits(nums);

		return sum % (10 + 1) === 0;
	},
	findMissingDigit(isbn: string): number {
		const nums = isbn.match(/\d|\?/g)!;
		if(nums.length !== 10) throw new Error(`ISBN must have 10 digits`);

		const sum = ISBN10.sumDigits(nums);
		
		const index = nums.indexOf('?');
		if(index === -1) throw new Error('No missing digit');

		const weight = 10 - index;

		for(let i = 0; i < 10; i++){
			if((sum + i * weight) % (10 + 1) === 0) return i;
		}

		throw new Error('Huh ?');
	}
}

const ISBN13 = {
	sumDigits(numbers: string[]): number {
		return numbers
			.map((char, i) => {
				if(char === '?') return 0;
				return Number(char) * (i % 2 === 0 ? 1 : 3);
			})
			.reduce((acc, val) => acc + val, 0);
	},
	check(isbn: string): boolean {
		const nums = isbn.match(/\d/g)!;
		if(nums.length !== 13) throw new Error(`ISBN must have 13 digits`);

		const sum = ISBN13.sumDigits(nums);

		return sum % 10 === 0;
	},
	findMissingDigit(isbn: string): number {
		const nums = isbn.match(/\d|\?/g)!;
		if(nums.length !== 13) throw new Error(`ISBN must have 13 digits`);

		const sum = ISBN13.sumDigits(nums);
		
		const index = nums.indexOf('?');
		if(index === -1) throw new Error('No missing digit');

		const weight = index % 2 === 0 ? 1 : 3;

		for(let i = 0; i < 10; i++){
			if((sum + i * weight) % 10 === 0) return i;
		}

		throw new Error('Huh ?');
	}
}

console.log(ISBN10.findMissingDigit('3-540-?3218-9')) // 3
console.log(ISBN10.check('3-540-33218-9'))
console.log(ISBN10.check('0-13165332-6'))
console.log(ISBN10.findMissingDigit('950-311192-?')) // 7
console.log(ISBN10.check('950-311192-7'))
console.log(ISBN13.check('9783540332183'))

const str = '9783540332183';
for(let i = 0; i < 13; i++){
	const corrupted = str.split('');
	corrupted[i] = '?';
	
	const missingDigit = ISBN13.findMissingDigit(corrupted.join(''));

	if(missingDigit.toString() !== str[i]) {
		throw new Error(`Error en ${str} -> ${corrupted.join('')} -> ${missingDigit}`);
	}
}

