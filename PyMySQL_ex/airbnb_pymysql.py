import pymysql
import pymysql.cursors

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='oz-password',
    db='airbnb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with connection.cursor() as cursor:
    sql = "INSERT INTO Product"