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
import threading


# 5555000e02000001e31f001201f40100790240
# 5555000e020000013c1f001201f30100790298
# 5555000e02000001041f001201f40100790261
# 5555000e02000001b020001201f4010079020e
# 5555000e020000012521001201f40100790284

# b'UU\x00\x0e\x01\x00\x00\x00\x19\x04\x00\x0c\x01\x00\x00\x00y\x02^' 19

def send_port():
    # threading.Timer(0.5, send_port).start()
    ser.write(ser_message)
    ser_message_read = ser.readline()
   
    print(ser_message_read, len(ser_message_read))
    # print(ser_message_read.hex())
    time.sleep(0.5)


hex_string = '55 55 00 00 AA'
ser_message = bytes.fromhex(hex_string)

ser = serial.Serial(
    port='COM3', 
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout = 0)
    
ser.close()  

ser.open()

while True:
    try:
        send_port()
    except Exception as exc:
        print('type: {0}, message: {1}'.format(type(exc), str(exc)))
        break

