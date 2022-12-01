jaar = int(input("Voer uw geboortejaar in "))
maand = int(input("Voer uw geboortemaand in "))
dag = int(input("Voer uw geboortedag in "))

verjaardag = jaar, maand, dag

print(f"Uw geboortedatum is {verjaardag}")

while True:
    import datetime

    now = datetime.datetime.now()
    print("Current date and time is:")
    print(now.strftime("%y-%m-%d %H:%M:"))

    if now > 18 :
        print("Je mag motorrijden")
    else: print("Je mag nier rijden")