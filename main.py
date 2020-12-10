import turtle
import math
import winsound
import time

#on met en place l'écran sur lequel on va dessiner
wn = turtle.Screen()
wn.bgcolor("black")
wn.title('g̵̨̤̳͈̲̜͍͕̖̫̝̟̗̃̈̇́̄͐͗̓̍͗̈́̓͐̿̔̃́͐̊͗̔͋́͗̚̕͜͝͠a̵̧̧̛͈̝̠̩͇̠͚͔͔͖̖̬̪̭͓̳̟̻̞̭̻̙̾͂̎̀͗̓́͑̈́̔̈́͊̎̓̌̅̄͆̏̓́̆͗̀̈́͒̂̀̌̂͘̕͘̕͜͜͠ͅͅm̶̨̛̼͈͔̱̦̳͈͙̗̰̙̪͖̼̬̖̗̲͓͖̣͉̓͗̉̀̈̿̽͋̓̀̉̏͌́̿̓͂́͗̓͋́̏̄̓̋͜͠ͅȩ̴̧̢̹̯̥̤̳͇̥̪͉̫̺͖̹̺̣͕̠͈͇̯̤̘͙̜̩͎͍̥̮͉̞̞̎̒̽͐̃̀̓͑͑̈́̔̽͘̕̚͜ͅ')
wn.bgpic("BG2.gif")
wn.tracer(0)
wn.setup(700,700)

#Pen
class Pen(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape('square')
		self.color("#4F0505")
		self.penup()
		self.speed(0)

#on définit le joueur
class Player(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("circle")
		self.color('blue')
		self.penup()
		self.speed(0)
		self.gold = 0

	#on définit les déplacements possibles du joueurs. 24 est la taille d'une case
	def go_up(self):
		#on calcule les coordonnéees où on va aller
		move_to_x = player.xcor()
		move_to_y = player.ycor() + 24

		#On vérifie qu'on ne vas pas dans un mur
		if(move_to_x, move_to_y) not in walls:
			self.goto(move_to_x,move_to_y)

	def go_down(self):
		#on calcule les coordonnéees où on va aller
		move_to_x = player.xcor()
		move_to_y = player.ycor() - 24

		#On vérifie qu'on ne vas pas dans un mur
		if(move_to_x, move_to_y) not in walls:
			self.goto(move_to_x,move_to_y)

	def go_left(self):
		#on calcule les coordonnéees où on va aller
		move_to_x = player.xcor() - 24
		move_to_y = player.ycor() 

		#On vérifie qu'on ne vas pas dans un mur
		if(move_to_x, move_to_y) not in walls:
			self.goto(move_to_x,move_to_y)

	def go_right(self):
		#on calcule les coordonnéees où on va aller
		move_to_x = player.xcor() + 24
		move_to_y = player.ycor() 

		#On vérifie qu'on ne vas pas dans un mur
		if(move_to_x, move_to_y) not in walls:
			self.goto(move_to_x,move_to_y)

	#On crée les collisions avec les collectibles
	def is_collision(self, other):
		a = self.xcor()-other.xcor()
		b = self.ycor()-other.ycor()
		distance = math.sqrt((a**2)+(b**2))

		if distance < 5:
			return True
		else:
			return False


#On crée les trésors collectibles
class Treasure(turtle.Turtle):
	def __init__(self, x,y):
		turtle.Turtle.__init__(self)
		self.shape("triangle")
		self.color('gold')
		self.penup()
		self.speed(0)
		self.gold = 100
		self.goto(x,y)

	def destroy(self):
		self.goto(2000,2000)
		self.hideturtle()


#level list
levels = [""]

#level 1
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP        X    X   X X  X",
"X X  X   XXX   T   X X  X",
"X    X  X X    X T   X XX",
"XXXXXX  XXXXX  X   X T  X",
"XT  X   XXXXX  X   X   XX",
"XXX     XXXXXT XXX X    X",
"X   XXXX  XXX  X T XXXXXX",
"X      X    X  X    XXXXX",
"X   XXXX  XXX  X  XXX XXX",
"X  XX   T      X  T X   X",
"X XX   XXXXXXXXX      X X",
"X        X T   XXXXXXXX X",
"XXXXXXXX X     XT       X",
"X   T    X   XXXXX XXXXXX",
"X  XXX X     X  X   X   X",
"X    X XXXXX X  XX    T X",
"XXX  X X   X X    T XXXXX",
"X    X X XXX XXXXX  XXXXX",
"XXXXXX   X   X   X  XXXXX",
"XTX  X   X T X X X   T  X",
"X X  XXX X   X X XXX    X",
"X XX   X X T X X   T XXXX",
"X  T     X     XX       X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

#On fait une liste des trésors
treasures = []

#on intègre level 1 à la liste levels
levels.append(level_1)


def setup_maze(level):
	for y in range(len(level)):
		for x in range(len(level[y])):
			#On relève et note les coordonnées du character 
			character = level[y][x]
			#calculer les coordonnées sur l'écran
			screen_x = -288 +(x*24)
			screen_y = 288 - (y*24)
			#ici, on définit quelle lettre dans la carte définit un mur, un bonus ou le joueur
			if character == "X":
				pen.goto(screen_x,screen_y)
				pen.stamp()
				#on entre les coordonnées des murs dans la liste
				walls.append((screen_x, screen_y))

			if character == "P":
				player.goto(screen_x,screen_y)

			if character == "T":
				treasures.append(Treasure(screen_x, screen_y))

#On fait appel aux class créées plus tôt
pen = Pen()
player = Player()

#on crée la liste contenant les murs
walls = []

#setup
setup_maze(levels[1])
 
#On définit les déplacements du joueur en fonction de la touche pressée, on peut remplacer 'Left' etc par des lettres
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

time_limit = 45
start_time = time.time()


score = player.gold
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("red")
score_pen.penup()
score_pen.setposition(-330,310)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial",14, "normal"))
score_pen.hideturtle()

timer = 45
time_pen = turtle.Turtle()
time_pen.speed(0)
time_pen.color("red")
time_pen.penup()
time_pen.setposition(-120,310)
scorestring = "Time: %s" %timer
time_pen.write(scorestring, False, align="left", font=("Arial",14, "normal"))
time_pen.hideturtle()


#main loop
while True:
	for treasure in treasures:
		if player.is_collision(treasure):
			score_pen.clear()
			player.gold += treasure.gold
			score = player.gold
			score_pen.write("Score: {}".format(score), align="center", font=("Arial",14, "normal"))
			treasure.destroy()
			winsound.PlaySound('treasure.wav', winsound.SND_FILENAME)
			treasures.remove(treasure)

		if treasures==[]:
			print("Victory !")
			winsound.PlaySound('victory.wav', winsound.SND_FILENAME)
			exit()
			

	time_pen.clear()
	elapsed_time = time.time() - start_time
	timer = time_limit - elapsed_time
	time_pen.write("Time: {}".format(timer), align="center", font=("Arial",14, "normal"))
	print(time_limit - int(elapsed_time))

	if elapsed_time > time_limit:
		print("GAME OVER")
		player.goto(2000,2000)
		treasure.goto(2000,2000)
		wn.bgpic("gameover.gif")

	else:
		start_time = time.time() - elapsed_time

	wn.update()
