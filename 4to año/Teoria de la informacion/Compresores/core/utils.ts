import Fraction from './fraction';

export function count(str: string, substring: string): number {
	let count = 0;
	for(let i = 0; i < str.length; i++) {
		if(str.slice(i, i + substring.length) === substring) {
			count++;
		}
	}

	return count;
}

export function substringCounts(str: string, length = 1): Record<string, number> {
	const counts: Record<string, number> = {};
	for(let i = 0; i < str.length; i++) {
		const substring = str.slice(i, i + length);
		counts[substring] = (counts[substring] || 0) + 1;
	}

	return counts;
}

type Key = string | number;

export function copySorted<T extends string | number | Fraction>(
	object: Record<string, T>,
	byValue = false
): Record<string, T> {
	return Object.keys(object)
		.sort((a, b) => {
			if(byValue) {
				if(typeof object[a] === 'string'){
					return object[a].localeCompare(object[b] as string);
				}else if(object[a] instanceof Fraction) {
					return object[a].subtract(object[b] as Fraction).valueOf();
				}else if (typeof object[a] === 'number') {
					return object[a] - (object[b] as number);
				}else throw new Error('Invalid type');
			}

			return a.localeCompare(b);
		})
		.reduce((acc, key) => {
			acc[key] = object[key]!;
			return acc;
		}, {} as Record<string, T>);
}

export function mapObject<K extends Key, V, R>(
	object: Record<K, V>,
	callback: (value: V, key: K) => R
): Record<K, R> {
	const newObj: Record<K, R> = {} as Record<K, R>;

	for(const key in object) {
		newObj[key] = callback(object[key], key);
	}

	return newObj;
}
