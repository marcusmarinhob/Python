import os
os.system('cls')

print('\n# BEGIN OF THE SCRIPT #############################################')

import turtle           # Allow us to use the turtles library
wn = turtle.Screen()    # Creates a graphics window
alex = turtle.Turtle()  # Creates a turtle named alex
alex.forward(150)       # Tell alex to move foward by 150 units
alex.left(90)           # Turn by 90 degrees
alex.forward(75)        # Complete the second side of a rectangle
alex.left(90)           # Turn by 90 degrees
alex.forward(150)       # Tell alex to move foward by 150 units
alex.left(90)           # Turn by 90 degrees
alex.forward(75)        # Complete the rectangle
wn.exitonclick()        # wait for a user click on the canvas

# Auto git saving #####################################################
save = 1
commitMsg = '1. Turtle Lib - Creating a rectangle using Turtle Library.' 

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
print('\n'*3)
