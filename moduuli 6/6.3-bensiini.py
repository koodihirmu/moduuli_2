def gallonat_bensaksi(gallonaa) -> float:
    return gallonaa * 3.785


def main():

    while True:
        gallonat = 0

        try:
            gallonat = float(input("Anna gallonat: "))
            if gallonat < 0:
                break
            print(f"Bensiinin määrä litroina: {gallonat_bensaksi(gallonat)}")
        except:
            print("Error: Anna luku")


if __name__ == "__main__":
    main()