nimi = input("Sisesta oma nimi: ")
vanus = int(input(nimi + ", mis on Sinu vanus? "))
# kontrollin, kas vanus on negatiivne
if (vanus > 17 and vanus < 41):
    # teavitan kasutajat
    print(nimi + ", tere tulemast 18-40 klubisse")
else:
    print("Vabandust, oled liiga noor või vana")