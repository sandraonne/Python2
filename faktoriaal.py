
arv = int(input("Sisesta täisarv: "))
fakt = 1
# kontrollin, kas arv on negatiivne, positiivne või null
if arv < 0:
    print("Negatiivsete arvude jaoks ei ole faktoriaal defineeritud")
elif arv == 0:
    print("0! = 1")
else:
    for i in range(1, arv + 1):
        fakt = fakt * i
    print(str(arv) + '! = ' +str(fakt))
    print('-----------')