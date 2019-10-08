import os
os.system('cls')

print('\n# BEGIN OF THE SCRIPT #############################################')

str_seconds = input("Please enter the number of seconds you wish to convert: ")
total_secs = int(str_seconds)

hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes = secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining % 60

print("Hrs= ", hours, "mins=", minutes, "secs=", secs_finally_remaining)


# Auto git saving #####################################################
save = 1
commitMsg = '1. Seconds conversion.' 

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
