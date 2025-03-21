		ORG 1024d
		LD HL, 1100d
		LD (1300d), H
		LD (1301d), L

		LD A, FFh
		OUT (11d), A

		LD A, 3d; 00000011
		OUT (9d), A

		LD A, 24d; 00011000
		OUT (12d), A

		JP INICIO
		FIN


		ORG 1748d
RUTIN1 	EQU 1800d
RUTIN2 	EQU 1900d
		PUSH AF
		PUSH BC
		PUSH DE
		PUSH HL
		PUSH IX
		PUSH IY

		IN A, (9d)
		BIT 7, A
		JP Z, SIG
		BIT 0, A
		CALL RUTIN1

SIG		IN A, (11d)
		BIT 6, A
		JP Z, SIG
		BIT 4, A
		CALL RUTIN2

		POP IY
		POP IX
		POP HL
		POP DE
		POP BC
		POP AF
		RETI
		FIN
	


		ORG 1800d
		LD HL, (1300d)

FIN1L 	IN A, (10d)
		LD (HL), A
		INC HL
		LD (HL), FFh
		LD (1300d), H
		LD (1301d), L

		POP IY
		POP IX
		POP HL
		POP DE
		POP BC
		POP AF
		RETI
		FIN



		ORG 1900d
		LD HL, 1100d

LOOP2	LD A, (HL)
		CP FFh
		JP Z, FIN2L
		OUT (13d), A
		INC HL

		PUSH HL
		CALL ESPERA
		POP HL
		JP LOOP2
		
FIN2L	LD HL, 1100d
		LD (1300d), H
		LD (1301d), L

		POP IY
		POP IX
		POP HL
		POP DE
		POP BC
		POP AF
		RETI
		FIN