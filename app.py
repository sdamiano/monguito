from app import create_app
from app.config import Config

# Instanciación mediante Application Factory
app = create_app()

if __name__ == "__main__":
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG
    )