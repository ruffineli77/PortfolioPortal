
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class ProductionConfig:
    def __init__(self):
        self.CV_APP_ADDRESS = os.environ.get("CV_APP_ADDRESS")
        self.SSL_CONTEXT = temp_ssl_context(self)
        self.SESSION_COOKIE_HTTPONLY = True
        self.SESSION_COOKIE_SAMESITE = 'None'
        self.SESSION_COOKIE_SECURE = True
        self.BASE_DIR = os.path.abspath(os.path.dirname(__file__))
        self.SECRET_KEY = os.environ.get('SECRET_KEY')
        self.SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
        self.SQLALCHEMY_BINDS = {}
        self.STATIC_URL_PATH = "/static"
        self.STATIC_FOLDER = "static"
        self.MAIL_SERVER = 'smtp.googlemail.com'
        self.MAIL_PORT = 587
        self.MAIL_USE_TLS = True
        self.MAIL_USERNAME = os.environ.get('EMAIL_USER')
        self.MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
        self.DEBUG = False
        self.TESTING = False
        self.MAIL_SUPPRESS_SEND = False


class DevelopmentConfig:
    def __init__(self):
        self.CV_APP_ADDRESS = os.environ.get("CV_APP_ADDRESS")
        self.SSL_CONTEXT = temp_ssl_context(self)
        self.SESSION_COOKIE_HTTPONLY = True
        self.SESSION_COOKIE_SAMESITE = 'None'
        self.SESSION_COOKIE_SECURE = True
        self.BASE_DIR = os.path.abspath(os.path.dirname(__file__))
        self.SECRET_KEY = os.environ.get('SECRET_KEY')
        self.SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
        self.SQLALCHEMY_BINDS = {}
        self.STATIC_URL_PATH = "/static"
        self.STATIC_FOLDER = "static"
        self.MAIL_SERVER = 'smtp.googlemail.com'
        self.MAIL_PORT = 587
        self.MAIL_USE_TLS = True
        self.MAIL_USERNAME = os.environ.get('EMAIL_USER')
        self.MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
        self.DEBUG = True
        self.TESTING = False
        self.MAIL_SUPPRESS_SEND = False


class TestingConfig:
    def __init__(self):
        self.CV_APP_ADDRESS = os.environ.get("CV_APP_ADDRESS")
        self.SSL_CONTEXT = temp_ssl_context(self)
        self.SESSION_COOKIE_HTTPONLY = False
        self.SESSION_COOKIE_SAMESITE = 'None'
        self.SESSION_COOKIE_SECURE = True
        self.BASE_DIR = os.path.abspath(os.path.dirname(__file__))
        self.SECRET_KEY = os.environ.get('SECRET_KEY')
        self.SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
        self.SQLALCHEMY_BINDS = {}
        self.STATIC_URL_PATH = "/static"
        self.STATIC_FOLDER = "static"
        self.MAIL_SERVER = 'smtp.googlemail.com'
        self.MAIL_PORT = 587
        self.MAIL_USE_TLS = True
        self.MAIL_USERNAME = os.environ.get('EMAIL_USER')
        self.MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
        self.DEBUG = False
        self.TESTING = True
        self.MAIL_SUPPRESS_SEND = False


def temp_ssl_context(config=None):
    if config is None:
        return (
            "None/private.pem",
            "None/public.pem"
        )

    if isinstance(config, TestingConfig) or isinstance(config, DevelopmentConfig) or (config, ProductionConfig):
        return (
            str(Path(BASE_DIR, 'certs/public.pem')),
            str(Path(BASE_DIR, 'certs/private.pem'))
        )

    else:
        return (
            "unknown/private.pem",
            "unknown/private.pem"
        )


def home_test_certs():
    ssl_context = temp_ssl_context(TestingConfig())
    private_cert = Path(ssl_context[0])
    public_cert = Path(ssl_context[1])

    if Path.is_file(private_cert) and Path.is_file(public_cert):
        print("Both files exist!")
    else:
        print(f'Certificates not found!\nPrivate: {private_cert}\nPublic: {public_cert}')


# home_test_certs()
