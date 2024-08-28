def karsi_parittomat(list: list) -> list:
    list_temp = []
    for i in list:
        if i % 2 == 0:
            list_temp.append(i)
    return list_temp

def tulosta_lista(list: list) -> None:
    for i in list:
        print(f"{i} ", end="")
    print()

def main() -> None:

    list = [2,6,3,3,6,45,9,6]
    list2 = karsi_parittomat(list)

    tulosta_lista(list)
    tulosta_lista(list2)

if __name__ == "__main__":
    main()