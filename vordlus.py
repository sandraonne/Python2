# Ülesanne:
# Lase kasutajal sisestada 2 arvu. Programm peab võrdlema need arvud
# 1) võrdluse tulemus salvestatakse järgmisels
# 0 kui arvud on võrdsed
# 1 kui esimene arv on suurem kui teine
# -1 kui esimene arv on väiksem kui teine
# 2) võrdluse tulemuse järgi toimub väljastamine
# kas arvud on võrdsed
# või
# esimene on suurem kui teine
# või
# esimene on väiksem kui teine

arv1 = int(input("arv 1 = "))
arv2 = int(input("arv 2 = "))
# võrdlemine
if(arv1 == arv2): tulemus = 0
elif(arv1 > arv2): tulemus = 1
else: tulemus = -1
# väljastamine
if(tulemus == 0): print(str(arv1) + " = " + str(arv2))
if(tulemus == 1): print(str(arv1) + " > " + str(arv2))
if(tulemus ==-1): print(str(arv1) + " < " + str(arv2))

