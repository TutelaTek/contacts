from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jsldfjlasdjfjalkdsjfj'

    from .application import contact

   
    app.register_blueprint(contact, url_prefix='/')
    return app