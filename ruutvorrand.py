import math
a = float(input("Sisesta 1. arv: "))
b = float(input("Sisesta 2. arv: "))
c = float(input("Sisesta 3. arv: "))
if(a == 0):
    print("See ei ole ruutvõrrand")
else:
    d = math.pow(b, 2) - 4 * a * c
    if(d > 0):
        print("Võrrandil on 2 lahendit")
    elif(d == 0):
        print("Võrrandil on 1 lahend")
    else:
        # d = 0
        print("Lahendid puuduvad")
