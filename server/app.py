from flask import Flask, make_response, request, session
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, User, FantasyLeague, FantasyTeam, Player, Game
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fantasy.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
migrate = Migrate(app, db)
db.init_app(app)

CORS(app)
api = Api(app)
bcrypt = Bcrypt(app)


@app.route("/")
def index():
    return f"<h1>Welcome to Flatiron Gang Fantasy League </h1>"


class Players(Resource):
    def get(self):
        all_players = Player.query.all()
        players_dict = [
            player.to_dict(
                only=(
                    "id",
                    "name",
                    "position",
                    "nfl_team",
                    "bye-week",
                    "fantasy_team_id",
                    "week_1_points",
                    "week_2_points",
                    "week_3_points",
                    "week_4_points",
                    "week_5_points",
                    "week_6_points",
                    "week_7_points",
                    "week_8_points",
                    "week_9_points",
                    "week_10_points",
                    "week_11_points",
                    "week_12_points",
                    "week_13_points",
                    "week_14_points",
                    "playoff_points",
                    "championship_points",
                )
            )
            for player in all_players
        ]
        response = make_response(players_dict, 200)
        return response


api.add_resource(Players, "/players")


class PlayerById(Resource):
    def get(self, id):
        player = Player.query.filter(Player.id == id).first()
        response = make_response(
            player.to_dict(
                only=(
                    "id",
                    "name",
                    "position",
                    "nfl_team",
                    "bye-week",
                    "fantasy_team_id",
                    "week_1_points",
                    "week_2_points",
                    "week_3_points",
                    "week_4_points",
                    "week_5_points",
                    "week_6_points",
                    "week_7_points",
                    "week_8_points",
                    "week_9_points",
                    "week_10_points",
                    "week_11_points",
                    "week_12_points",
                    "week_13_points",
                    "week_14_points",
                    "playoff_points",
                    "championship_points",
                )
            ),
            200,
        )
        return response

    def patch(self, id):
        player = Player.query.filter(Player.id == id).first()

        data = request.get_json()

        for attr in data:
            setattr(player, attr, data.get(attr))

        db.session.add(player.to_dict())
        db.session.commit()

        response = make_response(
            player.to_dict(
                only=(
                    "id",
                    "name",
                    "position",
                    "nfl_team",
                    "bye-week",
                    "fantasy_team_id",
                    "week_1_points",
                    "week_2_points",
                    "week_3_points",
                    "week_4_points",
                    "week_5_points",
                    "week_6_points",
                    "week_7_points",
                    "week_8_points",
                    "week_9_points",
                    "week_10_points",
                    "week_11_points",
                    "week_12_points",
                    "week_13_points",
                    "week_14_points",
                    "playoff_points",
                    "championship_points",
                )
            ),
            202,
        )
        return response


api.add_resource(PlayerById, "/players/<int:id>")


class FantasyTeams(Resource):
    def get(self):
        all_teams = FantasyTeam.query.all()
        teams_dict = [
            team.to_dict(only=("id", "team_name", "league_id", "user_id"))
            for team in all_teams
        ]
        response = make_response(teams_dict, 200)
        return response

    def post(self):
        data = request.get_json()

        new_data = FantasyTeam(
            team_name=data.get("team_name"),
            league_id=data.get("league_id"),
            user_id=data.get("user_id"),
        )

        db.session.add(new_data.to_dict())
        db.session.commit()

        response = make_response(
            new_data.to_dict(only=("id", "team_name", "league_id", "user_id")), 201
        )
        return response


api.add_resource(FantasyTeams, "/fantasy_teams")


class FantasyTeamsById(Resource):
    def get(self, id):
        fantasy_team = FantasyTeam.query.filter(FantasyTeam.id == id).first()

        response = make_response(
            fantasy_team.to_dict(only=("id", "team_name", "league_id", "user_id")), 200
        )

        return response

    def patch(self, id):
        fantasy_team = FantasyTeam.query.filter(FantasyTeam.id == id).first()

        data = request.get_json()

        for attr in data:
            setattr(fantasy_team, attr, data.get(attr))

        db.session.add(fantasy_team.to_dict())
        db.session.commit()

        response = make_response(
            fantasy_team.to_dict(only=("id", "team_name", "league_id", "user_id")), 202
        )

        return response


