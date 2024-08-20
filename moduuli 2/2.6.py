import random as rd

def generoi_koodi(alku, loppu, määrä):
    koodi = []
    for i in range(0, määrä):
        koodi.append(rd.randint(alku, loppu))
    return koodi

def tulosta(list):
    for i in list:
        print(f"{i} ", end="")
    print()
        

def main():
    #print(f"{}")
    #print(f"{generoi_koodi(1, 6, 4)}")
    tulosta(generoi_koodi(0, 9, 3))
    tulosta(generoi_koodi(1, 6, 4))

if __name__ == "__main__":
    main()