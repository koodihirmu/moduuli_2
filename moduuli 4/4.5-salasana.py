def main():

    kayttajatunnus = "python"
    salasana = "rules"
    yrityksia = 5

    while True:
        u_user = input("Anna käyttäjätunnus: ")
        u_pass = input("Anna salasana: ")

        yrityksia -= 1
        if yrityksia == 0:
            print("Pääsy evätty")
            break

        if u_pass == salasana and u_user == kayttajatunnus:
            print("Tervetuloa")
            break


if __name__ == "__main__":
    main()
