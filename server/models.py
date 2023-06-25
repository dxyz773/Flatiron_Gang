from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)


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
        "FantasyTeam", back_populates="owner", cascade="all, delete-orphan"
    )
    players = association_proxy("fantasy_team", "players")


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
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"))
    league_id = db.Column(db.Integer, db.ForeignKey("fantasy_leagues.id"))
    # relationships
    owner = db.relationship("User", back_populates="fantasy_teams")
    players = db.relationship("Player", back_populates="fantasy_teams")
    league = db.relationship("FantasyLeague", back_populates="fantasy_teams")


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
    # foreign key
    game_stat_id = db.Column(db.Integer, db.ForeignKey("game_stats.id"))
    # relationships
    stats = db.relationship("GameStat", back_populates="player")
    fantasy_teams = db.relationship(
        "FantasyTeam", back_populates="players", cascade="all, delete-orphan"
    )
    managers = association_proxy("fantasy_teams", "owner")


class GameStat(db.Model, SerializerMixin):
    __tablename__ = "game_stats"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    # class specific
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
    # relationship
    player = db.relationship("Player", back_populates="stats")


class FantasyLeague(db.Model, SerializerMixin):
    __tablename__ = "fantasy_leagues"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    # class specific
    name = db.Column(db.String, nullable=False)
    # relationships
    fantasy_teams = db.relationship("FantasyTeam", back_populates="league")

    # class Game(db.Model, SerializerMixin):
    #     __tablename__ = "games"
    #     id = db.Column(db.Integer, primary_key=True)
    #     created_at = db.Column(db.DateTime, server_default=db.func.now())
    #     updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    #     # class specific
