lentoasemat = {}


def main():
    running = True

    while running:
        u_input = input("Syötä uusi lentoasema/hae/lopeta U/H/L: ")
        u_input = u_input.upper()

        if u_input == "U":
            print("lisätään lentokenttää")
            lentokenttä_icao = input("Syötä lentokentän tunnus: ")
            lentokenttä_nimi = input("Syötä lentokentän nimi: ")
            lentoasemat[lentokenttä_icao.upper()] = lentokenttä_nimi
        elif u_input == "H":
            print("Haetaan lentokenttää")
            lentokenttä_icao = input("Syötä lentokentän tunnus: ")
            lentokenttä_icao = lentokenttä_icao.upper()
            try:
                print(f"Lentokentän {lentokenttä_icao} \
                  nimi {lentoasemat[lentokenttä_icao]}")
            except:
                print("Lentokenttää ei löytynyt")
        else:
            print("Lopetetaan")
            running = False



if __name__ == "__main__":
    main()
