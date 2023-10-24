
import json
from flask import current_app
from database import db
from cv_app.faqs.models import FaQuestion
from pathlib import Path


# return the data from one json file.
def parse_json(json_file):
    json_file_path = json_file
    with open(json_file_path) as f:
        data = json.load(f)
    return data


def insert_faqs():
    base_path = current_app.root_path
    web_dev_url = Path(base_path, "static/json/webdev.json")
    portfolio_url = Path(base_path, "static/json/portfolio.json")
    faqs_files = [web_dev_url, portfolio_url]

    for faqs_file in faqs_files:
        faqs_data = parse_json(faqs_file)

        for index, faq in enumerate(faqs_data):
            faq_record = FaQuestion(source_file=str(faqs_file), question=faq['question'], answer=faq['answer'])
            exists = FaQuestion.query.filter_by(question=faq['question'], answer=faq['answer']).first()

            if not exists:
                db.session.add(faq_record)
