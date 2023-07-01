from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from config import db, bcrypt


class Fan(db.Model, SerializerMixin):
    __tablename__ = "fans"
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    # Class Specific
    name = db.Column(db.String, nullable=False)
    img = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)
    # Relationships
    likes = db.relationship("Like", back_populates="fan", cascade="all, delete-orphan")
    # Association proxy
    players = association_proxy("likes", "player")
    # Serialize Rules
    serialize_rules = (
        "-likes.fan",
        "-created_at",
        "-updated_at",
        "-_password_hash",
    )

    def __repr__(self):
        return f"<Fan {self.username}, iD {self.id}>"

    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash_setter(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode("utf-8"))
        self._password_hash = password_hash.decode("utf-8")

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode("utf-8"))


class Like(db.Model, SerializerMixin):
    __tablename__ = "likes"
    # base columns
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    # Class Specific
    like_type = db.Column(db.String, nullable=False)
    # Foreign Keys
    fan_id = db.Column(db.Integer, db.ForeignKey("fans.id"), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"))
    #  Relationships
    fan = db.relationship("Fan", back_populates="likes")
    player = db.relationship("Player", back_populates="likes")
    # Serialize Rules
    serialize_rules = (
        "-created_at",
        "-updated_at",
        "-fan.likes",
        "-player.likes",
    )


class Player(db.Model, SerializerMixin):
    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    # Class Specific
    img = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    team = db.Column(db.Integer, nullable=False)
    position = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    bye_week = db.Column(db.Integer, nullable=False)
    # Relationship
    likes = db.relationship("Like", back_populates="player")
    # Association Proxy
    fans = association_proxy("likes", "fan")
    # Serialize Rules
    serialize_rules = (
        "-created_at",
        "-updated_at",
        "-likes.player",
    )
