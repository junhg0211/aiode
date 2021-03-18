from json import load
from os import path

from flask import Flask, render_template, send_file

from article import Article

app = Flask(__name__)

app.template_folder = './web'

with open('./res/const.json', 'r', encoding='utf-8') as file:
    const = load(file)


@app.route('/web/<path:path_>')
def download(path_: str):
    path_ = path.join(app.template_folder, path_)
    return send_file(path_)


@app.route('/')
def index():
    app_ = const['article-per-page']
    return render_template('index.html', articles=Article.get_articles(to=app_), const=const, now_page=1,
                           article_count=Article.get_article_count(), article_per_page=app_)


@app.route('/p/<id_>')
def post(id_: str):
    if Article.is_article(id_):
        return render_template('post.html', articles=(Article.get_article(id_),), const=const)
    else:
        return 'No Article.'


@app.route('/h/<hashtag_>')
def hashtag(hashtag_: str):
    return render_template('post.html', articles=Article.get_articles_by_hashtag(hashtag_), const=const)


@app.route('/ps/<int:page>')
def posts(page: int):
    app_ = const['article-per-page']
    return render_template('post.html', articles=Article.get_articles((page - 1) * app_, page * app_), const=const,
                           now_page=page, article_count=Article.get_article_count(), article_per_page=app_)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
