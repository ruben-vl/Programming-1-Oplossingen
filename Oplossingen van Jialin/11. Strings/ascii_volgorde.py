# https://dodona.ugent.be/nl/courses/1286/series/14351/activities/335876740

woord = input()
uitvoer = ''

while len(woord) != 0:
    kleinste = 'z'
    for char in woord:
        if char < kleinste:
            kleinste = char
    uitvoer += kleinste
    woord = woord.replace(kleinste, '', 1)

print(uitvoer)

