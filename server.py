import numpy as np
from flask import Flask, request, jsonify,render_template
import util
import pickle
import pandas as pd

app  = Flask(__name__)

@app.route('/')
def home():
   return render_template('app.html')

@app.route("/predict_diamond_price", methods=["POST"])
def predict_diamond_price():
    var1=request.form["cuttersss"]
    var2=float(request.form["Carat"])
    var3=float(request.form["Depth"])
    var4=float(request.form["Table"])
    response = util.get_diamond_price(var1,var2,var3,var4)
    
    return render_template("app.html",prediction_text="Diamond prediction is {}".format(response))

if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run(debug=True)
    




