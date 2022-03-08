import mysql.connector
con = mysql.connector.connect(host='127.0.0.1',
                                         user='root',
                                         database='mysql',
                                         password='PASS')

sqlite_table = """ CREATE TABLE note (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content VARCHAR(255) NOT NULL
)"""
#create db
cur = con.cursor()
cur.execute(sqlite_table)
