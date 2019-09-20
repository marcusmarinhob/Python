n = 5

while n > 0:
    print(n)
    n = n -1

print('Blastoff!')



# Auto git saving #####################################################
import os

fileName = os.path.basename(__file__)
commitMsg = "1. Added Auto git saving to the code" 

os.system("git add "+ fileName)
print('git commit -m '+'"'+commitMsg+'"')
os.system('git commit -m '+'"'+commitMsg+'"')
