# kuukaudet: dict = {"kevät": [1, 2, 3], "kesä": [
#     4, 5, 6], "syksy": [7, 8, 9], "talvi": [10, 11, 12]}

kuukaudet = ("kevät", [1, 2, 3], "kesä", [
    4, 5, 6], "syksy", [7, 8, 9], "talvi", [10, 11, 12])


def main():
    user_input = int(input("Anna kuukauden numero: "))

    for i in range(1, len(kuukaudet), 2):
        if user_input in kuukaudet[i]:
            print(kuukaudet[i-1])


if __name__ == "__main__":
    main()
