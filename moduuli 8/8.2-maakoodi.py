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

airport_types = {"large_airport": 0, "medium_airport": 0, "small_airport": 0,  "heliport": 0, "seaplane_base": 0,"balloonport": 0,"closed": 0,}

def get_airport_count_by_iso(iso_country):
    sql = f"select type from airport where iso_country = \"{iso_country}\""
    with connection.cursor(dictionary=True) as cursor:
        cursor.execute(sql)
        return cursor.fetchall()

def main():
    running = True
    while running:
        u_input = input("Anna maakoodi: ")
        if u_input == "":
            break
        airport_data = get_airport_count_by_iso(u_input)
        if len(airport_data) > 0:
            for airport in airport_data:
                airport_types[airport["type"]] += 1
                # print(airport)
            
            print("Maakoodilla löytyy: ")
            for key in airport_types.keys():
                print(f"{key} - {airport_types[key]}")


if __name__ == "__main__":
    main()