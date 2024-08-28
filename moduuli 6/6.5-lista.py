def karsi_parittomat(list: list) -> list:
    list_temp = []
    for i in list:
        if i % 2 != 0:
            list_temp.append(i)
    return list_temp


def main():
    list = [2,6,3,3,6,45,9,6]


if __name__ == "__main__":
    main()