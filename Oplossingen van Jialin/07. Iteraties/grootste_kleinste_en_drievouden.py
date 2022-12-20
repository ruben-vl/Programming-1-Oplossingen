# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/2109616883

grootste_getal = 0
aantal_drievouden = 0
nieuw_getal = int(input())
kleinste_getal = nieuw_getal
grootste_getal = nieuw_getal
if nieuw_getal % 3 == 0:
    aantal_drievouden += 1

for i in range(9):
    nieuw_getal = int(input())
    if nieuw_getal % 3 == 0:
        aantal_drievouden += 1
    if nieuw_getal <= kleinste_getal:
        kleinste_getal = nieuw_getal
    if nieuw_getal >= grootste_getal:
        grootste_getal = nieuw_getal


print("grootste:", grootste_getal)
print("kleinste:", kleinste_getal)
print("drievouden:", aantal_drievouden)
