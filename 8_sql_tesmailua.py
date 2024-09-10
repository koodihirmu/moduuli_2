import mysql.connector as mysql

yhteys = mysql.connect(
    host='127.0.0.1',
    port= 3306,
    database= 'flight_game',
    user= 'tomi',
    password= 'mariadb',
    autocommit= True
)

def get_airport_by_icao(icao):
    sql = f"SELECT ident, municipality, airport.name FROM airport \
        WHERE ident = \"{icao}\""

    with yhteys.cursor() as cursor:
        cursor.execute(sql)
        airport_data = cursor.fetchall()
        return airport_data

        # for row in rows:
        #     print(row)
        #     (id, municipality, data) = row
        #     print(f"{id} - {municipality} - {data}")

def get_airport_by_municipality(municipality):
    sql = f"SELECT ident, municipality, airport.name FROM airport \
        WHERE municipality = \"{municipality}\""

    with yhteys.cursor(dictionary=True) as cursor:
        cursor.execute(sql)
        airport_data = cursor.fetchall()
        return airport_data

def main():
    # while True:
    #     u_input = input("Lentokentän ICAO: ")
    #     if u_input == "":
    #         print("Closing program")
    #         break
    #     u_input = u_input.upper()
    #     get_airport_by_icao(u_input)

    airport_data = get_airport_by_municipality("helsinki")
    for airport in airport_data:
        print(f"{airport['name']} {airport['ident']}")


if __name__ == "__main__":
    main()
    yhteys.close()