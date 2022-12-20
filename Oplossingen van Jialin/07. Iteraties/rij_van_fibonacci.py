# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/1952876754

getal = int(input())
vorig_getal = 0
huidig_getal = 1

print(vorig_getal)
print(huidig_getal)
while huidig_getal <= getal:
    nieuw_getal = huidig_getal + vorig_getal
    vorig_getal = huidig_getal
    huidig_getal = nieuw_getal
    print(huidig_getal)