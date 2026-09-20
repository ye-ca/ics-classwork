# storing the team name in a string  
team = "Toronto Blue Jays"
# storing the current date in a string  
current_date = "July 18, 2021"
# storing the player's name in a string 
player = "Vladimir Guerrero Jr."
# storing the number of home runs hit to date in an intager
home_runs_to_date = 31
# storing the number of games played so far in an intager
games_played = 88
# storing the total number of games in a full season in an intager
total_season_games = 162
# storing the current MLB record for most home runs in a season
home_run_record = 73

# the point of this empty line is to seperate the data from the calculations 

# calculating the remaining games by subtracting games played from total season games and storing in games_remaining
games_remaining = total_season_games - games_played
# calculating the average home runs per game by dividing home runs to date by games played and storing in home_runs_per_game
home_runs_per_game = home_runs_to_date / games_played
# calculating the projected total home runs by multiplying the average per game by total season games and storing in projected_home_runs
projected_home_runs = home_runs_per_game * total_season_games
# calculating whether the projected total exceeds the record (true/false) and storing in can_break_record
can_break_record = projected_home_runs > home_run_record

# the point of this space is to seperate the calculations from the output

print(f"{player} of the {team}")
print(f"currently has {home_runs_to_date} home runs as of {current_date}.")
print(f"the current mlb record for most home runs in a season is {home_run_record}.")
print(f"with {round(games_remaining)} games remaining and an average of {round(home_runs_per_game, 2)} home runs per game,")
print(f"it is {can_break_record} that he is on pace to break the record.")
print(f"{player} is projected to hit {round(projected_home_runs)} home runs this season.")

# games_remaining is correct by definition (total - played = remaining) regardless of what the actual numbers are
