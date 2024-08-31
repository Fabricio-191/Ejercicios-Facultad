# Tabla de caracteres que se pueden comprimir, cada uno representado por 3 bits
__table = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] # 3 bits

def __bytes_to_binary_string(string):
    """
    Convierte una secuencia de bytes en una cadena binaria.
    
    :param string: Secuencia de bytes a convertir.
    :return: Cadena binaria que representa la secuencia de bytes.
    """
    return ''.join(format(i, '08b') for i in string)

def compress(str):
    """
    Comprime una cadena utilizando una tabla de caracteres predefinida.
    
    :param str: Cadena a comprimir.
    :return: Buffer binario comprimido en forma de bytearray.
    """
    s = ''
    # Convierte cada carácter de la cadena en su representación binaria de 3 bits
    for c in str:
        s += format(__table.index(c), '03b')
        
    # Calcula los bits necesarios para completar el último byte
    remainder = 8 - (len(s) + 3) % 8
    # Añade el número de bits de relleno al inicio de la cadena binaria
    s = format(remainder, '03b') + s
    # Añade los bits de relleno al final de la cadena binaria
    s += '0' * remainder
    
    # Convierte la cadena binaria en un bytearray
    bytes = bytearray([int(s[i : i + 8], 2) for i in range(0, len(s), 8)])
    
    # print(f'Compressed: {str} => {s} => {bytes}')
    return bytes
    
def decompress(bytes):
    """
    Descomprime un buffer binario en una cadena utilizando una tabla de caracteres predefinida.
    
    :param bytes: Buffer binario comprimido en forma de bytearray.
    :return: Cadena descomprimida.
    """
    # Convierte el bytearray en una cadena binaria
    s = __bytes_to_binary_string(bytes)
    # Obtiene el número de bits de relleno del inicio de la cadena binaria
    remainder = int(s[:3], 2)
    
    str = ''
    # Convierte cada grupo de 3 bits en el carácter correspondiente de la tabla
    for i in range(3, len(s) - remainder, 3):
        str += __table[int(s[i : i+3], 2)]
    
    # print(f'Decompressed: {bytes} => {s} => {str}')
    return str

if __name__ == '__main__':
    import random
    
    # Genera una cadena de prueba aleatoria utilizando los caracteres de la tabla
    test_str = ''.join([random.choice(__table) for _ in range(5)])
    # Comprime la cadena de prueba
    compressed = compress(test_str)
    # Descomprime la cadena comprimida
    decompressed = decompress(compressed)

    # Muestra los resultados
    print('Original:', test_str)
    print('Compressed size:', len(test_str) * 3 / 8, 'bytes')
    print('Compressed:', compressed)
    compressed_binary = __bytes_to_binary_string(compressed)
    print(f'Compressed (binary): {compressed_binary} ({len(compressed_binary)} bits)')
    print('Decompressed:', decompressed)

    # Verifica que la cadena descomprimida sea igual a la cadena original
    assert test_str == decompressed, 'Error: decompressed string is not equal to original string'