from check_crc import int_to_bytes, check_crc
from appa_109n import *

# tmp = b'UU\x00\x0e\x03\x00\x00\x00\t0\x00R\x01\x00\x00\x00\x00\x00G'
# tmp = b'UU\x00\x0e\x04\x00\x00\x80I\x00\x00\x0b\x01\x00\x00\x00\x00\x00\x91'
#tmp = b'UU\x00\x0e\x01\x01\x00\x01{\x0c\x00\x0b\x01\x00\x00\x00\x00\x00N'
# tmp = b'UU\x00\x0e\x04\x01\x00\x80\xf5\x03\x00Q\x01\x00\x00\x00\x00\x00\x87'
# tmp = b'UU\x00\x0e\x04\x01\x00\x80\xd0\x07\x00Q\x01\x00\x00\x00\x00\x00f'

# tmp = b'UU\x00\x0e\x03\x01\x00\x00\xbf\x00\x00\\\x01\x00\x00\x00\x00\x00\xd8'
# 10 2021-02-25 20:04:53.024 4.8896 KΩ
#tmp = b'UU\x00\x0e\x03\x00\x00\x00\xa2\x07\x00R\x01\x00\x00\x00\x00\x00\xb7'
# 10 2021-02-25 20:06:43.003 5002.24 Ω

tmp = b'UU\x00\x0e\x04\x01\x00\x80\xf5\x03\x00Q\x01\x00\x00\x00\x00\x00\x87'
# 10 2021-02-25 20:17:42.884 25932.8 Ω

def value_to_float(value: int, point_code: int) -> float:
    v = len(str(value))
    p = point_code
    if v > p:
        return float(str(value)[0:len(str(value)) - 
                                point_code]+"."+str(value)[len(str(value)) -
                                point_code:len(str(value))])
    elif v == p:
        return float("0."+str(value))        
    else:
        if v == 2:
            return float("0.0"+str(value))   
        elif v == 1:
            return float("0.00"+str(value))      

print(tmp.hex(), len(tmp))
print()

appa = tmp[0:4]

if appa.hex() == "5555000e":
    print("APPA 109N")
elif appa.hex() == "55550000":
    print("APPA 107N")


print("Знак градуса \u00B0С")

print(int_to_bytes(tmp[4]))
rotor_code = rotorcode(int_to_bytes(tmp[4]))
print(rotor_code)

blue_code = bluecode(int_to_bytes(tmp[4]) + 
                     int_to_bytes(tmp[5]))
print(blue_code)

range_code = rangecode(int_to_bytes(tmp[4]) + 
                       int_to_bytes(tmp[5]) + 
                       int_to_bytes(tmp[7]))
print(range_code)

# main_read = int_to_bytes(tmp[8]) + int_to_bytes(tmp[9]) + int_to_bytes(tmp[10])
# print(main_read)
main_read = int_to_bytes((tmp[8]<<16) | (tmp[9]<<8) | tmp[10])
# print(int_to_bytes(main_read))
# print("MAIN", main_read.hex())
main_read = int.from_bytes(main_read, byteorder = "little")
print("Main value=", main_read)

main_status_bits = bin(tmp[11])[2:].zfill(8)

point_code_bits = main_status_bits[5:]
# print(main_status_bits, point_code_bits)
main_pointcode = pointcode(point_code_bits)
print("Point code = ", main_pointcode)


main_unit_code_bits = main_status_bits[0:5]
# print(main_status_bits, unit_code_bits)
print("Unit code = ", unitcode(main_unit_code_bits))

func_table = functiontable(int_to_bytes(tmp[12]))
print("Function main = ", func_table)


sub_read = int_to_bytes(tmp[13]) + int_to_bytes(tmp[14]) + int_to_bytes(tmp[15])
# print("SUB", sub_read.hex())
sub_read_b = int.from_bytes(sub_read, byteorder = "big")
sub_read_l = int.from_bytes(sub_read, byteorder = "little")
print("Sub value=", sub_read_b, sub_read_l)

sub_status_bits = bin(tmp[16])[2:].zfill(8)

point_code_bits = sub_status_bits[5:]
# print(sub_status_bits, point_code_bits)
sub_pointcode = pointcode(point_code_bits)
print("Point code = ", sub_pointcode)

unit_code_bits = sub_status_bits[0:5]
# print(sub_status_bits, unit_code_bits)
print("Unit code = ", unitcode(unit_code_bits))

func_table = functiontable(int_to_bytes(tmp[17]))
print("Function sub = ",func_table)


print(value_to_float(main_read, main_pointcode), unitcode(main_unit_code_bits))