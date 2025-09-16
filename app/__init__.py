from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    # Register public blueprint explicitly (surface import errors!)
    from .routes.public import bp as public_bp
    app.register_blueprint(public_bp)

    # quick health endpoint (optional)
    @app.route("/health")
    def health():
        return "ok"

    return app


