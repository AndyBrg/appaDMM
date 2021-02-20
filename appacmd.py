# from serial import Serial

# def send_message(v):
#     if v == 0:
#         hex_string = '55 55 00 00 AA'
#     elif v == 1:
#         hex_string = '55 55 00 00 AA'
#     elif v == 2:
#         hex_string = '55 55 00 00 AA'
#     message = bytes.fromhex(hex_string)
#     ser = Serial(port='COM4', baudrate=9600, timeout = 0.1)
#     ser.open()
#     #self.write(ser, message)
#     if ser.is_open:
#         ser.flushInput()
#         ser.flushOutput()
#         sleep(0.1)
#         try:
#             ser.write(message)
#         except Exception as exc:
#             print('type: {0}, message: {1}'.format(type(exc), str(exc)))
#         else:
#             res = ser.readline()
#             print(res)
#             ser.close()

import time
import serial
# import threading
from ctypes import *

from datetime import datetime

from check_crc import check_crc

# 5555000e02000001e31f001201f40100790240
# b'UU\x00\x0e\x01\x00\x00\x00\x19\x04\x00\x0c\x01\x00\x00\x00y\x02^' 19

# Not connected...
# Please connect the device

class pxtup(Structure):
    _fields_ = [('red', c_int),
                ('green', c_int),
                ('blue', c_int)]

p_time = 0.5
index = 0

def send_port(poll_time: float):
    # threading.Timer(0.5, send_port).start()
    ser.write(send_message)
    time.sleep(poll_time)
    time = time_tmp = datetime.isoformat(
        datetime.now(), sep=' ', timespec='milliseconds')
    receive_message = ser.readline()
    if check_crc(receive_message):
        crc = "OK"
        index += 1
    else:
        crc ="ER"

    print(cnt, time, receive_message.hex(), crc)




com_appa = "55 55 00 00 AA"
send_message = bytes.fromhex(com_appa)

ser = serial.Serial(
    port="COM3", 
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout = 0)
    
ser.close()  

ser.open()

while True:
    try:
        if ser.is_open:
            send_port(p_time)
    except Exception as exc:
        print("type: {0}, message: {1}".format(type(exc), str(exc)))
        break

