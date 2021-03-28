import turtle
my_window = turtle.Screen()
my_window.bgcolor("white")
arrow = turtle.Turtle()
def Gallows():
    
    arrow.forward(100)
    arrow.back(50)
    arrow.left(90)
    arrow.forward(200)
    arrow.left(90)
    arrow.forward(100)
    arrow.left(90)
    arrow.forward(50)

Gallows()
print("Welcome to the Hangman Game!")
String = 'the hidden string'
def loop():
    Char = input("Enter a character:")
    for i in String:
        if (Char == i):
            loop()
            continue
        else:
            draw()   
num = 0               
def draw():
    global num
    num = num+1
    if (num == 1):
        arrow.right(60)
        turtle.circle(10)
    elif (num == 2):
        arrow.forward(30)
    elif(num == 3):
        arrow.left(120)
        arrow.forward(30)
        arrow.left(180)
        arrow.forward(30)
    elif(num == 4):
        arrow.right(60)
        arrow.forward(30)
        arrow.right(180)
        arrow.forward(30)
    elif(num == 5):
        arrow.right(30)
        arrow.forward(30)
        arrow.right(120)
        arrow.forward(30)
        arrow.right(180)
        arrow.forward(30)  
    elif(num == 6):
        arrow.left(30)
        arrow.forward(30)
    elif(num == 7):
        print("Oh no, You have lost the game\n")
        play = input( "Want to play again?")
        if (play == 'y'):
            loop()
        else:
            print("Thanks for playing, Bye")                  
loop()
