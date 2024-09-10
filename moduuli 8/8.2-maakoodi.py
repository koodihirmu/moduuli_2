import mysql.connector as mysql

# avataan yhteys tietokantaan
connection = mysql.connect(
    host='127.0.0.1',
    port= 3306,
    database= 'flight_game',
    user= 'tomi',
    password= 'mariadb',
    autocommit= True
)

def get_airport_count_by_iso(iso_country):
    # haku joka palauttaa tyypin ja määrän jokaiselle tyypille
    sql = f'''select type, count(*)
            from airport 
            where iso_country = \"{iso_country}\"
            group by type
            '''
    # suorita haku
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

        # printtaa tarvittava tieto
        if len(airport_data) > 0:
            print("Maakoodilla löytyy: ")
            for data in airport_data:
                print(f"{data['type']} - {data['count(*)']}")


if __name__ == "__main__":
    main()