
from flask import Flask, render_template, jsonify, request, json, Response
from flask_cors import CORS
from random import *
import database
import recommendation
import nlp

app = Flask(__name__,
            static_folder="frontend/dist/static",
            template_folder="frontend/dist")

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
conn = database.conn



@app.route('/', defaults = {'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1,100)
    }
    return jsonify(response)

@app.route('/api/recommend',methods=["POST"])
def recommend():
    list = eval(str(request.data, encoding='utf-8'))
    resultId = recommendation.recommendationSysAlgorithm(list)
    result = database.getHouseByIds(resultId)
    response = {
        "result": result
    }
    return jsonify(response)

@app.route('/api/allHouses')
def getAll():
    houses = list(database.getAllHouses())
    response = {
        "house": houses
    }
    return jsonify(response)



@app.route('/api/nlp',methods=["POST"])
def process():
    m = eval(str(request.data, encoding='utf-8'))
    print("message=",m)
    reply = [nlp.preprocessing(m[0])]
    print(reply)
    response = {
        "reply": reply
    }
    return jsonify(response)

# print(nlp.preprocessing())

if __name__ == "__main__":
    app.run(debug=True)