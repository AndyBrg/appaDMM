# from serial import Serial

# def data_send(v):
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

from ctypes import c_int
from threading import Timer
from datetime import datetime
from check_crc import check_crc


# 5555000e02000001e31f001201f40100790240
# b'UU\x00\x0e\x01\x00\x00\x00\x19\x04\x00\x0c\x01\x00\x00\x00y\x02^' 19

# Not connected...
# Please connect the device

# class pxtup(Structure):
#     _fields_ = [('red', c_int),
#                 ('green', c_int),
#                 ('blue', c_int)]

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

# rt = RepeatedTimer(1, hello, "World")

poll_time = 0.5


index = 0

global time_receive
global data_receive

def send_port():
    # threading.Timer(poll_time, send_port).start()
    ser.write(data_send)
    time.sleep(0.5)
    data_receive = ser.readline()
    time_receive = datetime.isoformat(
        datetime.now(), sep=' ', timespec='milliseconds')    
    if check_crc(data_receive):
        crc = "OK"
        global index
        index += 1
    else:
        crc ="ER"

    print(index, time_receive, crc, data_receive.hex())




appa_109n = "55 55 00 00 AA"
data_send = bytes.fromhex(appa_109n)

ser = serial.Serial(
    port="COM3", 
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    xonxoff=False,
    timeout=0)
    
ser.close()  

ser.open()

# while True:
#     try:
#         if ser.is_open:
#             send_port(p_time)
#     except Exception as exc:
#         print("type: {0}, message: {1}".format(type(exc), str(exc)))
#         break

if ser.is_open:
    send_port()
    rt = RepeatedTimer(poll_time, send_port)


try:
    time.sleep(10) # your long-running job goes here...
finally:
    rt.stop() # better in a try/finally block to make sure the program ends!