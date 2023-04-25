import os
import turtle

# Get the absolute path to the image file
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgpic("background_image_1.png")

# create the turtle for drawing the buttons
button_turtle = turtle.Turtle()
button_turtle.penup()
button_turtle.hideturtle()

# create the Start button
button_turtle.goto(0, 0)
button_turtle.color("white")
button_turtle.fillcolor("gray")
button_turtle.begin_fill()
button_turtle.goto(-100,50)
button_turtle.pendown()
button_turtle.goto(100,50)
button_turtle.goto(100,-50)
button_turtle.goto(-100,-50)
button_turtle.goto(-100,50)
button_turtle.end_fill()
button_turtle.penup()
button_turtle.goto(0, -10)  # move the button up by 35 pixels
button_turtle.write("Start", align="center", font=("Arial", 20, "normal"), move=True)
button_turtle.goto(-100, 0)



# create the Quit button
button_turtle.goto(-350, -250)
button_turtle.color("white")
button_turtle.fillcolor("gray")
button_turtle.begin_fill()
button_turtle.goto(-275, -250)
button_turtle.pendown()
button_turtle.goto(-275, -200)
button_turtle.goto(-350, -200)
button_turtle.goto(-350, -250)
button_turtle.goto(-275, -250)
button_turtle.end_fill()
button_turtle.penup()
button_turtle.goto(-330, -235)  # move turtle to center of button
button_turtle.write("Quit", align="left", font=("Arial", 14, "normal"))

# function to quit the game
def quit_game(x, y):
    turtle.bye()

# function to handle the Start button click
def next_page(x, y):
    # Remove existing buttons
    button_turtle.clear()

    # Create new buttons for the next page
    next_page_btn = turtle.Turtle()
    next_page_btn.shape("square")
    next_page_btn.color("white")
    next_page_btn.penup()
    next_page_btn.goto(100,250)
    next_page_btn.write("Next Page", align="center", font=("Arial", 20, "normal"), move=True)

    quit_btn = turtle.Turtle()
    quit_btn.shape("square")
    quit_btn.color("white")
    quit_btn.penup()
    quit_btn.goto(-280, -180)
    quit_btn.write("Quit", align="left", font=("Arial", 16, "normal"))

    # Set up event listeners for buttons
    next_page_btn.onclick(next_page)
    quit_btn.onclick(quit_game)

    # Set up event listener for quit button
    quit_btn.onclick(quit_game)


# Set up event listener for start button
screen.onclick(next_page)
screen.onclick(quit_game)

turtle.done()
turtle.mainloop()