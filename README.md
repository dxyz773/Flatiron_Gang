# Flatiron_Gang

### Explore the ultimate fantasy football management experience with our app, where you can draft, strategize, and build the team of your dreams to compete in leagues with family & friends for the right to call yourself a CHAMPION



| **Name** | **API endpoint**   | **HTTP verb** | **Purpose**                                                |
|----------|--------------------|---------------|------------------------------------------------------------|
| RETRIEVE | /players           | **GET**       | [{...}, {...}, ...]                                        |
| RETRIEVE | /players/:id       | **GET**       | {'id', 'name', 'position', 'nfl_team', 'bye-week','stats'} |
| DELETE   | /players/:id       | **DELETE**    | {}                                                         |
| RETRIEVE | /fantasy_teams     | **GET**       | [{...},{...}, ...]                                         |
| CREATE   | /fantasy_teams     | **POST**      | {'id','team_name', 'player_id', 'league_id', 'user_id'}    |
| RETRIEVE | /fantasy_teams/:id | **GET**       | {'id','team_name', 'player_id', 'league_id', 'user_id'}    |
| UPDATE   | /fantasy_teams/:id | **PATCH**     | {'id','team_name', 'player_id', 'league_id', 'user_id'}    |
| RETRIEVE | /users             | **GET**       | [{...}, {...}, ...]                                        |
| RETRIEVE | /users/:id         | **GET**       | {'id', 'name', 'username'}                                 |