from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    # Blueprints
    try:
        from .routes.public import bp as public_bp
        app.register_blueprint(public_bp)
    except Exception:
        # dacă nu există încă routes/public.py, aplicația pornește totuși
        pass

    return app

