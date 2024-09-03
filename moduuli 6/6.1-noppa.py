import random as rd


def noppa() -> int:
    return rd.randint(1, 6)


def main():

    nopan_luku = 0

    while nopan_luku != 6:
        nopan_luku = noppa()
        print(f"Heitetään noppaa: {nopan_luku}")


if __name__ == "__main__":
    main()
