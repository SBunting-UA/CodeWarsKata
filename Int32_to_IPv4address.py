def int32_to_ip(int32):
    binary = bin(int32)[2:]
    octets = []
    placeholder1 = 0
    placeholder2 = 8

    while len(binary) != 32:
        binary = '0' + binary

    while len(octets) != 4:
        current_oct = binary[placeholder1:placeholder2]
        current_oct = str(int(current_oct, 2))
        octets.append(current_oct)
        placeholder1 += 8
        placeholder2 += 8

    return octets[0] + '.' + octets[1] + '.' + octets[2] + '.' + octets[3]