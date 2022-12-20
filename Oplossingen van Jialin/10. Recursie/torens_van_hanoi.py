# https://dodona.ugent.be/nl/courses/1286/series/14350/activities/1092659960

def hanoi(n, start, tijdelijk, einde):
    if n == 2:
        print(f"Schijf {n-1} van {start} naar {tijdelijk}")
        print(f"Schijf {n} van {start} naar {einde}")
        print(f"Schijf {n-1} van {tijdelijk} naar {einde}")
        return

    hanoi(n-1, start, tijdelijk, einde)
    print(f"Schijf {n-1} van {tijdelijk} naar {einde}")
    hanoi(n-1, tijdelijk, einde, start)

hanoi(4, "A", "B", "C")
        
