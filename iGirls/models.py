from iGirls import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(31), unique=True)
    url = db.Column(db.String(1000), unique=True)
    score = db.Column(db.Integer)
    reports = db.Column(db.Integer, nullable=True)

    def __init__(self, username, url, score):
        self.username = username
        self.url = url
        self.score = score

    def __repr__(self):
        return f"Player('{self.username}', '{self.url}', '{self.score}')"
