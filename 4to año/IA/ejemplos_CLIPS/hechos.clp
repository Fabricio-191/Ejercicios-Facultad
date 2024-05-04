         CLIPS (V6.20 03/31/02)
CLIPS> (defacts startup (animal dog) (animal duck) (animal haddock) (animal turtle) (warn-blooded dog) (worn_blooded cat) (warn-blododed duck) lay-eggs duck) (lays-eggs turtle) (child

[EXPRNPSR3] Missing function declaration for defacts.
CLIPS> clear
clear
CLIPS> (clear)
CLIPS> (defacts startup (animal dog) (animal duck) (animal haddock) (animal turtle) (warn-blooded dog ) (warn-blooded cat ) (warn-blooded duck ) (lays-eggs duck) (lays-eggs turtle) (child-of cat kitten) (child-of turtle hatchling))(load "Z:/home/lve/Documentos/2017/IA/CLIPS/hechos.clp")

[CSTRCPSR1] Expected the beginning of a construct.
FALSE
CLIPS> (deffacts startup (animal dog) (animal duck) (animal haddock) (animal turtle) (warn-blooded dog ) (warn-blooded cat ) (warn-blooded duck ) (lays-eggs duck) (lays-eggs turtle) (child-of cat kitten) (child-of turtle hatchling))
