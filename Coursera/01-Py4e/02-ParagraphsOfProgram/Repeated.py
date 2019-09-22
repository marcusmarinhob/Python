n = 5

while n > 0:
    print(n)
    n = n -1

print('Blastoff!')



# Auto git saving #####################################################
save = 1
commitMsg = '1. Testing git saving' 

if save:
    import os

    fileName = os.path.basename(__file__)    

    os.system('git add '+ fileName)
    os.system('git commit -m '+'"'+commitMsg+'"')
    os.system('git push')
