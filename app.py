from flask import Flask, render_template, jsonify
from random import *

app = Flask(__name__,
            static_folder="frontend/dist/static",
            template_folder="frontend/dist")

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

if __name__ == "__main__":
    app.run(debug=True)