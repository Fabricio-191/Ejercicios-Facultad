const solution = [5, 1, 4, 3, 2];

const duraciones = [3, 4, 1, 4, 5];
const penalizacion = [700, 800, 100, 300, 200];

const costosActualizacion = [
	[1100    , 600     , 1200    , 2000    , 1400    , Infinity],
	[Infinity, 1300    , 700     , 1200    , 1100    , 1000    ],
	[900     , Infinity, 800     , 1400    , 1300    , 1100    ],
	[900     , 1000    , Infinity, 2000    , 700     , 1500    ],
	[1000    , 700     , 800     , Infinity, 600     , 1200    ],
	[1400    , 1300    , 1200    , 1300    , Infinity, 900     ]
]

let dias = 0;
let costoTotal = 0;

costoTotal += costosActualizacion[0][solution[0] - 1];

for(let i = 0; i < solution.length; i++){
	costoTotal += penalizacion[solution[i] - 1] * dias;
	costoTotal += costosActualizacion[solution[i] - 1][solution[i + 1] - 1];

	dias += duraciones[solution[i] - 1];
}

costoTotal += costosActualizacion[solution[4] - 1][5];

console.log(costoTotal);