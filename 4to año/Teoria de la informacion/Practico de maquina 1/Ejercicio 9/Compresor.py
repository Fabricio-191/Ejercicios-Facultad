"""
Haciendo uso de sockets, implemente un servidor y un cliente (a modo de ejemplo, se proveen un servidor y un cliente en lenguaje Python), que permita desde el cliente, enviar un archivo comprimido utilizando el alfabeto ABCDEFGH, y en el servidor, descomprimir el archivo.
"""
__table = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] # 3 bits

def __bytes_to_binary_string(string):
    return ''.join(format(i, '08b') for i in string)

def compress(str): # return binary buffer
    s = ''
    for c in str:
        s += format(__table.index(c), '03b')
        
    remainder = 8 - (len(s) + 3) % 8 # bits to complete the last byte
    s = format(remainder, '03b') + s
    s += '0' * remainder
    
    bytes = bytearray([int(s[i : i + 8], 2) for i in range(0, len(s), 8)])
    return bytes
    
def decompress(bytes):
    s = __bytes_to_binary_string(bytes)
    remainder = int(s[:3], 2)
    
    str = ''
    for i in range(3, len(s) - remainder, 3):
        str += __table[int(s[i : i+3], 2)]
        
    return str

if __name__ == '__main__':
    import random
    
    test_str = ''.join([random.choice(__table) for _ in range(100)])
    compressed = compress(test_str)
    decompressed = decompress(compressed)

    print('Original:', test_str)
    print('Compressed size:', len(test_str) * 3 / 8, 'bytes')
    print('Compressed:', compressed)
    compressed_binary = __bytes_to_binary_string(compressed)
    print(f'Compressed (binary): {compressed_binary} ({len(compressed_binary)} bits)')
    print('Decompressed:', decompressed)

    assert test_str == decompressed, 'Error: decompressed string is not equal to original string'
