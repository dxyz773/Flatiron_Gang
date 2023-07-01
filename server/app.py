from flask import make_response, request, session
from flask_restful import Resource
from models import Fan, Player, Like
from config import app, db, api


@app.route("/")
def index():
    return f"<h1>Welcome to Flatiron Gang Football Lover </h1>"


class Players(Resource):
    def get(self):
        all_players = Player.query.all()
        players_dict = [
            player.to_dict(
                only=(
                    "id",
                    "img",
                    "name",
                    "age",
                    "team",
                    "position",
                    "number",
                    "bye_week",
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

        if not player:
            return make_response({"error": "Player not found"}, 404)

        response = make_response(
            player.to_dict(
                only=(
                    "id",
                    "img",
                    "name",
                    "age",
                    "team",
                    "position",
                    "number",
                    "bye_week",
                )
            ),
            200,
        )
        return response


api.add_resource(PlayerById, "/players/<int:id>")


class Likes(Resource):
    def get(self):
        all_likes = Like.query.all()
        likes_dict = [
            likes.to_dict(only=("id", "like_type", "fan_id,", "player_id"))
            for likes in all_likes
        ]
        response = make_response(likes_dict, 200)
        return response

    def post(self):
        data = request.get_json()

        try:
            new_like = Like(
                like_type=data.get("like_type"),
                fan_id=data.get("fan_id"),
                player_id=data.get("player_id"),
            )

            db.session.add(new_like.to_dict())
            db.session.commit()

        except:
            return make_response({"errors": ["validation errors"]}, 400)

        response = make_response(
            new_like.to_dict(only=("id", "like_type", "fan_id", "player_id")), 201
        )
        return response


api.add_resource(Likes, "/likes")


class LikesById(Resource):
    def get(self, id):
        like = Like.query.filter(Like.id == id).first()

        if not like:
            return make_response({"error": "FantasyTeam not found"}, 404)

        response = make_response(
            like.to_dict(only=("id", "like_type", "fan_id", "player_id")), 200
        )

        return response

    def delete(self, id):
        like = Like.query.filter(Like.id == id).first()

        if not like:
            return make_response({"error": "FantasyTeam not found"}, 404)

        try:
            db.session.delete(like)
            db.session.commit()

        except:
            return make_response({"errors": ["validation errors"]}, 400)

        response = make_response({}, 200)

        return response


api.add_resource(LikesById, "/likes/<int:id>")


class Fans(Resource):
    def get(self):
        all_fans = Fan.query.all()

        fans_dict = [
            fan.to_dict(only=("id", "name", "username", "img")) for fan in all_fans
        ]

        response = make_response(fans_dict, 200)

        return response


api.add_resource(Fans, "/fans")


class FansById(Resource):
    def get(self, id):
        fan = Fan.query.filter(Fan.id == id).first()
        if not fan:
            return make_response({"error": "User not found"}, 404)

        response = make_response(fan.to_dict(only=("id", "name", "username")), 200)
        return response

    def patch(self, id):
        fan = Fan.query.filter(Fan.id == id).first()

        if not fan:
            return make_response({"error": "Game not found"}, 404)

        data = request.get_json()

        try:
            for attr in data:
                setattr(fan, attr, data.get(attr))

                db.session.add(fan.to_dict)
                db.session.commit()

        except:
            return make_response({"errors": ["validation errors"]}, 400)

        response = make_response(
            fan.to_dict(only=("id", "name", "username", "image")),
            202,
        )

        return response

    def delete(self, id):
        fan = Fan.query.filter(Fan.id == id).first()

        if not fan:
            return make_response({"error": "User not found"}, 404)

        db.session.delete(fan.to_dict())
        db.commit()

        return make_response({}, 204)


api.add_resource(FansById, "/fans/<int:id>")


class Signup(Resource):
    def post(self):
        data = request.get_json()
        new_fan = Fan(
            name=data.get("name"), username=data.get("username"), img=data.get("img")
        )
        # 6b. hash the given password and save it to _password_hash
        new_fan.password_hash = data.get("password")
        # db.session add and commit
        db.session.add(new_fan)
        db.session.commit()
        # 6c. save the user_id in session
        session["user_id"] = new_fan.id
        # return response
        return make_response(new_fan.to_dict(rules=("-_password_hash",)), 201)


api.add_resource(Signup, "/fans")


class Login(Resource):
    def post(self):
        try:
            # 7a. check if user exists
            data = request.get_json()
            fan = Fan.query.filter_by(username=data.get("username")).first()
            # 7b. check if password is authentic
            if fan.authenticate(data.get("password")):
                # 7c. set session's user id
                session["user_id"] = fan.id
                return make_response(fan.to_dict(), 200)
        except:
            # 7d. send error
            return make_response({"message": "401: Not Authorized"}, 401)


api.add_resource(Login, "/login")


class CheckSession(Resource):
    def get(self):
        user = Fan.query.filter(Fan.id == session.get("user_id")).first()
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
