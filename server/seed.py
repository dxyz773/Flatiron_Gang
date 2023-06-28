from models import User, FantasyLeague, FantasyTeam, Player, Game
from config import app, db
from random import choice

with app.app_context():
    User.query.delete()
    FantasyLeague.query.delete()
    FantasyTeam.query.delete()
    Player.query.delete()
    Game.query.delete()

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

    team1 = FantasyTeam(
        team_name="Strawberry Truthers",
        user=choice(users),
        league_id=1,
    )
    team2 = FantasyTeam(
        team_name="In Mahomes I Trust",
        user=choice(users),
        league_id=1,
    )
    team3 = FantasyTeam(
        team_name="Yemis Yetis",
        user=choice(users),
        league_id=1,
    )

    teams = [team1, team2, team3]
    db.session.add_all(teams)

    mahomes = Player(
        name="Patrick Mahomes",
        position="QB",
        nfl_team="Kansas City Chiefs",
        bye_week=10,
        fantasy_team_id=1,
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
    burrow = Player(
        name="Joe Burrow",
        position="QB",
        nfl_team="Cincinnati Bengals",
        bye_week=7,
        fantasy_team_id=2,
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
    jefferson = Player(
        name="Justin Jefferson",
        position="WR",
        nfl_team="Minnesota Vikings",
        bye_week=13,
        fantasy_team_id=3,
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
    players = [mahomes, burrow, jefferson]
    db.session.add_all(players)

    game1 = Game(team_1_id=1, team_2_id=2, team_1_score=0, team_2_score=0, winner_id=1)
    game2 = Game(team_1_id=2, team_2_id=3, team_1_score=0, team_2_score=0, winner_id=2)
    game3 = Game(team_1_id=1, team_2_id=3, team_1_score=0, team_2_score=0, winner_id=3)

    games = [game1, game2, game3]
    db.session.add_all(games)
    db.session.commit()
