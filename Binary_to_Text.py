def binary_to_text(binary):
    text = ''.join(chr(int(binary[i*8:i*8+8], 2)) for i in range(len(binary)//8))
    return text
