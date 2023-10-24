
import os
from cv_app import create_app
from cv_app.config import ProductionConfig, DevelopmentConfig, TestingConfig

env = os.environ.get('FLASK_DEBUG', 'production')
address, port = os.environ.get('CV_APP_ADDRESS').split(':')


prod, dev, test = ProductionConfig(), DevelopmentConfig(), TestingConfig()

if env == 'production':
    app = create_app(prod)
elif env == 'development':
    app = create_app(dev)
else:
    app = create_app(test)


# host_addr, port_num = app.config['CV_APP_ADDRESS'].split(':')[0], app.config['CV_APP_ADDRESS'].split(':')[1]
host_addr, port_num = "0.0.0.0", app.config['CV_APP_ADDRESS'].split(':')[1]

if __name__ == "__main__":
    with app.app_context():
        print(f" * App running in a {env} environment.")
        app.run(host=host_addr, port=port_num, ssl_context=app.config['SSL_CONTEXT'])
