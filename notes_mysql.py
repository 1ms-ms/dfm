from flask import Flask, request, jsonify
import json
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

#connect to db
def db_connection():
    con = None
    try:
        con = mysql.connector.connect(host='127.0.0.1',
                                         user='<enter user, root',
                                         database='<enter database, mysql',
                                         password='<enter password')
    except Error as e:
        print("Error while connecting to MySQL", e)
    return con

#List all the notes
@app.route("/", methods=["GET"])
def notes():
    note = None
    con = db_connection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM note")
    notes = [
        dict(id=row[0],content=row[1])
        for row in cursor.fetchall()
        ]
    if notes is not None:  
        con.close()
        return jsonify(notes) 
#Post a note 
@app.route("/create", methods=["POST"])
def notes_post():
    con = db_connection()
    cursor = con.cursor()

    new_content = request.json["content"]
    cursor.execute("INSERT INTO note (content) VALUES (%s)", (new_content,))
    con.commit()
    cursor.close()
    return "Success", 200

#Delete a note with given id
@app.route("/delete/<int:id>", methods=["DELETE"])
def notes_delete(id):
    con = db_connection()
    cursor = con.cursor()
       
    sql = """ DELETE FROM note WHERE id= %s """
    cursor.execute(sql, (id,))
    con.commit()
    con.close()
    return "Deleted note with id: {} .".format(id), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
