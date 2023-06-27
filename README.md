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

- GET all users
- GET user by id
- DELETE user by id
- GET, POST, and UPDATE their fantasy team
- GET all players
- GET player by id
- GET all games
- GET gamesd by id

---

## Entity Relationship Diagram

<img src="imgs/ERD.png" width=700>

## API Routes



=======
| **Name** | **API endpoint**   | **HTTP verb** | **Purpose**                                                                                                                                       |
|----------|--------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| RETRIEVE | /players           | **GET**       | [{...}, {...}, ...]                                                                                                                               |
| RETRIEVE | /players/:id       | **GET**       | {'id', 'name', 'position', 'nfl_team', 'bye-week','fantasy_team_id','week_1_points'....'week_14_points','playoff_points', 'championship_points' } |
| UPDATE   | /players/:id       | **PATCH**     | {'id', 'name', 'position', 'nfl_team', 'bye-week','fantasy_team_id','week_1_points'....'week_14_points','playoff_points', 'championship_points' } |
| RETRIEVE | /fantasy_teams     | **GET**       | [{...},{...}, ...]                                                                                                                                |
| CREATE   | /fantasy_teams     | **POST**      | {'id','team_name', 'league_id', 'user_id'}                                                                                                        |
| RETRIEVE | /fantasy_teams/:id | **GET**       | {'id','team_name', 'league_id', 'user_id'}                                                                                                        |
| UPDATE   | /fantasy_teams/:id | **PATCH**     | {'id','team_name', 'league_id', 'user_id'}                                                                                                        |
| RETRIEVE | /games             | **GET**       | {'id', 'team_1_id', 'team_2_id', 'team_1_score','team_2_score', 'winner_id'}                                                                      |
| UPDATE   | /games/:id         | **PATCH**     | {'id', 'team_1_id', 'team_2_id', 'team_1_score','team_2_score', 'winner_id'}                                                                      |
| RETRIEVE | /games/:id         | **GET**       | {'id', 'team_1_id', 'team_2_id', 'team_1_score','team_2_score', 'winner_id'}                                                                      |
| CREATE   | /games             | **POST**      | {'id', 'team_1_id', 'team_2_id', 'team_1_score','team_2_score', 'winner_id'}                                                                      |
| RETRIEVE | /users             | **GET**       | [{...}, {...}, ...]                                                                                                                               |
| RETRIEVE | /users/:id         | **GET**       | {'id', 'name', 'username'}                                                                                                                        |
| DELETE   | /users/:id         | **DELETE**    | {}                                                                                                                                                |

---
## Trello

<img src="imgs/Trello.png" width = 900>
