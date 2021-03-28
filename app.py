
from flask import Flask, render_template, jsonify, request, json, Response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from random import *
import config

app = Flask(__name__,
            static_folder="frontend/dist/static",
            template_folder="frontend/dist")

app.config.from_object(config)
db = SQLAlchemy(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

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


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(10), nullable=False)
    content = db.Column(db.Text, nullable=False)
db.create_all()

# title = request.args.get("title")
# content = request.args.get("content")
#测试数据库连接并新增一条数据
article = Article(title = "333", content = "jfnsid")
db.session.add(article)
db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)