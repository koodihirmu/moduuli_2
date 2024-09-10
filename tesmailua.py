import mysql.connector as mysql

connection = mysql.connect(
    host='127.0.0.1',
    port= 3306,
    database= 'ankkalinna',
    user= 'tomi',
    password= 'mariadb',
    autocommit= True
)

sql = f'''
select nimi
from lemmikki
where id in (
    select max(id)
    from lemmikki
)
'''

with connection.cursor() as cursor:
    cursor.execute(sql)
    print(cursor.fetchall())