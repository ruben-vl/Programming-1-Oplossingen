# https://dodona.ugent.be/nl/courses/1286/series/14349/activities/1590800482

def gemeenschappelijke_karakters(woord1, woord2):
    count = 0
    temp = ''
    for char in woord1:
        if char in woord2 and char not in temp:
            count += 1
        temp += char

    return count
