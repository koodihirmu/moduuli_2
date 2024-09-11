import mysql.connector as mysql
from geopy import distance

# avataan yhteys tietokantaan
connection = mysql.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='tomi',
    password='mariadb',
    autocommit=True
)


def get_airport():
    airport_icao = input("Anna lentokentän tunnus: ")
    return get_coordinates_by_icao(airport_icao)


def get_coordinates_by_icao(icao):
    sql = f'''
        select latitude_deg , longitude_deg
        from airport
        where ident = "{icao}"
    '''
    with connection.cursor(dictionary=True) as cursor:
        cursor.execute(sql)
        # airport = cursor.fetchall()
        airport = cursor.fetchone()
        if airport:
            return (airport["latitude_deg"], airport["longitude_deg"])
        else:
            print("Vastaavaa lentokenttää ei löytynyt")
            return None


def main():
    print('''Syötä lentokenttien tunnukset 
        \nniin ohjelma mittaa niiden välimatkan
        \nSyötä tyhjä lopettaaksesi ohjelman
          ''')
    while True:
        airport_1 = get_airport()
        if airport_1 is None:
            break
        airport_2 = get_airport()

        format = distance.distance(airport_1, airport_2)
        print(f"Lentokenttien etäisyys on: {format.km:.0f} km")


if __name__ == "__main__":
    main()
