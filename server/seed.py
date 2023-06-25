from models import db, User, FantasyLeague, FantasyTeam, Player, GameStat
from app import app
from random import choice

with app.app_context():
    User.query.delete()
    FantasyLeague.query.delete()
    FantasyTeam.query.delete()
    Player.query.delete()
    GameStat.query.delete()

    demitry = User(
        name="Demitry",
        username="demixyz773",
        _password_hash="12323nsdghdsflng12ou4y23o4",
    )
    billy = User(
        name="Billy Lowry",
        username="billylowry",
        _password_hash="12432ouhfskdjf7i9w4rw4r4",
    )
    yemi = User(
        name="Yemi A",
        username="tim",
        _password_hash="12432546744375349w4rw4r4",
    )

    users = [yemi, billy, demitry]
    db.session.add_all(users)

    league1 = FantasyLeague(name="Flatiron Gang")

    db.session.add(league1)

    stat1 = GameStat(
        week_1_points=0,
        week_2_points=0,
        week_3_points=0,
        week_4_points=0,
        week_5_points=0,
        week_6_points=0,
        week_7_points=0,
        week_8_points=0,
        week_9_points=0,
        week_10_points=0,
        week_11_points=0,
        week_12_points=0,
        week_13_points=0,
        week_14_points=0,
        playoff_points=0,
        championship_points=0,
    )

    stat2 = GameStat(
        week_1_points=0,
        week_2_points=0,
        week_3_points=0,
        week_4_points=0,
        week_5_points=0,
        week_6_points=0,
        week_7_points=0,
        week_8_points=0,
        week_9_points=0,
        week_10_points=0,
        week_11_points=0,
        week_12_points=0,
        week_13_points=0,
        week_14_points=0,
        playoff_points=0,
        championship_points=0,
    )

    stat3 = GameStat(
        week_1_points=0,
        week_2_points=0,
        week_3_points=0,
        week_4_points=0,
        week_5_points=0,
        week_6_points=0,
        week_7_points=0,
        week_8_points=0,
        week_9_points=0,
        week_10_points=0,
        week_11_points=0,
        week_12_points=0,
        week_13_points=0,
        week_14_points=0,
        playoff_points=0,
        championship_points=0,
    )

    stats = [stat1, stat2, stat3]
    db.session.add_all(stats)

    mahomes = Player(
        name="Patrick Mahomes",
        position="QB",
        nfl_team="Kansas City Chiefs",
        bye_week=10,
        stats=choice(stats),
    )
    burrow = Player(
        name="Joe Burrow",
        position="QB",
        nfl_team="Cincinnati Bengals",
        bye_week=7,
        stats=choice(stats),
    )
    jefferson = Player(
        name="Justin Jefferson",
        position="WR",
        nfl_team="Minnesota Vikings",
        bye_week=13,
        stats=choice(stats),
    )
    players = [mahomes, burrow, jefferson]
    db.session.add_all(players)

    team1 = FantasyTeam(
        team_name="Strawberry Truthers",
        owner=choice(users),
        players=choice(players),
        league=league1,
    )
    team2 = FantasyTeam(
        team_name="In Mahomes I Trust",
        owner=choice(users),
        players=choice(players),
        league=league1,
    )
    team3 = FantasyTeam(
        team_name="Yemis Yetis",
        players=choice(players),
        owner=choice(users),
        league=league1,
    )

    teams = [team1, team2, team3]
    db.session.add_all(teams)

    db.session.commit()
