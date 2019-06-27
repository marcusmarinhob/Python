# URI ONLINE JUDGE ##############################################
# PROBLEM: 1026 - To Carry or not to Carry
# LANGUAGE: Python 3 (Python 3.4.3)
# DEVELOPER: Marcus Marinho
# GITHUB: https://github.com/marcusmarinhob
#################################################################


while True:
  try:
    X, Y = input().split() 
    x = int(X)
    y = int(Y)
    
    output = x ^ y
    print(output)
  except EOFError:
    break
    
    