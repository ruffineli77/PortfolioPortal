
from portfolioPortal.database import db
from flask import Blueprint, render_template
from portfolioPortal.cv_app.faqs.utils import insert_faqs
from portfolioPortal.cv_app.faqs.models import FaQuestion
from portfolioPortal.cv_app.contact.models import ContactFormModel
from sqlalchemy.exc import OperationalError
from flask import current_app


main_bp = Blueprint('main', __name__)


def is_model_initialized(model):
    try:
        return model.query.first() is not None
    except OperationalError:
        return False


def initialize_db_and_insert_models(models, insertion_functions):
    with current_app.app_context():

        db.create_all()

        for model, insertion_function in zip(models, insertion_functions):
            if not is_model_initialized(model):
                insertion_function()

        db.session.commit()


@main_bp.route('/')
@main_bp.route("/home")
def home():
    title = "Elijah Ruffin Portfolio"
    models_to_initialize = [FaQuestion, ContactFormModel]
    insertion_functions_to_call = [insert_faqs]
    initialize_db_and_insert_models(models_to_initialize, insertion_functions_to_call)

    return render_template('home.html', title=title, is_home_page=True)


@main_bp.route('/projects')
def projects():
    title = "Portfolio Projects"

    return render_template('projects.html', title=title)
