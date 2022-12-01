spelers = int(input("hoeveel spelers doen ermee? "))

inputs = []

while True:
    namen = input("naam/KLAAR ")
    if namen == "klaar":
        break
    inputs.append(namen)

print(inputs)

print("Degene die mag beginnen is... ")

import random

print(random.choice(inputs))