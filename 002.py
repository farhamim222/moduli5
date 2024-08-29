import random
def heita_noppaa(tahkojen_maara):

    return random.randint(1, tahkojen_maara)


def paaojelma():

    tahkojen_maara = int(input("Anna nopan tahkojen määrä: "))

    while True:
        silmaluku = heita_noppaa(tahkojen_maara)
        print(f"Heitit: {silmaluku}")
        if silmaluku == tahkojen_maara:
            break

paaojelma()
