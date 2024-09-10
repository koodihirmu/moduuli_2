def kysy_nimi() -> str:
    nimi = input("Anna nimi: ")
    return nimi


def main():
    # tee setti "nimet" jonne varastoidaan syöte
    nimet = set()

    while True:
        uusi_nimi = kysy_nimi()
        if (uusi_nimi == ""):
            break

        if nimet.add(uusi_nimi):
            print("Aiemmin syötetty nimi")
        else:
            print("Uusi nimi")
            nimet.add(uusi_nimi)

    for nimi in nimet:
        print(nimi)


if __name__ == "__main__":
    main()
