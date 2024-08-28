# palauta annetun listan summa
def summa(list: list) -> int:
    sum = 0
    for i in list:
        sum += i
    return sum


def main():
    list = [4,6,3,7]
    print(f"listan lukujen summa: {summa(list)}")


if __name__ == "__main__":
    main()