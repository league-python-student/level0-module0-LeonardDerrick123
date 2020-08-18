import random
import turtle

# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================

def screenClicked(x, y):
    print('You pressed: x=' + str(x) + ', y=' + str(y))
    
    # 6. Call the turtle .penup() method
    D5.penup()
    # 7. Move the turtle to a new location using .goto(x, y)
    D5.goto(x,y)
def turtleClicked(x, y):
    print('turtle clicked!')
    
    # 8. Make a for loop to run the next instructions 3 times
        
        # 9. Make the turtle spin 360 degrees using the .right() method
    for i in range(3):
        D5.right(360)
        # 10. Use the .color() method and getRandomColor() function to change
    D5.color(getRandomColor())
        # the color of the turtle,



if __name__ == '__main__':
    window = turtle.Screen()
    window.setup(width=0.75, height=0.8, startx=0, starty=0)
    
    # 1. Make a new turtle
    D5 = turtle.Turtle()
    # 2. Make your turtle's shape 'turtle', .shape('turtle')
    D5.shape('triangle')
    # 3. Set your turtle's color using .color('green') and .pencolor('blue')
    D5.color('green')
    D5.pencolor('dark green')
    # 4. Set and new width, length, and outline of our turtle
    D5.turtlesize(stretch_wid=10, stretch_len=10, outline=4)

    # 5. Uncomment the following line and replace 'myTurtle' with your turtle
    D5.onclick(turtleClicked)

# ===================== DO NOT EDIT THE CODE BELOW ============================
    window.onclick(screenClicked)
    turtle.done()
