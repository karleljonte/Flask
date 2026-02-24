# Below is the first question
from flask import *
import os
import pymysql

app = Flask (__name__)

app.config["UPLOAD_FOLDER"] = "static/images"

@app.route("/api/laptop", methods=["POST"])
def addproducts():
    if request.method == "POST":
        name = request.form["name"]
        brand = request.form["brand"]
        processor = request.form["processor"]
        ram = request.form["ram"]
        storage = request.form["storage"]
        screensize = request.form["screensize"]
        price = request.form["price"]
        stock = request.form["stock"]
        photo = request.files["photo"]

        filename=photo.filename
        photo_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        photo.save(photo_path)

        connection = pymysql.connect(host="localhost", user="root", password="", database="online")
        
        cursor = connection.cursor()

        sql = "INSERT INTO laptop(name, brand, processor, ram, storage, screensize, price, stock, photo) VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s)"
        data = (name, brand, processor, ram, storage, screensize, price, stock, photo)

        cursor.execute(sql, data)
        connection.commit()



        return jsonify({"Message" : "added successfully"})













app.run(debug=True)