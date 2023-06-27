from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from models import db, User, FantasyLeague, FantasyTeam, Player, Game

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fantasy.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)


@app.route("/")
def index():
    return f"<h1>Welcome to Flatiron Gang Fantasy League </h1>"


if __name__ == "__main__":
    app.run(port=5555, debug=True)
