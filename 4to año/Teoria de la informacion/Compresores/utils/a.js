function bwt(text) {

	const matrix = [];
  
	for (let i = 0; i < text.length; i++) {
  
	  matrix.push(text.slice(i) + text.slice(0, i));
  
	}
  
	matrix.sort();
  
	const result = [];
  
	let startIndex = 0;
  
	for (let i = 0; i < matrix.length; i++) {
  
	  result.push(matrix[i][matrix[i].length - 1]);
  
	  if (matrix[i].startsWith(text[0])) {
  
		startIndex = i;
  
	  }
  
	}
  
	return { transformed: result.join(''), startIndex };
  
  }
  
  function ibwt({ transformed, startIndex }) {

	const matrix = [];
  
	for (let i = 0; i < transformed.length; i++) {
  
	  matrix.push(transformed[i] + transformed.slice(0, i));
  
	}
  
	matrix.sort();
  
	let original = '';
  
	for (let i = 0; i < matrix.length; i++) {
  
	  if (i === startIndex) {
  
		original = matrix[i];
  
		break;
  
	  }
  
	}
  
	const firstChar = original[0];
  
	let result = '';
  
	for (let i = 0; i < original.length; i++) {
  
	  result = original[i] + result;
  
	  if (original[i] === firstChar) {
  
		break;
  
	  }
  
	}
  
	return result;
  
  }

console.log(bwt('banana'));

console.log(ibwt(bwt('banana')));