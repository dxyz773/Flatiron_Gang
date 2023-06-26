# Flatiron Gang

#### Explore the ultimate fantasy football management experience with our app, where you can draft, strategize, and build the team of your dreams to compete in leagues with family & friends for the right to call yourself a CHAMPION

---

## Wireframes

<img src="imgs/Homepage.png" width=600>
<img src="imgs/Fantasy Dashboard.png" width=600>
<img src="imgs/Users Players .png" width=600>

---

## User Stories

Users should:

Create and personalize my fantasy football team by selecting players from a variety of teams and positions.

Have a user-friendly interface that allows me to readily navigate through the app's various sections, such as team management, league standings, and player statistics.

Access a comprehensive player database containing detailed player profiles, historical performance data, and expert analysis to facilitate strategic decision-making.

Participate in weekly matches
Compete against other teams in League

Receive alerts and updates regarding player injuries, lineup changes.

A User can:

- GET all players info
- GET individual player info
- POST and DELETE a Player from Team
- Like a Player to put in personalized player list (queue)
- UPDATE usersname and name
- GET all user Leagues
- GET all user Teams
- POST new fantsay League or Team
- UPDATE team name or league name

---

## Entity Relationship Diagram

# <img src="imgs/Entity Relationship Diagram.png" width=600 height=500>

---

## API Routes

| **Name** | **API endpoint**   | **HTTP verb** | **Purpose**                                                |
| -------- | ------------------ | ------------- | ---------------------------------------------------------- |
| RETRIEVE | /players           | **GET**       | [{...}, {...}, ...]                                        |
| RETRIEVE | /players/:id       | **GET**       | {'id', 'name', 'position', 'nfl_team', 'bye-week','stats'} |
| DELETE   | /players/:id       | **DELETE**    | {}                                                         |
| RETRIEVE | /fantasy_teams     | **GET**       | [{...},{...}, ...]                                         |
| CREATE   | /fantasy_teams     | **POST**      | {'id','team_name', 'player_id', 'league_id', 'user_id'}    |
| RETRIEVE | /fantasy_teams/:id | **GET**       | {'id','team_name', 'player_id', 'league_id', 'user_id'}    |
| UPDATE   | /fantasy_teams/:id | **PATCH**     | {'id','team_name', 'player_id', 'league_id', 'user_id'}    |
| RETRIEVE | /users             | **GET**       | [{...}, {...}, ...]                                        |
| RETRIEVE | /users/:id         | **GET**       | {'id', 'name', 'username'}                                 |
