def main():

    numerot = []

    print("Anna lukuja, tyhjä lopettaa ohjelman")

    while True:
        nums = input("Anna luku: ")
        if nums == "":
            break
        # lisää numero listaan
        numerot.append(int(nums))

    if numerot:
        numerot.sort()
        print(f"Pienin numero: {numerot[0]}")
        print(f"Suurin numero: {numerot[-1]}")


if __name__ == "__main__":
    main()
