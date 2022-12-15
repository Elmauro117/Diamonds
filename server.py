
from flask import Flask, request, jsonify
import util

app  = Flask(__name__)

@app.route('/get_cuts_names', methods=["GET"])
def get_cuts_names():
    response = jsonify({
        "cuts": util.get_cuts_names()
        })
    response.headers.add("Acces-Control-Allow-Origin","*")
    
    return response    
    
@app.route("/predict_diamond_price", methods=["GET","POST"])
def predict_diamond_price():
    vari1=str(request.form["vari1"])
    vari2=float(request.form["vari2"])
    vari3=float(request.form["vari3"])
    vari4=float(request.form["vari4"])
    
    response = jsonify({
        "estimated_price": util.get_diamond_price(vari1,vari2,vari3,vari4)
        })
    
    response.headers.add("Acces-Control-Allow-Origin","*")
    
    return response

if __name__ == "__main__":
    util.load_saved_artifacts()
    print("Starting Python Flask Serveru para predecir diamantes $$$")
    app.run()
    






