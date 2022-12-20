# https://dodona.ugent.be/nl/courses/1286/series/14347/activities/774332532

cijfer = int(input())

if cijfer < 60:
    print('F')
elif 60 <= cijfer <= 69:
    print('D')
elif 70 <= cijfer <= 79:
    print('C')
elif 80 <= cijfer <= 89:
    print('B')
else:
    print('A')