import turtle
import math
import os
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title('game')
wn.setup(700,700)
wn.tracer(0)

#IMAGES 24*24px (placeholders)
#turtle.register_shape("circle")
#turtle.register_shape("bunny_left.gif")
#turtle.register_shape("carrot.gif")
#turtle.register_shape("grass.gif")


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color('white')
        self.penup()
        self.speed(-5)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color('blue')
        self.penup()
        self.speed(5)
        self.gold = 0
        
    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor()+24
        
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        
    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor()-24
        
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
    
    def go_left(self):
        self.shape("circle")
        move_to_x = player.xcor()-24
        move_to_y = player.ycor()
        
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_right(self):
        self.shape("circle")
        move_to_x = player.xcor()+24
        move_to_y = player.ycor()
        
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
            
    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a**2) + (b**2))
        
        if distance < 5:
            return True  
        else:
            return False
                 
class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("triangle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x,y)
    
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle
        

levels=[""]

level_1 = [
    
"XXXXXXXXXXXXXXXXXXXX     XXXX",
"X    X    X    X   X     X  ",
"X    X  XXX    T   X     X   ",
"X    X  X X        X   XXX   ",
"X    X  X X X  X   X     X   ",
"X   XX    X X  X   X     T   ",
"X   X     X X  X   X         ",
"    XXXX  XXX  X   XXXXXXX   ",
"    X  P       X    X        ",
"  X X     T    X  XXX        ",
"  XXX          X    X     T  ",
"  X    XXXXXX  X        XXXXX",
"         X     X        X   X",
"     T   X     X        X   X",
"X  X     X   XXXXXXXX   X   X",
"X  XXX   X          X   X   X",
"X    X   X    T             X",
"X    X   X             T    X",
"X    X   X   XXXX   X       X",
"XXXXXX   X   X      XXXXX   X",
"X    X   X   X          XX  X",
"X    XXX X   X          XX  X",
"X        X   X   XXXXXXXX   X",
"X        X   X      X       X",
"XXXXXXXXXXXXXX      X       X"

]

treasures = []

levels.append(level_1)

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x*24)
            screen_y = 288 - (y*24)
            
            if character =="X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x,screen_y))
                
            if character =="P":
                player.goto(screen_x, screen_y)
                
            if character == "T":
                treasures.append(Treasure(screen_x,screen_y))

pen = Pen()
player = Player()

walls = []

score = player.gold
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-350,310)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial",14, "normal"))
score_pen.hideturtle()

setup_maze(levels[1])

turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_down,"Down")
turtle.onkey(player.go_up,"Up")

wn.tracer(0)

while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            scorestring="Score: %s" %score
            print("Player Gold : {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)
    
    wn.update()