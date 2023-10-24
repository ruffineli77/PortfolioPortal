
from database import db


class InfoPage(db.Model):
    info_id = db.Column(db.Integer, primary_key=True)
    info_code = db.Column(db.String(80), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    chapters = db.Column(db.String(1000), nullable=True)
    paragraphs = db.Column(db.String(1000), nullable=True)
    body = db.Column(db.String(1000), nullable=False)
    notes = db.Column(db.String(300))

    def __repr__(self):
        return f"InfoPage('{self.title}', '{self.body}', '{self.notes}')"
