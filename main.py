#It doesn't matter which keys we use.


import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light yellow")
drawing_board.title("Turtle Python")

turtle_instance = turtle.Turtle()


#Search on Google for turtle's detection ->
#-> when the user presses the keys: turtle ->
#-> python detects keyboard on screen
#than Search: turtle python on key listen


'''
def turtle_forward():
    turtle_instance.forward(50)

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="f")

turtle.mainloop()
'''


'''
#Turning the turtle left and right at an angle:

def turtle_forward():
    turtle_instance.forward(50)

def rotate_angle_right():  #
    turtle_instance.right(50)  #

def rotate_angle_left():  #
    turtle_instance.left(50)  #

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="f")
drawing_board.onkey(fun=rotate_angle_right, key="Down")  #
drawing_board.onkey(fun=rotate_angle_left, key="Up")  #

turtle.mainloop()
'''


'''
#For precise direction, it is necessary to keep->
#-> the  angle small:

def turtle_forward():
    turtle_instance.forward(50)

def rotate_angle_right():
    turtle_instance.right(10)  #

def rotate_angle_left():
    turtle_instance.left(10)  #

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="f")
drawing_board.onkey(fun=rotate_angle_right, key="Down")
drawing_board.onkey(fun=rotate_angle_left, key="Up")

turtle.mainloop()
'''


'''
#Rotate turtle with current angle:

def turtle_forward():
    turtle_instance.forward(50)

def rotate_angle_right():
    turtle_instance.setheading(turtle_instance.heading()-10)  #
    #turtle_instance.right(10)

def rotate_angle_left():
    turtle_instance.setheading(turtle_instance.heading()+10)  #
    #turtle_instance.left(10)

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="f")
drawing_board.onkey(fun=rotate_angle_right, key="Down")
drawing_board.onkey(fun=rotate_angle_left, key="Up")

turtle.mainloop()
'''


'''
#Clear screen:

def turtle_forward():
    turtle_instance.forward(50)

def rotate_angle_right():
    turtle_instance.setheading(turtle_instance.heading()-10)

def rotate_angle_left():
    turtle_instance.setheading(turtle_instance.heading()+10)

def clear_screen():  #
    turtle_instance.clear()  #

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="f")
drawing_board.onkey(fun=rotate_angle_right, key="Down")
drawing_board.onkey(fun=rotate_angle_left, key="Up")
drawing_board.onkey(fun=clear_screen, key="c")  #

turtle.mainloop()
'''


'''
#Bring to the top by drawing:

def turtle_forward():
    turtle_instance.forward(50)

def rotate_angle_right():
    turtle_instance.setheading(turtle_instance.heading()-10)

def rotate_angle_left():
    turtle_instance.setheading(turtle_instance.heading()+10)

def clear_screen():
    turtle_instance.clear()

def turtle_return_home():  #
    turtle_instance.home()  #

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="f")
drawing_board.onkey(fun=rotate_angle_right, key="Down")
drawing_board.onkey(fun=rotate_angle_left, key="Up")
drawing_board.onkey(fun=clear_screen, key="c")
drawing_board.onkey(fun=turtle_return_home, key="h")  #

turtle.mainloop()
'''


'''
#Bring to the top without drawing:

def turtle_forward():
    turtle_instance.forward(50)

def rotate_angle_right():
    turtle_instance.setheading(turtle_instance.heading()-10)

def rotate_angle_left():
    turtle_instance.setheading(turtle_instance.heading()+10)

def clear_screen():
    turtle_instance.clear()

def turtle_return_home():
    turtle_instance.home()

def turtle_pen_up():  #
    turtle_instance.penup()  #

def turtle_pen_down():  #
    turtle_instance.pendown()  #

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="f")
drawing_board.onkey(fun=rotate_angle_right, key="Down")
drawing_board.onkey(fun=rotate_angle_left, key="Up")
drawing_board.onkey(fun=clear_screen, key="c")
drawing_board.onkey(fun=turtle_return_home, key="h")
drawing_board.onkey(fun=turtle_pen_up, key="u")  #
drawing_board.onkey(fun=turtle_pen_down, key="d")  #

turtle.mainloop()
'''


#Bring the pencil the top without lifting it ->
#-> and start drawing again without lowering ->
#-> the pencil:

def turtle_forward():
    turtle_instance.forward(50)

def rotate_angle_right():
    turtle_instance.setheading(turtle_instance.heading()-10)

def rotate_angle_left():
    turtle_instance.setheading(turtle_instance.heading()+10)

def clear_screen():
    turtle_instance.clear()

def turtle_return_home():
    turtle_instance.penup()  #
    turtle_instance.home()
    turtle_instance.pendown()  #

def turtle_pen_up():
    turtle_instance.penup()

def turtle_pen_down():
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="f")
drawing_board.onkey(fun=rotate_angle_right, key="Down")
drawing_board.onkey(fun=rotate_angle_left, key="Up")
drawing_board.onkey(fun=clear_screen, key="c")
drawing_board.onkey(fun=turtle_return_home, key="h")
drawing_board.onkey(fun=turtle_pen_up, key="u")
drawing_board.onkey(fun=turtle_pen_down, key="d")

turtle.mainloop()