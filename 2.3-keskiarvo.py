import math

def main():
    kanta = int(input("Anna suorakulmion kanta: "))
    korkeus = int(input("Anna suorakulmion korkeus: "))
    
    # laske suorakulmion pinta-ala
    tulos = kanta * korkeus
    print(f"Suorakulmion pinta-ala: {tulos}")

    # laske suorakulmion piiri
    tulos = kanta*2 + korkeus*2
    print(f"Suorakulmion piiri: {tulos}")

if __name__ == "__main__":
    main()