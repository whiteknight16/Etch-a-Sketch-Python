from turtle import Turtle,Screen

def move_forward():
    t.fd(20)

def move_backward():
    t.bk(20)

def turn_left():
    t.left(20)

def turn_right():
    t.right(20)

def clear_screen():
    t.clear()


t=Turtle()
screen=Screen()

screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear_screen,"c")









screen.exitonclick()