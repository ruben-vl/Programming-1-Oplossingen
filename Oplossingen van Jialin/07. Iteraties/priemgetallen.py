# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/1453132170

getal = int(input())

aantal_delers = 0

for i in range(1, getal+1):
    if getal % i == 0:
        aantal_delers += 1

if aantal_delers > 2:
    print(getal, "is geen priemgetal")
else:
    print(getal, "is een priemgetal")