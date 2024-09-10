import mysql.connector as mysql

# avataan yhtey tietokantaan
connection = mysql.connect(
    host='127.0.0.1',
    port= 3306,
    database= 'flight_game',
    user= 'tomi',
    password= 'mariadb',
    autocommit= True
)

def get_airport_by_icao(icao: str):
    # sql query
    sql = f"select airport.name, municipality \
        from airport where ident = \"{icao}\""

    # valitaan tietoa taulusta
    with connection.cursor(dictionary=True) as cursor:
        cursor.execute(sql)
        return cursor.fetchall()


def main():
    running = True
    while running:
        get_icao = input("Anna lentokentän tunnus: ")
        if get_icao == "":
            print("Ohjelmaa lopetetaan")
            running = False

        for airport in get_airport_by_icao(get_icao):
            print(f"Lentokentän nimi on {airport['name']} ja paikkakunta {airport['municipality']}")

if __name__ == "__main__":
    main()
    
    # suljetaan yhteys sql tietokantaan
    print("Sql yhteyttä suljetaan")
    connection.close()