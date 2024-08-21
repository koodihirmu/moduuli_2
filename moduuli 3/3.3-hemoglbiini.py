
#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

def main():
    arvo = int(input("Anna hemoglobiiniarvo (g/l): "))
    sukupuoli = input("Anna sukupuoli (nainen/mies): ")

    if arvo > 117 and sukupuoli == "nainen":
        print("Hemoglobiiniarvot on normaalit")
    elif arvo < 175 and sukupuoli == "nainen":
        print("Hemoglobiiniarvot on normaalit")
    elif arvo > 134 and sukupuoli == "mies":
        print("Hemoglobiiniarvot on normaalit")
    elif arvo < 195 and sukupuoli == "mies":
        print("Hemoglobiiniarvot on normaalit")
    else:
        print("Hemoglobiiniarvot epänormaalit")

if __name__ == "__main__":
    main()