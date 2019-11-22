from pymysql import connect
import os

connection = connect(
    host = os.getenv('MYSQL_HOST'),
    user = os.getenv('MYSQL_USER'),
    password = os.getenv('MYSQL_PASSWORD'),
    db = os.getenv('MYSQL_DATABASE'),
    charset = 'utfmb4'
)


#This is an insert statement
try:
    with connection.cursor() as cursor:
        query = 'INSERT INTO .......;'
        cursor.execute(query)
#   Commits only have to be made when something is being written to the database
    connection.commit()

    with connection.cursor() as cursor:
        query = 'SELECT * FROM Account;'
        cursor.execute(query)
#       No need to commit as it is a read query
        result = cursor.fetchall()
#       Result will return a table tuple
        print(result)

finally:
    connection.close()
    


