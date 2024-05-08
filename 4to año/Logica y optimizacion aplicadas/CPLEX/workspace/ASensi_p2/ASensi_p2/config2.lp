\ENCODING=ISO-8859-1
\Problem name: config2

Maximize
 obj1: 60 cantRamos("Bodas") + 40 cantRamos("Cumpleanio")
       + 60 cantRamos("Aniversario")
Subject To
 c1: 4 cantRamos("Bodas") + cantRamos("Aniversario") <= 120
 c2: 3 cantRamos("Cumpleanio") <= 100
 c3: 3 cantRamos("Aniversario") <= 80
 c4: 2 cantRamos("Bodas") <= 60
 c5: 2 cantRamos("Cumpleanio") <= 90
 c6: 2 cantRamos("Cumpleanio") <= 70
 c7: 2 cantRamos("Aniversario") <= 110
 c8: 3 cantRamos("Bodas") <= 50
 C2: 1.5 cantRamos("Bodas") + cantRamos("Cumpleanio")
     + 1.2 cantRamos("Aniversario") <= 180
End
