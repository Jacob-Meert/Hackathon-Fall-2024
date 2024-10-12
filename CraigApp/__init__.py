from flask import Flask
import secrets

def create_app():
    # Create a Flask application instance
    app = Flask(__name__)

    app.config['SECRET_KEY'] = secrets.token_hex(16)

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app

