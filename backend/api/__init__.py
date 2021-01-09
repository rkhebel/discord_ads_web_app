from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import os
from flask_migrate import Migrate

db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    CORS(app, support_credentials = True)

    # load correct config depending on dev or prod, refer to config.py
    if os.getenv('FLASK_ENV') == 'production':
        config = 'config.ProductionConfig'
    elif os.getenv('FLASK_ENV') == 'development':
        config = 'config.DevelopmentConfig'

    app.config.from_object(config)

    # Initialize Plugins
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # Include our Routes
        from .auth import routes as auth_routes
        from .advertiser import routes as advertiser_routes
        from .discord import routes as discord_routes

        # Register Blueprints
        app.register_blueprint(auth_routes.auth)
        app.register_blueprint(advertiser_routes.advertiser)
        app.register_blueprint(discord_routes.discord)

        return app