// const longitudes = [1, 1, 2, 3, 3, 4, 5, 5, 5, 5];
// const longitudes = [1, 1, 2, 2, 3, 3, 4, 4, 4, 5];
// const longitudes = [1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3];
const longitudes = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5];

const base = 3;

// checkear inecuacion de craft

const checkCraft = (longitudes, base) => {
    let sum = longitudes.reduce((acc, curr) => acc + base ** -curr, 0);

    return sum <= 1
}

console.log(checkCraft(longitudes, base));