
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
    print("list",list)
    resultId = recommendation.recommendationSysAlgorithm(list)
    result = database.getHouseByIds(resultId)
    response = {
        "result": result
    }
    return jsonify(response)

@app.route('/api/recommendById',methods=["POST"])
def recommendById():
    id = eval(str(request.data, encoding='utf-8'))
    house = list(database.getRecommendation(id))
    del house[0]
    print("house",house)
    resultId = recommendation.recommendationSysAlgorithm(house)
    result = database.getHouseByIds(resultId)
    print("result", result)
    response = {
        "result": result
    }
    return jsonify(response)

@app.route('/api/allHouses',methods=["POST"])
def getAll():
    n = eval(str(request.data, encoding='utf-8'))
    print("n=",type(n[1]))
    houses = list(database.getAllHouses(n[0],n[1]))
    response = {
        "house": houses
    }
    return jsonify(response)



@app.route('/api/nlp',methods=["POST"])
def process():
    m = eval(str(request.data, encoding='utf-8'))
    print("message=",m)
    print("type",type(m[1]))
    reply = nlp.NaturalLanguageProcess(m[0],m[1],m[2])
    print(reply)
    response = {
        "reply": reply
    }
    return jsonify(response)

# print(nlp.preprocessing())

if __name__ == "__main__":
    app.run(debug=True)