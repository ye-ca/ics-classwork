team_a_points = 25
team_a_wins = 15

team_b_points = 20
team_b_wins = 16

if team_a_points > team_b_points:
    print("Team A wins!")
    team_a_wins += 1
elif team_b_points > team_a_points:
    print("Team B wins!")
    team_b_wins += 1
else:
    print("Tie.")

if team_a_wins > team_b_wins:
    print("Team A has more wins than Team B.")
if team_b_wins > team_a_wins:
    print("Team B has more wins than Team A.")
else:
    print("Both Teams A and B have the same number of wins.")


# 1. There is a bit of code that adds wins depending on how many points a team has, and it added a win to team A because it had more points, bringing team_a_wins from the initalized 15 to 16.  Which is equal to team B. 

# 2. elif means else if, you can chain them together . In this case, it ensures that there is only one thing outputted from that section of code. 

# 3. it shouldn't make a difference because the statement is false either way if  one is more than the other.  
