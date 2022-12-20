# https://dodona.ugent.be/nl/courses/1286/series/14351/activities/2032693594

woord = input()
zin = input()
aantal = 0

while zin.count(woord) != 0:
    start = zin.find(woord)
    if zin[start+len(woord)].isalpha() or zin[start-1].isalpha():
        zin = zin.replace(woord, "", 1)
    else:
        aantal += 1
        zin = zin.replace(woord, "", 1)

print(f"Aantal keren dat het woord \"{woord}\" voorkomt: {aantal}")