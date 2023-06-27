from flask import Flask, make_response, request
from flask_restful import Api, Resource
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

class Players(Resource):
    def get(self):
        all_players = Player.query.all()
        players_dict = [player.to_dict(only=('id', 'name', 'position', 'nfl_team', 'bye-week',
                                            'fantasy_team_id','week_1_points','week_2_points',
                                            'week_3_points','week_4_points','week_5_points',
                                            'week_6_points','week_7_points','week_8_points',
                                            'week_9_points','week_10_points','week_11_points',
                                            'week_12_points','week_13_points','week_14_points',
                                            'playoff_points', 'championship_points')) for player in all_players]
        response = make_response(players_dict, 200)
        return response
api.add_resource(Players,'/players')

class PlayerById(Resource):
    def get(self, id):
        player = Player.query.filter(Player.id==id).first()
        response = make_response(player.to_dict(only=('id', 'name', 'position', 'nfl_team', 'bye-week','fantasy_team_id','week_1_points','week_2_points',
                                                      'week_3_points','week_4_points','week_5_points','week_6_points','week_7_points','week_8_points','week_9_points',
                                                      'week_10_points','week_11_points','week_12_points','week_13_points','week_14_points','playoff_points', 'championship_points')), 200)
        return response
    
    def patch(self, id):
        player = Player.query.filter(Player.id==id).first()

        data = request.get_json()

        for attr in data:
             setattr(player, attr, data.get(attr))

        db.session.add(player.to_dict())
        db.session.commit()

        response = make_response(player.to_dict(only=('id', 'name', 'position', 'nfl_team', 'bye-week','fantasy_team_id','week_1_points','week_2_points',
                                                      'week_3_points','week_4_points','week_5_points','week_6_points','week_7_points','week_8_points','week_9_points',
                                                      'week_10_points','week_11_points','week_12_points','week_13_points','week_14_points','playoff_points', 'championship_points')), 202)
        return response

    
api.add_resource(PlayerById,'/players/<int:id>')


class FantasyTeams(Resource):
    def get(self):
        pass








if __name__ == "__main__":
    app.run(port=5555, debug=True)
