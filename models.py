from app import db


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    category = db.Column(db.String(64))
    github = db.Column(db.String(250))
    url = db.Column(db.String(250))
    info = db.Column(db.String(5000))

    def __init__(self, name, category, info, github=None, url=None):
        self.name = name
        self.category = category
        self.info = info
        if github is not None:
            self.github = github
        if url is not None:
            self.url = url
