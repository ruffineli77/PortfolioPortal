
from database import db
from flask import current_app
from flask import Blueprint, render_template
from cv_app.faqs.models import FaQuestion
from pathlib import Path

faqs_bp = Blueprint('faqs', __name__, template_folder='templates')


@faqs_bp.route('/faqs')
def faqs():
    title = "FAQs"
    base_path = current_app.root_path
    web_dev_url = Path(base_path, "static/json/webdev.json")
    portfolio_url = Path(base_path, "static/json/portfolio.json")

    questions = db.session.query(FaQuestion).order_by(FaQuestion.question_id).distinct()
    webdev_faqs = FaQuestion.query.filter_by(source_file=str(web_dev_url)).all()
    bio_faqs = FaQuestion.query.filter_by(source_file=str(portfolio_url)).all()

    return render_template('faqs.html', title=title, 
                           all_questions=questions, webdev_faqs=webdev_faqs, bio_faqs=bio_faqs)
