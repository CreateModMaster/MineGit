strtoturn = input("Enter a string: ")
encstr = strtoturn.encode()
hexstr = encstr.hex()
print(hexstr)
hexint = int(hexstr, 16)
hexbin = bin(hexint)
binary_string = hexbin[2:]
print(binary_string)
strtodecode = str