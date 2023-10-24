
from database import db


class ContactFormModel(db.Model):
    contact_form_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    company = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    subject = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f"FaQuestion('{self.email}', '{self.name}', '{self.company}', '{self.content}')"
