
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from portfolioPortal.cv_app.config import ProductionConfig
from portfolioPortal.database import db


bcrypt = Bcrypt()
mail = Mail()

# sqlalchemy_logger = logging.getLogger("sqlalchemy.engine")
# sqlalchemy_logger.setLevel(logging.DEBUG)
# sqlalchemy_logger.addHandler(logging.StreamHandler())


def create_app(config_class=ProductionConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Importing routes after the app is initialized to prevent a circular import.
    from portfolioPortal.cv_app.main.routes import main_bp
    from portfolioPortal.cv_app.faqs.routes import faqs_bp
    from portfolioPortal.cv_app.contact.routes import contact_bp
    from portfolioPortal.cv_app.about.routes import about_bp
    from portfolioPortal.cv_app.errors.routes import errors_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(faqs_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(errors_bp)

    # The SQLAlchemy db object is imported before the app is created and the apps database is initialized after that.
    # https://stackoverflow.com/questions/20744277/sqlalchemy-create-all-does-not-create-tables

    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)

    return app
