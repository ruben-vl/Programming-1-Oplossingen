# https://dodona.ugent.be/nl/courses/1286/series/14348/activities/879249671

getal = int(input())

som = 0
veelvoud = getal

while veelvoud <= 100:
    som += veelvoud
    veelvoud += getal

print(som)
