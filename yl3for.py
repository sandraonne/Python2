# Koosta programm, mis arvutab arvude 1 kuni 10 summat ja trükib summa ekraanile, kasutada tuleb for tsyklit


summa = 0
for arv in range(1, 11, 1):     # 1-st 11-ni, ühe võrra
    summa = summa + arv     # koondatud variant: summa += arv
    print('arv = ' +str(arv))
    print('hetkel summa = ' + str(summa))
    print('-----------')

# Kirjuta programm nii ümber, et lahendus oleks koostatud while tsükliga

summa = 0
arv = 1
while (arv < 11):
    summa = summa + arv     # koondatud variant: summa += arv
    print('arv = ' +str(arv))
    print('hetkel summa = ' + str(summa))
    print('-----------')
    arv += 1