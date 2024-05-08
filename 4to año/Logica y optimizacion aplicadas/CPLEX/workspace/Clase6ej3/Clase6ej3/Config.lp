\ENCODING=ISO-8859-1
\Problem name: Config

Maximize
 obj1: 15 cantBebidas("1") + 15 cantBebidas("2") + 15 cantBebidas("3")
Subject To
 C1: cantBebidas("1") + cantBebidas("2") + cantBebidas("3") <= 400
 c2: 6 cantBebidas("1") + 3 cantBebidas("2") + 3 cantBebidas("3") <= 1500
 c3: 3 cantBebidas("1") + 3 cantBebidas("2") + 4 cantBebidas("3") <= 2000
End
