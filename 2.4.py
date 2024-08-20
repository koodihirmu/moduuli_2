# laske summa annetuista luvuista
def summa(lista):
    sum = 0
    for i in lista:
        sum += i
    return sum

# laske tulo annetuista luvuista
def tulo(lista):
    sum = 0
    for i in lista:
        if sum == 0:
            sum = i
            continue
        sum *= i
    return sum

# laske keskiarvot
def keskiarvo(lista):
    return sum(lista) / len(lista)

def main():
    kokonaisluvut = []
    # lue kolme kokonaislukua
    for i in range(0,3):
        kokonaisluvut.append(int(input("Anna kokonaisluku: ")))

    print(f"Summa: {summa(kokonaisluvut)}")
    print(f"Tulo: {tulo(kokonaisluvut)}")
    print(f"Keskiarvo: {keskiarvo(kokonaisluvut)}")
    
if __name__ == "__main__":
    main()