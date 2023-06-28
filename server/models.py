from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates, backref
from sqlalchemy.ext.hybrid import hybrid_property
from config import db, bcrypt


class User(db.Model, SerializerMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    # class specific
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)
    # relationships
    fantasy_teams = db.relationship(
        "FantasyTeam", backref=backref("user"), cascade="all, delete-orphan"
    )
    serialize_rules = (
        "-fantasy_teams.user",
        "-created_at",
        "-updated_at",
        "-_password_hash",
    )

    def __repr__(self):
        return f"user {self.username}, iD {self.id}"

    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode("utf-8"))
        self._password_hash = password_hash.decode("utf-8")

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode("utf-8"))


class FantasyTeam(db.Model, SerializerMixin):
    __tablename__ = "fantasy_teams"
    # base columns
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    # class specific
    team_name = db.Column(db.String, nullable=False)
    # foreign keys N
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    league_id = db.Column(db.Integer, db.ForeignKey("fantasy_leagues.id"))
    #  relationships
    games = db.relationship(
        "Game", backref=backref("fantasy_team"), cascade="all, delete-orphan"
    )
    players = db.relationship(
        "Player", backref=backref("fantasy_team"), cascade="all, delete-orphan"
    )
    serialize_rules = (
        "-user.fantasy_teams",
        "-fantasy_league.fantasy_teams",
        "-games.fantasy_team",
        "-players.fantasy_team",
    )


class Player(db.Model, SerializerMixin):
    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    # class specific
    name = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    nfl_team = db.Column(db.String, nullable=False)
    bye_week = db.Column(db.Integer, nullable=False)
    week_1_points = db.Column(db.Integer)
    week_2_points = db.Column(db.Integer)
    week_3_points = db.Column(db.Integer)
    week_4_points = db.Column(db.Integer)
    week_5_points = db.Column(db.Integer)
    week_6_points = db.Column(db.Integer)
    week_7_points = db.Column(db.Integer)
    week_8_points = db.Column(db.Integer)
    week_9_points = db.Column(db.Integer)
    week_10_points = db.Column(db.Integer)
    week_11_points = db.Column(db.Integer)
    week_12_points = db.Column(db.Integer)
    week_13_points = db.Column(db.Integer)
    week_14_points = db.Column(db.Integer)
    playoff_points = db.Column(db.Integer)
    championship_points = db.Column(db.Integer)
    # foreign key
    fantasy_team_id = db.Column(db.Integer, db.ForeignKey("fantasy_teams.id"))
    serialize_rules = ("-fantasy_team.players",)


class FantasyLeague(db.Model, SerializerMixin):
    __tablename__ = "fantasy_leagues"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    # class specific
    name = db.Column(db.String, nullable=False)
    # relationships
    fantasy_teams = db.relationship(
        "FantasyTeam", backref=backref("fantasy_league"), cascade="all, delete-orphan"
    )
    serialize_rules = ("-fantasy_teams.fantasy_league",)


class Game(db.Model, SerializerMixin):
    __tablename__ = "games"
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    # class specific
    team_1_id = db.Column(db.Integer, db.ForeignKey("fantasy_teams.id"))
    team_2_id = db.Column(db.Integer)
    team_1_score = db.Column(db.Integer)
    team_2_score = db.Column(db.Integer)
    winner_id = db.Column(db.Integer)
    serialize_rules = ("-fantasy_team.games",)
