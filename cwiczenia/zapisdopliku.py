slownik = {
    "Artur": 4,
    "Basia": 3,
    "Cezary": 3,
    "Daniel": 4,
    "Eliza": 3,
}

for key, value in slownik.items():
    print("Ocena dla ucznia {key} to {value}")


with open("zapisoceny.txt", "w") as plik: 
    for key, value in slownik.items():
        plik.write(f"Ocena dla ucznia {key} to jest {value}\n")




