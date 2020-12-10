from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    CORS(app)

    # load correct config depending on dev or prod, refer to config.py
    if os.getenv('FLASK_ENV') == 'production':
        config = 'config.ProductionConfig'
    elif os.getenv('FLASK_ENV') == 'development':
        config = 'config.DevelopmentConfig'

    app.config.from_object(config)

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # Include our Routes
        from . import routes as shared_routes
        from .advertisers import routes as advertisers_routes
        from .discord_users import routes as discord_users_routes

        db.create_all()

        # Register Blueprints
        app.register_blueprint(advertisers_routes.advertisers)
        app.register_blueprint(discord_users_routes.discord_users)

        return app