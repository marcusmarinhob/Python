import os
os.system('cls')

print('\n# BEGIN OF THE SCRIPT #############################################')

import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""

    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()      # Set up the window and its attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()    # create alex
drawSquare(alex, 50)      # Call the function to draw the square passing the actual turtle and the actual side size

wn.exitonclick()


# Auto git saving #####################################################
save = 1
commitMsg = '1. Functions - drawSquare' 

if save:
    print('\nAUTO GIT SAVING...')
    
    fileName = os.path.basename(__file__)    

    os.system('git add '+ fileName)
    os.system('git commit -m '+'"'+commitMsg+'"')
    os.system('git push')

    print('\nFile Name: '+fileName)
    print('\nCommit Message: '+commitMsg)
    print('\nSAVED AND PUSHED!')


print('\n# END OF THE SCRIPT ###############################################')
#print('\n'*15)
