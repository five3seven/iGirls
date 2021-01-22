from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from iGirls.config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from iGirls.play.routes import play_blueprint
    from iGirls.scoreboard.routes import scoreboard_blueprint
    from iGirls.vote.routes import vote_blueprint
    from iGirls.home.routes import home_blueprint
    from iGirls.report.routes import report_blueprint
    app.register_blueprint(play_blueprint)
    app.register_blueprint(scoreboard_blueprint)
    app.register_blueprint(vote_blueprint)
    app.register_blueprint(home_blueprint)
    app.register_blueprint(report_blueprint)

    return app