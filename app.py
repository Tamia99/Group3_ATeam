
from flask import Flask, render_template, jsonify, request, json, Response
from flask_cors import CORS
from random import *
import database
import recommendation

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
    # list = tolist(request.data)
    d = bytes.decode(request.data)
    d = d.replace("\"","").replace("[","").replace("]","")
    list = d.split(",")
    # print(type(d))
    # print (list)
    return list

#database.test()

recommendation.recommendationSysAlgorithm()

conn.close()
if __name__ == "__main__":
    app.run(debug=True)