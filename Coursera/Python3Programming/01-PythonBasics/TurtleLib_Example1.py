import os
os.system('cls')

print('\n# BEGIN OF THE SCRIPT #############################################')

import turtle           # Allow us to use the turtles library
wn = turtle.Screen()    # Creates a graphics window
wn.bgcolor(0.0, 0.50, 1.0)

alex = turtle.Turtle()  # Creates a turtle named alex
alex.pensize(10)
alex.color(1.0, 1.0, 1.0)

alex.forward(150)      
alex.left(90)           
alex.forward(300)       
alex.left(90)           
alex.forward(300)      
alex.left(90)           
alex.forward(300)       
alex.left(90)
alex.forward(150)

mike = turtle.Turtle() # Creates a turtle named mike

mike.pensize(10)
mike.color(0.0, 0.0, 0.0)

mike.forward(150)      
mike.right(90)           
mike.forward(300)       
mike.right(90)           
mike.forward(300)      
mike.right(90)           
mike.forward(300)       
mike.right(90)
mike.forward(150)
wn.exitonclick()  

# Auto git saving #####################################################
save = 1
commitMsg = '1. Turtle Lib - Creating tow squares, changing background color, pencil size and color.' 

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
