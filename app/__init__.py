from flask import Flask
from app.config import Config


def create_app(config_class=Config):
    """Patrón Application Factory para crear la instancia de la aplicación Flask."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Registro de Blueprints
    from app.routes.blog import blog_bp

    app.register_blueprint(blog_bp)

    return app
