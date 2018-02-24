aasta = int(input("Sisesta aastaarv: "))
if ((aasta % 4) == 0):
    if ((aasta % 100) == 0):
        if((aasta % 400) == 0):
            print("Sisestatud aasta on liigaasta")
        else:
            print("Sisestatud aasta ei ole liigaasta")
    else:
        print("Sisestatud aasta on liigaasta")
else:
    print("Sisestatud aasta ei ole liigaasta")

