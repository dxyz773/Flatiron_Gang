# Flatiron Gang NFL Lover

#### Indulge in your NFL obsession with 🏈 Flatiron Gang NFL Lover! Sign up with us and let the NFL fun begin! Be the 🏆 champion of your Fantasy football league by searching our NFL player data base and liking your favorite NFL players. You'll be ahead of the game and ready for that much anticipated Fantasy Football Draft.

---

## Wireframes

---

## User Stories

A Users can:

- Signup for a user account on Flatiron Gang NFL Lover App
- Login to user account
- Search through a database of NFL players by player name and see the player's information.
- Like their favorite NFL players
- update name on user account
- Logout of user account

---

## React Tree

## <img src="imgs/react_tree.png" width=600>

## Client Side Routes

| **Client Route** | **Component** |
| ---------------- | ------------- |
| /                | Home.js       |
| /account         | Account.js    |
| /mylikes         | MyLikes.js    |
| /players         | AllPlayers.js |
| /players/:id     | Player.js     |
| /auth            | Auth.js       |

---

## Entity Relationship Diagram

<img src="imgs/ERD.png" width=600>

---

## API Routes

| **Name** | **API endpoint**   | **HTTP verb** | **Purpose**                                                                                                                                       |
| -------- | ------------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
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
