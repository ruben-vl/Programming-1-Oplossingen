# https://dodona.ugent.be/nl/courses/1286/series/14349/activities/1180320113

def tafel_van_vermenigvuldiging(getal):
    for i in range(1, 11):
        print(str(i), "*", str(getal), "=", str(i*getal))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

