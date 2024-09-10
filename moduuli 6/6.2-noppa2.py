import random as rd


def noppa(koko) -> int:
    return rd.randint(1, koko)


def main():

    nopan_koko = 21
    nopan_luku = 0

    while nopan_luku != nopan_koko:
        nopan_luku = noppa(nopan_koko)
        print(f"Heitetään noppaa: {nopan_luku}")


if __name__ == "__main__":
    main()
