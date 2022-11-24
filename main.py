import random as ran
import turtle as t

t.bgcolor('yellow')
caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

leaf = t.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('cicle',leaf_shape)
leaf.shape('circle')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)
game_started = False
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start',align='center',\
    font=('Arial',16,'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed()

def outside_window():
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    (x,y) = caterpillar.pos()
    outside = \
        x <left_wall or \
            x>right_wall or \
                y < bottom_wall or \
                    y > top_wall
    return outside


def game_over():
    caterpillar.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER!',align='center',font=('Arial',30,'normal'))

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width()/ 2) - 50
    y = (t.window_height() / 2) - 50
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score),align='right',font=('Arial',40,'bold'))

def place_leaf():
    leaf.ht()
    leaf.setx(ran.randint(-200,200))
    leaf.sety(ran.randint(-200,200))
    leaf.st()

def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    score = 0
    text_turtle.clear()

    caterpillar_speed = 1
    caterpillar_length = 3
    caterpillar.shapesize(1,caterpillar_length,1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()
    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf)<20:
            place_leaf()
            caterpillar_length += 1
            caterpillar.shapesize(1,caterpillar_length,1)
            caterpillar_speed += 1
            score += 1
            display_score(score)
        if outside_window():
            game_over()
            break
def mov_up():
    caterpillar.setheading(90)
def mov_down():
    caterpillar.setheading(270)
def mov_right():
    caterpillar.setheading(0)
def mov_left():
    
    caterpillar.setheading(180)
t.onkey(start_game,'space')
t.onkey(mov_up,'Up')
t.onkey(mov_down,'Down')
t.onkey(mov_right,'Right')
t.onkey(mov_left,'Left')
t.listen()
t.mainloop()
