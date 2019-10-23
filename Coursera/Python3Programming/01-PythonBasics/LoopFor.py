import os
os.system('cls')

print('\n# BEGIN OF THE SCRIPT #############################################')

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# Write your code here.
words = sentence.split()

same_letter_count = 0
for i in range (0, len(words)):
    for j in range (0, len(words)):
        if ( i != j ):
            if ( (words[i][0] == words[j][0]) and (words[i][-1] == words[j][-1]) ):
                print(words[i][0])
                same_letter_count += 1



# Auto git saving #####################################################
save = 0
commitMsg = '1. Loop for - Two loops.' 

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
