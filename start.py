from json import load
from os import path

from flask import Flask, render_template, send_file

from article import Article

app = Flask(__name__)

app.template_folder = './web'

with open('./res/const.json', 'r') as file:
    const = load(file)


@app.route('/web/<path:path_>')
def download(path_: str):
    path_ = path.join(app.template_folder, path_)
    return send_file(path_)


@app.route('/')
def index():
    return render_template('index.html', articles=Article.get_articles(), const=const)


@app.route('/post/<id_>')
def post(id_: str):
    return render_template('post.html', article=Article.get_article(id_), const=const)


if __name__ == '__main__':
    app.debug = True
    app.run(port=8000)
