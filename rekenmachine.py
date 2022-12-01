def optellen(x, y):
    return x + y

def minus(x, y):
    return x - y

def keer(x, y):
    return x * y

def delen(x, y):
    return x / y

print("Kies uw keuze.")
print("1.Optellen")
print("2.Aftrekken")
print("3.Vermenigvuldigen")
print("4.Delen")

while True:
    choice = input("Kies uw keuze(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Typ uw eerste nummer: "))
        num2 = float(input("Typ uw tweede nummer: "))

        if choice == '1':
            print(num1, "+", num2, "=", optellen(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", minus(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", keer(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", delen(num1, num2))
        
        next_calculation = input("Volgende rekensom? (ja/nee): ")
        if next_calculation == "nee":
          break
    else:
        print("Ongeldige invoer")