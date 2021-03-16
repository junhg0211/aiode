import re
from datetime import datetime
from os import listdir, path
from pathlib import Path

from markdown import markdown


class Article:
    DIRECTORY = './res/article'
    HASHTAG_RE = re.compile(r'#[^( |\n)]+')

    @staticmethod
    def get_articles(limit: int = 5) -> list:
        return [Article.get_article(filename, True) for filename in listdir(Article.DIRECTORY)[::-1][:limit]]

    @staticmethod
    def get_article(id_: str, is_filename: bool = False):
        if is_filename:
            filename = id_
        else:
            filename = id_ + '.md'
        with open(file_path := path.join(Article.DIRECTORY, filename), 'r', encoding='utf-8') as file:
            title, content = file.read().split('\n', 1)
            hashtags = [hashtag[1:] for hashtag in re.findall(Article.HASHTAG_RE, content)]
            content = markdown(content.strip(), extensions=('fenced_code', 'codehilite'))
            title = markdown(title.strip())
        stat = Path(file_path).stat()
        edited_at = datetime.fromtimestamp(stat.st_atime)
        wrote_at = datetime.fromtimestamp(stat.st_mtime)
        id_ = path.split(filename)[-1][::-1].split('.', 1)[1][::-1]
        return Article(id_, title, wrote_at, edited_at, content, hashtags)
    
    @staticmethod
    def get_articles_by_hashtag(hashtag: str, limit: int = 5) -> list:
        result = list()
        for filename in listdir(Article.DIRECTORY)[::-1][:limit]:
            article = Article.get_article(filename, True)
            if hashtag in article.hashtags:
                result.append(article)
        return result

    def __init__(self, id_: str, title: str, wrote_at: datetime, edited_at: datetime, content: str, hashtags: list):
        self.id = id_
        self.title = title
        self.wrote_at = wrote_at
        self.edited_at = edited_at
        self.content = content
        self.hashtags = hashtags
