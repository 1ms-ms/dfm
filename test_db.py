import mysql.connector
con = mysql.connector.connect(host='127.0.0.1',
                                         user='<enter user, root',
                                         database='<enter database, mysql',
                                         password='<enter password')

sqlite_table = """ CREATE TABLE note (
    id int NOT NULL AUTO_INCREMENT,
    content varchar(20) NOT NULL,
    PRIMARY KEY(id)
)"""
#create db
cur = con.cursor()
cur.execute(sqlite_table)
