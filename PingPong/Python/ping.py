'''
Created on Mar 28, 2020

@author: HOLVOET
'''

import logging
 
from Arduino.arduino import Arduino

from string import ascii_lowercase, ascii_uppercase, digits

def ping(serial, cmd):
    assert serial is not None
    # Sends the command to Arduino
    serial.write(bytes(cmd, 'utf-8'))
    
    response=bytearray()
    oneChar=serial.read()  # Read one
    while oneChar != b'\0':
        response.extend(oneChar)
        oneChar=serial.read()
    
    expectedResponse=bytearray("Got Command:<" + cmd + ">", 'utf-8')
    # response better be EQUAL to expectedResponse
    # otherwise Arduino is not in its right mind 
    info= "{" + response.decode('utf-8') + "}" + \
        " shoud be equal to " + \
        "{" + expectedResponse.decode('utf-8') + "}"
    logging.info(info)
    assert response == expectedResponse
 
arduino=Arduino("/dev/ttyACM0", True)

if arduino.serial != None:
    for c in ascii_lowercase:
        ping(arduino.serial, c)
    for c in ascii_uppercase:
        ping(arduino.serial, c)
    for c in digits:
        ping(arduino.serial, c)
    print("Test OK: Arduino is replying with sensible data")
    
    
   
