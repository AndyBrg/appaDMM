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

import serial

hex_string = '55 55 00 00 AA'
ser_message = bytes.fromhex(hex_string)

ser = serial.Serial(
    port='COM4', 
    baudrate=9600, 
    bytesize=EIGHTBITS,
    parity=PARITY_NONE,
    stopbits=STOPBITS_ONE,
    timeout = 0)
    
ser.close()    
ser.open()
ser.flushInput()
while True:
    try:
        ser.write(ser_message)
        ser_message_read = ser.readline()
        time.sleep(0.5)

        print(ser_message_read.hex())
    except:
        print("Interrupt")
        break
