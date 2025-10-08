ilosc = int(input("Podaj ilość linii: "))

with open("linie.txt", "w", encoding="utf-8") as plik:
    for i in range(1, ilosc + 1):
        plik.write(f"Linia {i}\n")

