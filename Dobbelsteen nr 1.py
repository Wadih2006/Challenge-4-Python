print("Hoeveel dobbelstenen wil je gooien?")
print("1", "2", "3", "4", "5", "6")

    # take input from the user
choice = input("Keuze")

    # check if choice is one of the four options
if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Typ hier uw keuze: "))

        if choice == '1':
            import random
            print(random.randint(1,6))

        if choice == '2':
            import random
            print(random.randint(1,6))
            print(random.randint(1,6))

        if choice == '3':
            import random
            print(random.randint(1,6))
            print(random.randint(1,6))
            print(random.randint(1,6))

        if choice == '4':
            import random
            print(random.randint(1,6))
            print(random.randint(1,6))
            print(random.randint(1,6))
            print(random.randint(1,6))

        if choice == '5':
            import random
            print(random.randint(1,6))
            print(random.randint(1,6))
            print(random.randint(1,6))
            print(random.randint(1,6))
            print(random.randint(1,6))

        if choice == '6':
            import random
            print(random.randint(1,6))
            print(random.randint(1,6))
            print(random.randint(1,6))
            print(random.randint(1,6))
            print(random.randint(1,6))
            print(random.randint(1,6))