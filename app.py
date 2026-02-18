# impot the flask frame work
from flask import *


# Below we create a web server based application
app = Flask(__name__)

# below we create the home route
# Routing: this is mapping/connecting different resources to different funtions. We do this by the help of a decprator
@app.route("/api/home")
def home():
    return jsonify({"message" : "Home Route accessed"})


# below is the products route
@app.route("/api/products")
def products():
    return jsonify({"message" : "Welcome to the products route"})


# below is a route for additon
@app.route("/api/calc", methods=["POST"])
def calculator():
    if request.method == "POST":
         number1 = request.form["number1"]
         number2 = request.form["number2"]
         sum = int(number1) + int(number2)


         return jsonify({"The answer is": sum})
    


# create a route that is able to calculate the simple interest given the pricipal as 20000, rate as 7% and time as 8 years.



# below we run the application
app.run(debug=True)