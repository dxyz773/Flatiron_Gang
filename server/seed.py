from models import Fan, Player, Like
from config import app, db
from random import choice

with app.app_context():
    Fan.query.delete()
    Like.query.delete()
    Player.query.delete()

    fan1 = Fan(
        name="Demi",
        username="demixyz773",
        img="imgs/etty-fidele-UBJsHb3HLv8-unsplash.jpg",
        _password_hash="12323nsdghdsflng12ou4y23o4",
    )
    fan2 = Fan(
        name="Billy P",
        username="billylowry",
        img="imgs/irene-strong-TMt3JGoVlng-unsplash.jpg",
        _password_hash="12432ouhfskdjf7i9w4rw4r4",
    )
    fan3 = Fan(
        name="Yemi A",
        username="tim",
        img="imgs/elizeu-dias-2EGNqazbAMk-unsplash.jpg",
        _password_hash="12432546744375349w4rw4r4",
    )
    fan4 = Fan(
        name="Victoria P.",
        username="vicky123",
        img="imgs/stephanie-liverani-Zz5LQe-VSMY-unsplash.jpg",
        _password_hash="7645762nsdghdsflng12ou4y23o4",
    )
    fan5 = Fan(
        name="Ashley F.",
        username="AshTheBest",
        img="imgs/jake-nackos-IF9TK5Uy-KI-unsplash.jpg",
        _password_hash="124564754576576i9w4rw4r4",
    )

    fans = [fan1, fan2, fan3, fan4, fan5]
    db.session.add_all(fans)

    player1 = Player(
        img="https://static.clubs.nfl.com/image/private/t_thumb_squared_2x/f_auto/chiefs/iwmsg6lhulvntsg327gk.jpg",
        name="Patrick Mahomes",
        age=27,
        team="Kansas City Chiefs",
        position="QB",
        number=15,
        bye_week=10,
    )
    player2 = Player(
        img="https://static.clubs.nfl.com/image/private/t_thumb_squared_2x/f_auto/bengals/ggco0lxn01s4nbh4ws7l.jpg",
        name="Joe Burrow",
        age=26,
        team="Cincinnati Bengals",
        position="QB",
        number=9,
        bye_week=7,
    )
    player3 = Player(
        img="https://static.clubs.nfl.com/image/private/t_thumb_squared_2x/f_auto/vikings/opjji2r1uulvqwwpbgdo.jpg",
        name="Justin Jefferson",
        age=24,
        team="Minnesota Vikings",
        position="WR",
        number=18,
        bye_week=13,
    )
    player4 = Player(
        img="https://static.clubs.nfl.com/image/private/t_thumb_squared_2x/f_auto/cardinals/fvpufsgjxofsrqf9yek6.jpg",
        name="Kylar Murray",
        age=25,
        team="Arizona Cardinals",
        position="QB",
        number=1,
        bye_week=14,
    )
    player5 = Player(
        img="https://static.clubs.nfl.com/image/private/t_thumb_squared_2x/f_auto/chiefs/g3dx0oiwosi4myembgwe.jpg",
        name="Travis Kelce",
        age=33,
        team="Kansas City Chiefs",
        position="TE",
        number=87,
        bye_week=10,
    )
    player6 = Player(
        img="https://static.clubs.nfl.com/image/private/t_thumb_squared_2x/f_auto/cardinals/ntce6ir7wsrxhpnlgh68.jpg",
        name="Marquise Brown",
        age=26,
        team="Arizona Cardinals",
        position="WR",
        number=2,
        bye_week=14,
    )

    #  name="Colt McCoy",
    # position="QB",
    # team="Arizona Cardinals",
    # bye_week=14,
    # player3 = Player(
    #     name="James Conner",
    #     position="RB",
    #     nfl_team="Arizona Cardinals",
    #     bye_week=14,
    # )
    # player4 = Player(
    #     name="Keaontay Ingram", position="RB", nfl_team="Arizona Cardinals", bye_week=14
    # )

    # player6 = Player(
    #     name="Rondale Moore",
    #     position="WR",
    #     nfl_team="Arizona Cardinals",
    #     bye_week=14,
    # )
    # player7 = Player(
    #     name="Greg Dortch",
    #     position="TE",
    #     nfl_team="Arizona Cardinals",
    #     bye_week=14,
    # )
    # player8 = Player(
    #     name="Trey McBride",
    #     position="TE",
    #     nfl_team="Arizona Cardinals",
    #     bye_week=14,
    # )
    # player9 = Player(
    #     name="Zach Ertz",
    #     position="TE",
    #     nfl_team="Arizona Cardinals",
    #     bye_week=14,
    # )
    # player10 = Player(
    #     name="Cardinals D/ST",
    #     position="D/ST",
    #     nfl_team="Arizona Cardinals",
    #     bye_week=14,
    # )
    # player11 = Player(
    #     name="Desmond Ridder",
    #     position="QB",
    #     nfl_team="Atlanta Falcons",
    #     bye_week=11,
    # )
    # player12 = Player(
    #     name="Taylor Heinicke",
    #     position="QB",
    #     nfl_team="Atlanta Falcons",
    #     bye_week=11,
    # )
    # player13 = Player(
    #     name="Bijan Robinson",
    #     position="RB",
    #     nfl_team="Atlanta Falcons",
    #     bye_week=11,
    # )
    # player14 = Player(
    #     name="Tyler Allgeier",
    #     position="RB",
    #     nfl_team="Atlanta Falcons",
    #     bye_week=11,
    # )
    # player15 = Player(
    #     name="Cordarrelle Patterson",
    #     position="WR",
    #     nfl_team="Atlanta Falcons",
    #     bye_week=11,
    # )
    # player16 = Player(
    #     name="Drake London",
    #     position="WR",
    #     nfl_team="Atlanta Falcons",
    #     bye_week=11,
    # )
    # player17 = Player(
    #     name="Mack Hollins",
    #     position="WR",
    #     nfl_team="Atlanta Falcons",
    #     bye_week=11,
    # )
    # player18 = Player(
    #     name="Scott Miller", position="WR", nfl_team="Atlanta Falcons", bye_week=11
    # )

    # player19 = Player(
    #     name="Kyle Pitts",
    #     position="TE",
    #     nfl_team="Atlanta Falcons",
    # )
    # player20 = Player(
    #     name="Jonnu Smith",
    #     position="TE",
    #     nfl_team="Atlanta Falcons",
    #     bye_week=11,
    # )
    # player21 = Player(
    #     name="Falcons D/ST",
    #     position="D/ST",
    #     nfl_team="Atlanta Falcons",
    #     bye_week=11,
    # )

    players = [
        player1,
        player2,
        player3,
        player4,
        player5,
        player6,
    ]
    db.session.add_all(players)

    like_types = ["like", "love", "dislike"]

    like1 = Like(
        like_type=choice(like_types),
        fan=choice(fans),
        player=choice(players),
    )

    like2 = Like(
        like_type=choice(like_types),
        fan=choice(fans),
        player=choice(players),
    )
    like3 = Like(
        like_type=choice(like_types),
        fan=choice(fans),
        player=choice(players),
    )

    like4 = Like(
        like_type=choice(like_types),
        fan=choice(fans),
        player=choice(players),
    )
    like5 = Like(
        like_type=choice(like_types),
        fan=choice(fans),
        player=choice(players),
    )
    like6 = Like(
        like_type=choice(like_types),
        fan=choice(fans),
        player=choice(players),
    )

    likes = [like1, like2, like3, like4, like5, like6]
    db.session.add_all(likes)

    db.session.commit()
