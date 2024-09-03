import random as rd


def main():
    pisteita = int(input("Anna pisteiden määrä: "))
    pisteita_ympyrassa = 0

    for _ in range(0, pisteita):
        x = rd.uniform(-1, 1)
        y = rd.uniform(-1, 1)
        if (x**2+y**2 < 1):
            pisteita_ympyrassa += 1

        # nopeammin saa tuloksen ulos jos ei printtaa välillä likiarvoa
        # print(f"Piin likiarvo: {4*pisteita_ympyrassa/i}")

    print(f"Piin likiarvo: {4*pisteita_ympyrassa/pisteita}")


if __name__ == "__main__":
    main()
