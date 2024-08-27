def main():

    kaupungit = []

    # kysy kaikki kaupungit, _ variablena koska
    # haluan ilmaista että sitä ei tarvita
    for _ in range(0, 5):
        kaupungit.append(input("Anna kaupunki: "))
    
    for i in kaupungit:
        print(i)

if __name__ == "__main__":
    main()