kuu = int(input("Sisesta kuu numbrilisel kujul: "))
if (kuu > 2 and kuu < 6):
    teade = "kevadkuu"
elif(kuu > 5 and kuu < 9):
    teade = "suvekuu"
elif(kuu > 8 and kuu < 12):
    teade = "sügiskuu"
elif(kuu == 12 or kuu == 1 or kuu == 2):
    teade = "talvekuu"
if(kuu > 0 and kuu < 13):
    print("Antud kuu on " + teade)
else:
    print("Meie aastas ei ole niisuguse numbriga kuud")