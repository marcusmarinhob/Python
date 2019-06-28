# UDP Client ###################################################
# LANGUAGE: Python 3 (Python 3.7.3)
# DEVELOPER: Marcus Marinho
# GITHUB: https://github.com/marcusmarinhob
#################################################################

from socket import *

# Setup
serverName = 'hostname'
serverPort = 12000
clientSocket = socket(socket.AF_INET, socket.SOCK_DGRAM)

# Write a message
message = raw_input('Input lowercase sentence:')

# Send the message writen
clientSocket.sendto(message, (serverName, serverPort))

# Receive and and save the message read
modifiedMessage, serverAdress = clientSocket.recvfrom(2048)

# Show the modified message
print(modifiedMessage)

clientSocket.close()
