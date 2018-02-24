#sona = 'See on väga lihtne sõna'
#for taht in sona:
#    print(taht)

sona = 'appi'
morse = {'a':'.-',
         'p':'--',
         'i':'-.'
         }
for taht in sona:
    for voti in morse: # siit alates võiks olla funktsioon
        if (taht == voti):
            print(morse[voti])