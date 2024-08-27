def main():
    print("Anna lukuja ja ohjelma tulostaa 5 suurinta \
          \nTyhjä tulostaa numerot")

    numerot = []

    while True:
        syöte = input("Anna lukuja: ")
        if syöte == "":
            break
        numerot.append(int(syöte))
    
    # järjestä lista suurimmasta pieninpään
    numerot.sort(reverse=True)

    # tulosta viisi isointa numeroa slice funktiolla
    print(numerot[slice(5)])

if __name__ == "__main__":
    main()