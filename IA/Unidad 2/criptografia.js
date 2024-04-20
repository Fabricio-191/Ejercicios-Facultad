// @ts-nocheck

// A * 3000 + G * 300 + U * 30 + A * 3 = S * 10000 + A * 1000 + L * 100 + U * 10 + D

function isSolution(A, G, U, S, L, D) {
	return (new Set([A, G, U, S, L, D])).size === 6 && (
		A * 3000 + G * 300 + U * 30 + A * 3 === S * 10000 + A * 1000 + L * 100 + U * 10 + D
	)
}

for(let A = 0; A <= 9; A++) {
	for(let G = 0; G <= 9; G++) {
		for(let U = 0; U <= 9; U++) {
			for(let S = 0; S <= 9; S++) {
				for(let L = 0; L <= 9; L++) {
					for(let D = 0; D <= 9; D++) {
						if(isSolution(A, G, U, S, L, D)) {
							console.log(`A = ${A}, G = ${G}, U = ${U}, S = ${S}, L = ${L}, D = ${D}`)
						}
					}
				}
			}
		}
	}
}