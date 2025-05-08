from flask import Flask
from app.routes.registration_routes import registration_bp
from app.routes.login_routes import login_bp
from app.routes.home_routes import home_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key_here'  # Use a secure random key

    app.register_blueprint(registration_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(home_bp)

    return app
