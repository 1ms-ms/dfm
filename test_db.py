import mysql.connector
import json

con = mysql.connector.connect(option_files='my.conf')

sqlite_table = """ CREATE TABLE note (
    id int NOT NULL AUTO_INCREMENT,
    content varchar(255) NOT NULL,
    PRIMARY KEY(id)
)"""
#create db
cur = con.cursor()
cur.execute(sqlite_table)
