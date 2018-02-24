# kasutaja sisend tunnid.minutid
aeg = float(input("Sisesta aeg kujul tund.minut: "))
# arvutame aja väärtusest tunnis
# selleks teisendama aeg muutuja tüüp täisarvuks
tunnid = int(aeg)
# minutid arvutame: 5.45 - 5 -> 0.45 * 100 -> 45.0 -> 45
minutid = int((aeg - tunnid) * 100)
# kontrollime, et tunde ei ole rohkem kui 23
if(tunnid > 23 or minutid > 59):
    print("Tunde ei saa olla rohkem kui 23")
# kontrollime, et minuteid ei ole rohkem kui 59
    print("Minuteid ei saa olla rohkem kui 59")
elif(tunnid > 23 and minutid < 60):
    print("Tunde ei saa olla rohkem kui 23")
elif(tunnid < 24 and minutid > 59):
    print("Minuteid ei saa olla rohkem kui 59")
else:
    # väljastame
    print("aeg\ntunnid: " + str(tunnid) + " minutid: " + str(minutid))
