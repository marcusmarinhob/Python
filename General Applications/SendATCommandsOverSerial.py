# GENERAL APPLICATIONS ###########################################
# PROBLEM: Send AT Commands Over Serial
# LANGUAGE: Python 3 (Python 3.4.3)
# DEVELOPER: Marcus Marinho
# GITHUB: https://github.com/marcusmarinhob
#################################################################

import time
import serial


# Configure the Serial settings
ser = serial.Serial(
	port='COM7',
	baudrate=9600,
	parity=serial.PARITY_ODD,
	stopbits=serial.STOPBITS_TWO,
	bytesize=serial.SEVENBITS
)


while 1 :
    # Get AT Command (implemmented after)
    ATCommand = 'AT+Test'

    # Send the characters under Serial Tx
    ser.write(str.encode(ATCommand+'\r\n'))
    out = ''
    
    # Wait one second before reading Serial Rx
    time.sleep(1)


    # Read characters received under Serial Rx
    while ser.inWaiting() > 0:
        out += ser.read(1)                
    if out != '':
        print( '>>' + out)
