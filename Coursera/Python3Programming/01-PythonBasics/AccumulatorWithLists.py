import os
os.system('cls')

print('\n# BEGIN OF THE SCRIPT #############################################')

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

acro = ""

for word in sent.split():
    if not(word in stopwords):
        letters = word[0:2].upper()+'.'
        acro = acro + letters
        acro.strip()
        print(acro)

acro = acro[:-1]    
print(acro)


    





# Auto git saving #####################################################
save = 0
commitMsg = '1. The Accumulator Pattern with Lists' 

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
