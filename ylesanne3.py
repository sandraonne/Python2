punktid = float(input("Sisesta punktisumma: "))
if (punktid >= 90): hinne = "A"
elif (punktid >= 80): hinne = "B"
elif (punktid >= 70): hinne = "C"
elif (punktid >= 60): hinne = "D"
else: hinne = "F"

print("Punktid:", str(punktid), "Hinne:", hinne)
