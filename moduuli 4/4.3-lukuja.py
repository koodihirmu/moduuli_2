def main():

    numerot = []
    
    while True:
        u_input = input("Anna luku tai tyhjä lopettaaksesi ohjelman: ")
        if u_input == "": 
            break
        # lisää numero listaan
        numerot.append(int(u_input))
    
    if numerot:
        numerot.sort()
        print(numerot[:-1])

if __name__ == "__main__":
    main()