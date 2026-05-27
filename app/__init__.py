from pathlib import Path
from flask import Flask

from app.config import Config
from app.extensions import db, migrate


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    Path(app.instance_path).mkdir(parents=True, exist_ok=True)

    db.init_app(app)
    migrate.init_app(app, db)

    from app import models

    @app.get("/")
    def index():
        return {"message": "API do Sistema Imobiliario funcionando"}

    return app