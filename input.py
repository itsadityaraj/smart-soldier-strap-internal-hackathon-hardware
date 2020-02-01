from soldier import soldier

import serial

ser =  serial.Serial('COM4', baudrate = 9600, timeout = 1)

while 1 :
    ad = ser.readline().decode('ascii')
    print(ad)