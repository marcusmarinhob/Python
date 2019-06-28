# TCP Server ###################################################
# LANGUAGE: Python 3 (Python 3.7.3)
# DEVELOPER: Marcus Marinho
# GITHUB: https://github.com/marcusmarinhob
#################################################################


from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((’’,serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()