api.add_resource(FantasyTeamsById, "/fantasy_teams/<int:id>")


class Games(Resource):
    def get(self):
        all_games = Game.query.all()
        games_dict = [
            game.to_dict(
                only=(
                    "id",
                    "team_1_id",
                    "team_2_id",
                    "team_1_score",
                    "team_2_score",
                    "winner_id",
                )
            )
            for game in all_games
        ]

        response = make_response(games_dict, 200)
        return response

    def post(self):
        data = request.get_json()
        new_data = Game(
            team_1_id=data.get("team_1_id"),
            team_2_id=data.get("team_2_id"),
            team_1_score=data.get("team_1_score"),
            team_2_score=data.get("team_2_score"),
            winner_id=data.get("winner_id"),
        )

        db.session.add(new_data.to_dict())
        db.session.commit()

        response = make_response(
            new_data.to_dict(
                only=(
                    "id",
                    "team_1_id",
                    "team_2_id",
                    "team_1_score",
                    "team_2_score",
                    "winner_id",
                )
            ),
            201,
        )

        return response


api.add_resource(Games, "/games")


class GameById(Resource):
    def get(self, id):
        game = Game.query.filter(Game.id == id).first()

        response = make_response(
            game.to_dict(
                only=(
                    "id",
                    "team_1_id",
                    "team_2_id",
                    "team_1_score",
                    "team_2_score",
                    "winner_id",
                )
            ),
            200,
        )

        return response

    def patch(self, id):
        game = Game.query.filter(Game.id == id).first()

        data = request.get_json()

        for attr in data:
            setattr(game, attr, data.get(attr))

        db.session.add(game.to_dict)
        db.session.commit()

        response = make_response(
            game.to_dict(
                only=(
                    "id",
                    "team_1_id",
                    "team_2_id",
                    "team_1_score",
                    "team_2_score",
                    "winner_id",
                )
            ),
            202,
        )

        return response


api.add_resource(GameById, "/games/<int:id>")


class Users(Resource):
    def get(self):
        all_users = User.query.all()

        users_dict = [
            user.to_dict(only=("id", "name", "username")) for user in all_users
        ]

        response = make_response(users_dict, 200)

        return response

    def post(self):
        data = request.get_json()

        new_data = User(
            name=data.get("name"),
            username=data.get("username"),
            password=data.get("password"),
        )

        db.session.add(new_data.to_dict())
        db.session.commit()

        response = make_response(new_data.to_dict(only=("id", "name", "username")), 201)

        return response


api.add_resources(Users, "/users")


class UserById(Resource):
    def get(self, id):
        user = User.query.filter(User.id == id).first()

        response = make_response(user.to_dict(only=("id", "name", "username")), 200)

        return response

    def delete(self, id):
        user = User.query.filter(User.id == id).first()

        db.session.delete(user.to_dict())
        db.commit()

        return make_response({}, 204)


api.add_resource(UserById, "/users/<int:id>")


class Login(Resource):
    def post(self):
        username = request.get_json()["username"]
        user = User.query.filter(User.username == username)

        password = request.get_json()["password"]

        if user.authenticate(password):
            session["user_id"] = user.id
            return make_response(user.to_dict(), 200)
        return make_response({"error": "Invalid username or password"}, 401)


class CheckSession(Resource):
    def get(self):
        user = User.query.filter(User.id == session.get("user_id")).first()
        if user:
            return make_response(user.to_dict(), 200)
        else:
            return make_response({"message": "401: Not Authorized"}, 401)


api.add_resource(CheckSession, "/check_session")


class Logout(Resource):
    def delete(self):
        session["user_id"] = None
        return make_response({"message": "204: No Content"}, 204)


api.add_resource(Logout, "/logout")


if __name__ == "__main__":
    app.run(port=5555, debug=True)
