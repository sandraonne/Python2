kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
s6na = "august"
pakkumine = input("Arva ära, mis kuu on: ")
katse = 0

if pakkumine == s6na:
    print("Palju õnne, arvasid õigesti!")
elif pakkumine not in kuud:
    print("Sellist kuud pole olemas")
else:
    while katse < 10:
        katse = katse + 1
        print("Arvasid valesti. Sul on jäänud " + str(10 - katse) + " katset.")