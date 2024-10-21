import random
import turtle
import time

# screen setup
screen = turtle.Screen()
screen.bgcolor("green")

# player 1 setup 
player_one = turtle.Turtle()
# colour
player_one.color("red")
# shape
player_one.shape("square")

# player 2 setup
player_two = player_one.clone()
# colour
player_two.color("blue")

# position
player_one.penup()
player_one.goto( -300, 200)
player_two.penup()
player_two.goto( -300, -200)

# finish line
player_one.goto( 300, -250)
player_one.pendown()
player_one.color("black")
player_one.goto( 300, 250)

# reset player 1 pos
player_one.penup()
player_one.goto(-300, 200)
player_one.color("red")

# loop to continue after a game
winings = 10
loop = 1
while loop == 1:
	# betting 
	print("You have ",winings,"chips")
	bet = input("do you want to bet on red (1) or blue (2)?")
	if bet == 1:
		print("You have bet on player one! Good luck!")
	elif bet == 2:
		print("You have bet on player two! Good luck")

# win variables
	p1_win = 0
	p2_win = 0
	Draw = False



# die and win conditions 
	die = [1, 2, 3, 4, 5, 6]

	for i in range(30):
		if player_one.pos() >= ( 300, -250) and player_two.pos() >= ( 300, -250):
			Draw=True
		elif player_one.pos() >= ( 300, -250):
			print("player one (red) wins!")
			p1_win = 1
			break
		elif player_two.pos() >= ( 300, -250):
			print("player two (blue) wins!")
			p2_win = 1
			break
		else:
			die_roll = random.choice(die)
			player_one.forward(30*die_roll)
			time.sleep(1)
			die_roll2 = random.choice(die)
			player_two.forward(30*die_roll2)
			time.sleep(1)

# position reset
	player_one.penup()
	player_one.goto( -300, 200)
	player_two.penup()
	player_two.goto( -300, -200)

# betting wins 

	if Draw==True:
		print("it is as draw! You still lose money lol.")
		winings=winings/3
		winings=winings*2
	elif bet == "1" and p1_win == 1:
		winings = winings * 2
		print("congrats you won!")
		p1_win = 0
	elif bet == "2" and p2_win == 1:
		winings = winings * 2
		print("congrats you won!")
		p2_win = 0
	else: 
		winings = winings / 2
		print("sorry you lost!")
	bet = 0
	if winings == 0:
		print("you are broke")
		loop = 0
else:
	print("You lost!")
turtle.done()
