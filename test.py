tmp = b'UU\x00\x0e\x01\x00\x00\x00\x19\x04\x00\x0c\x01\x00\x00\x00y\x02^'

    

print(tmp.hex())
print(len(tmp))
print()

# tmp = bytearray(tmp)
for x in range(len(tmp)):
    print(tmp[x])