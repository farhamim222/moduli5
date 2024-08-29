import random

def heita_noppaa():

    return random.randint(1, 6)

def paaojelma():
    while True:
        silmaluku = heita_noppaa()
        print(f"Heitit: {silmaluku}")
        if silmaluku == 6:
            break

paaojelma()
