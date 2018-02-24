
# Koosta programm, mis programmi käivitamisel tervitab
# kasutajat nii tavakeeles kui morse koodina, lubab
# seejärel kasutajal sisestada sõnu ning teisendab need
# sümbolhaaval morsetähestikku (lisades iga sümboli järele
# tühiku). Sõnastik ei pruugi sisaldada kõikvõimalikke
# märke, seega tuleb iga sümboli puhul kontrollida, kas
# see üldse esineb sõnastikus. kontrollimiseks kasutame
# ainult väikesed tähed. Samuti õ. ä. ü ja ö asemel kasutame o, a ja u.



tahestik = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..",
            "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.",
            "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--..", " ":".......",
            "ä":".-", "õ":"---", "ö":"---", "ü":"..-"}
tervitus = "Tervist"
print("Tervist")
for taht in tervitus:
    for voti in tahestik:
        if (taht.lower() == voti):
            print(tahestik[voti])

sona = input("Sisesta sõna või lause: ")

for taht in sona:
    for voti in tahestik:
        if (taht.lower() == voti):
            print(tahestik[voti])
#        else:
#            print("Sellist sümbolit ei esine morsetähestikus")