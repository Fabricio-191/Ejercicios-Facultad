
	ORG C100h
CEREO:
	LD (HL), 0d
	INC HL

	DJNZ CEREO
	RET
	END CEREO


	ORG C500h
INICIO:
	LD B, 25d
	LD HL, 1000h

	PUSH BC
	PUSH HL
	CALL CEREO
	POP HL
	POP BC

	END INICIO