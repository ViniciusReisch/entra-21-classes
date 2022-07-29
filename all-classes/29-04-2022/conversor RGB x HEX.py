rgb1 = int(input("Escreva o codigo R: "))
rgb2 = float(input("Escreva o codigo G: "))
rgb3 = float(input("Escreva o codigo B: "))

resto1 = rgb1%16
rgb1 = rgb1 - resto1
rgb1 = rgb1/16
rgb1 = int(rgb1)
resto1 = int(resto1)
print(resto1, rgb1)

resto2 = rgb2%16
rgb2 = rgb2 - resto2
rgb2 = rgb2/16
rgb2 = int(rgb2)
resto2 = int(resto2)
print(resto2, rgb2)

resto3 = rgb3%16
rgb3 = rgb3 - resto3
rgb3 = rgb3/16
rgb3 = int(rgb3)
resto3 = int(resto3)
print(resto3, rgb3)

if rgb1 == 10:
    rgb1 = "A"
elif rgb1 == 11:
    rgb1 = "B"
elif rgb1 == 12:
    rgb1 = "C"
elif rgb1 == 13:
    rgb1 = "D"
elif rgb1 == 14:
    rgb1 = "E"
elif rgb1 == 15:
    rgb1 = "F"

if resto1 == 10:
    resto1 = "A"
elif resto1 == 11:
    resto1 = "B"
elif resto1 == 12:
    resto1 = "C"
elif resto1 == 13:
    resto1 = "D"
elif resto1 == 14:
    resto1 = "E"
elif resto1 == 15:
    resto1 = "F"


if rgb2 == 10:
    rgb2 = "A"
elif rgb2 == 11:
    rgb2 = "B"
elif rgb2 == 12:
    rgb2 = "C"
elif rgb2 == 13:
    rgb2 = "D"
elif rgb2 == 14:
    rgb2 = "E"
elif rgb2 == 15:
    rgb2 = "F"

if resto2 == 10:
    resto2 = "A"
elif resto2 == 11:
    resto2 = "B"
elif resto2 == 12:
    resto2 = "C"
elif resto2 == 13:
    resto2 = "D"
elif resto2 == 14:
    resto2 = "E"
elif resto2 == 15:
    resto2 = "F"

if rgb3 == 10:
    rgb3 = "A"
elif rgb3 == 11:
    rgb3 = "B"
elif rgb3 == 12:
    rgb3 = "C"
elif rgb3 == 13:
    rgb3 = "D"
elif rgb3 == 14:
    rgb3 = "E"
elif rgb3 == 15:
    rgb3 = "F"

if resto3 == 10:
    resto3 = "A"
elif resto3 == 11:
    resto3 = "B"
elif resto3 == 12:
    resto3 = "C"
elif resto3 == 13:
    resto3 = "D"
elif resto3 == 14:
    resto3 = "E"
elif resto3 == 15:
    resto3 = "F"

print(f"{rgb1}{resto1}{rgb2}{resto2}{rgb3}{resto3}")


