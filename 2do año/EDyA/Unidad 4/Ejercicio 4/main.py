from Huffman import Huffman
from os import path

if __name__ == '__main__':
    Huffman().comprimir(
		path.dirname(__file__) + '/input.txt',
		path.dirname(__file__) + '/output.txt'
	)