# Below is the first question
from flask import *
import os
import pymysql

app = Flask (__name__)

app.config["UPLOAD_FOLDER"] = "static/images"

@app.route("/api/add_products", methods=["POST"])
def addproducts():
    if request.method == "POST":
        phonename = request.form["name"]
        brand = request.form["brand"]
        model = request.form["model"]
        storage = request.form["storage"]
        ram = request.form["ram"]
        battery = request.form["battery"]
        price = request.form["price"]
        stock = request.form["stock"]
        photo = request.files["photo"]

        filename=photo.filename
        photo_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        photo.save(photo_path)

        connection = pymysql.connect(host="localhost", user="root", password="", database="online")
        
        cursor = connection.cursor()

        sql = "INSERT INTO smartphone(phonename, brand, model, storage, RAM, battery, price, stock, photo) VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s)"
        data = (phonename, brand, model, storage, ram, battery, price, stock, photo)

        cursor.execute(sql, data)
        connection.commit()



        return jsonify({"Message" : "added successfully"})













app.run(debug=True)