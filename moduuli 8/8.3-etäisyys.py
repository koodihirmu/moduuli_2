import mysql.connector as mysql
from geopy import distance

# avataan yhteys tietokantaan
connection = mysql.connect(
    host='127.0.0.1',
    port= 3306,
    database= 'flight_game',
    user= 'tomi',
    password= 'mariadb',
    autocommit= True
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
        airport = cursor.fetchall()
        if len(airport) > 0:
            return (airport[0]["latitude_deg"], airport[0]["longitude_deg"])

def main():
    running = True

    airport_1 = get_airport()
    airport_2 = get_airport()
    format = distance.distance(airport_1, airport_2)
    print(f"{format}")


if __name__ == "__main__":
    main()

