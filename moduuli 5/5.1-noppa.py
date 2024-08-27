import random as rd

def main():

    noppia = int(input("Anna noppien lukumäärä: "))
    summa = 0

    # heitä kaikkia noppia yhden kerran
    for _ in range(0, noppia):
        summa += rd.randint(1, 6)
        # print(f"summa: {summa}")

    print(f"Noppien ({noppia}) summa on {summa}")

if __name__ == "__main__":
    main()