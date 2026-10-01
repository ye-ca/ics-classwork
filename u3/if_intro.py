robot_location = 47
ball_location = 39
goal_location = 29
have_ball = False

if robot_location < ball_location:
	print("Almost at the ball")

if robot_location > goal_location:
	print("You are beyond the goal.")

if robot_location == goal_location:
	print("The robot is at the goal.")

robot_location -= 8
print("Moving back 8")

if robot_location == goal_location:
	print("At the goal.")

if robot_location == ball_location:
	print("At the ball")
	print("Picking up the ball.")
	have_ball = True
	print("Now make your way to the goal.")

robot_location -= 10
print("Moving back 10")

if robot_location < goal_location:
	print("You went too far.")

if robot_location == goal_location and have_ball is True:
	print("You reached the goal and scored!")
	have_ball = False

# 1. The if sets a conditional for the code under it to run, if the condition in the if statement is true, then the code runs. 

# 2. The purpose for indenting code in an if statement is to show that this code runs in this if branch, otherwise it would just run regardless if the if statement is true or false. 

# 3. ok 

# 4. +=  means add to the variable, for example x = x + 1 is equivalent to x += 1, and the same but inverted for -=
