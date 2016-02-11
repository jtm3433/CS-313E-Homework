#  File: USFlag.py
#  Description: Uses flag graphics to draw the US flag
#  Student's Name: John Mitchell
#  Student's UT EID: jtm3433
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 2/10/2016
#  Date Last Modified: 2/10/2016

import turtle, math

#function that draws a white star, taking in the turtle, x coordinate (middle), y coordinate (middle) and desired diameter of said star
def drawWhiteStars(ttl, x, y, diameter):

     # calculate length of star side using diameter
    length = diameter * math.cos(16*math.pi/180)

    # since the coordinates given were in the middle of the star, move turtle to the outside of the diameter
    ttl.sety(y+diameter/2)

    # begin drawing
    ttl.pendown()
    ttl.begin_fill()   

    # create sides of star
    for i in range(5):
        ttl.right(144)
        ttl.forward(length)

    # fill in star and return turtle to original coordinates
    ttl.end_fill()
    ttl.penup()
    ttl.setx(x)
    ttl.sety(y)
        

def main():

    # populate variables for different flag components using government guidelines
    # hoist (height)
    a = int(input("Enter hoist: "))
    # width
    b = 1.9 * a
    # canton height
    c = (7/13) * a
    # canton width
    d = (2/5) * b
    # height difference for stars
    e = c / 10
    # width difference for stars
    g = d / 12
    # height of stripe
    l = a / 13
    # diameter of star
    k = (4/5) * l

    # set up window and move turtle object to starting position
    turtle.title("US Flag")
    turtle.bgcolor("#d3d3d3")
    turtle.setup(width = (b +200), height = (a +200))
    flag = turtle.Turtle()
    flag.penup()
    flag.setx(-b/2)
    flag.sety(a/2)
    flag.speed(0)
    

    # create canton
    flag.color("#002664")
    flag.pendown()
    flag.begin_fill()
    for i in range(2):
        flag.forward(d)
        flag.right(90)
        flag.forward(c)
        flag.right(90)    
    flag.end_fill()
    flag.forward(d)

    # create narrow stripes    
    for i in range(7):

        # this code is ugly - however, its function is to detect whether the turtle is currently red
        if flag.color() == ((0.7333333333333333, 0.07450980392156863, 0.24313725490196078), (0.7333333333333333, 0.07450980392156863, 0.24313725490196078)):
        # switch to red if white and vice versa
            flag.color("#FFFFFF")
        else:
            flag.color("#BB133E")

        # begin drawing the stripe
        flag.begin_fill()
        for i in range(2):
            flag.forward(b - d)
            flag.right(90)
            flag.forward(l)
            flag.right(90)
        flag.end_fill()
        flag.right(90)
        flag.forward(l)
        flag.left(90)

    # create wide stripes
    flag.setx(-b/2)
    for i in range(6):
        
        # this code is ugly - however, its function is to detect whether the turtle is currently red
        if flag.color() == ((0.7333333333333333, 0.07450980392156863, 0.24313725490196078), (0.7333333333333333, 0.07450980392156863, 0.24313725490196078)):
        # switch to red if white and vice versa
            flag.color("#FFFFFF")
        else:
            flag.color("#BB133E")

        # begin drawing the stripe
        flag.begin_fill()
        for i in range(2):
            flag.forward(b)
            flag.right(90)
            flag.forward(l)
            flag.right(90)
        flag.end_fill()
        flag.right(90)
        flag.forward(l)
        flag.left(90)

    # prepare to create stars by moving turtle, setting colors and pointing turtle in correct direction
    flag.penup()
    flag.setx(-b/2+g)
    flag.sety(a/2-e)
    stars = 6
    flag.color("#FFFFFF")
    flag.right(288)

    # run loop nine times for nine rows
    for i in range(9):

        # loop to create each row of stars
        for i in range(stars):
            drawWhiteStars(flag, flag.xcor(), flag.ycor(), k)
            flag.setx(flag.xcor()+2*g)

        # move turtle down to next row
        flag.sety(flag.ycor()- e)

        # determine how many stars go into the next row and set starting x accordingly
        if stars == 6:
            stars = 5
            flag.setx(-b/2+2*g)
        else:
            stars = 6
            flag.setx(-b/2+g)

main()
