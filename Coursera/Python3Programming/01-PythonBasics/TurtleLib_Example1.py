import os
os.system('cls')

print('\n# BEGIN OF THE SCRIPT #############################################')

import turtle           # Allow us to use the turtles library
wn = turtle.Screen()    # Creates a graphics window
wn.bgcolor(0.0, 0.50, 1.0)

elan = turtle.Turtle()
elan.pensize(100)
elan.color(1.0, 0.5, 0.0)
elan.shape("turtle")

elan.up()

# distance = 50
# for _ in range(10):
#     elan.stamp()
#     elan.forward(distance)
#     elan.right(90)
#     distance = distance + 20

# elan.left(90)
# elan.forward(100)

# elan.color(1.0, 1.0, 1.0)


radio = 0.5
for index in range(100):
    elan.stamp()
    elan.forward(radio)
    elan.left(15)
    radio = radio + 0.5

wn.exitonclick()



# Auto git saving #####################################################
save = 0
commitMsg = '1. Turtle Lib - Creating spirals' 

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
