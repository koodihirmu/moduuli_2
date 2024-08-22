import random as rd


def main():

    print("Yritä arvata luku 1 ja 10 väliltä.")
    luku = rd.randint(1, 10)

    while True:

        arvaus = int(input("Anna arvaus: "))

        if arvaus > luku:
            print("Liian suuri arvaus")
        if arvaus < luku:
            print("Liian pieni arvaus")
        if arvaus == luku:
            print("Oikein")
            break


if __name__ == "__main__":
    main()
