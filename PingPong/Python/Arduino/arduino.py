'''
Created on Mar 28, 2020

@author: HOLVOET
'''

import serial

class Arduino:
    
    def __init__(self, channel, doPrint=None):
        try:
            self.serial = serial.Serial(channel, 
                115200,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=0.5)
        
            pingPongOK=True
            # Active loop to wait for Arduino to be ready
            # Simple ping-pong of '0xff' and when we get one
            # back, it should mean Arduino is alive and kicking
            for _ in range(10):
                if doPrint != None:
                    print(".")
                ping0=b'\0'
                self.serial.write(ping0)
                # On time out, if Arduino is not up
                # we get an empty byte
                pong=self.serial.read(1)
                if pong==ping0:
                    # Arduino is alive and kicking
                    pingPongOK=True
                    break;
              
            if pingPongOK:
                # one more byte 0xfe
                # waiting for the replay
                # possible empty the buffer of 
                # remaing ff if any
                ping1=b'\1'  
                self.serial.write(ping1)
                pong=self.serial.read(1)
                while pong!=ping1:
                    if doPrint:
                        print(".")
                    pong=self.serial.read(1)
                
                if pong==ping1:
                    # All good here
                    if doPrint:
                        message="OK: Connected to " + channel + ", Arduino alive and kicking\n"
                        print(message)
                else:
                    raise Exception
            else:
                raise Exception
    
        except:
            if doPrint != None:
                message="OOPS: Arduino not connected on " + channel + "\n"
                print(message)
            self.serial=None
