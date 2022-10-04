		ORG 1024d

		LD A, 7d
		OUT (11d), A

		LD A, 3d; 
		OUT (9d), A

		JP INICIO
		FIN



		ORG 1748d
		PUSH AF
		PUSH BC
		PUSH DE
		PUSH HL
		PUSH IX
		PUSH IY

		IN A, (10d)
		CP 0
		JP P, UN

		LD A, 0d
		OUT (13d), A
		JP FINAL
		
UN		CP 10d
		JP P, DO

		LD A, 1d
		OUT (13d), A
		JP FINAL

DO		CP 80d
		JP P, TR

		LD A, 3d
		OUT (13d), A
		JP FINAL

TR		LD A, 7d
		OUT (13d), A

FINAL	POP IY
		POP IX
		POP HL
		POP DE
		POP BC
		POP AF
		RETI
		FIN