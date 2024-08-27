def main():
    print("Tämä ohjelma tarkistaa onko luku alkuluku")

    luku = int(input("Anna luku: "))
    jaettava = False

    # tarkasta kaikki luvut luvun ja 2 välillä
    # 1 ja lukua ei tarkisteta koska kaikki luvut
    # on jaettavissa niillä
    for i in range(2, luku - 1):
        if luku % i == 0:
            jaettava = True
            break

    if jaettava:
        print("Luku ei ole alkuluku!")
    else:
        print("Luku on alkuluku!")


if __name__ == "__main__":
    main()