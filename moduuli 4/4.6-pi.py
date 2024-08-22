import random as rd


def main():
    pisteita = int(input("Anna pisteiden määrä: "))
    pisteita_ympyrassa = 0

    for i in range(1, pisteita):
        x = rd.uniform(-1, 1)
        y = rd.uniform(-1, 1)
        if (x**2+y**2 < 1):
            pisteita_ympyrassa += 1
        print(f"Piin likiarvo: {4*pisteita_ympyrassa/i}")


if __name__ == "__main__":
    main()
