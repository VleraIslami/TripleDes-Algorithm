from Crypto.Cipher import DES3
import os


def encrypt_file(input_file_path, output_file_path, key):
    block_size = DES3.block_size
    iv = os.urandom(block_size)
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    with open(input_file_path, 'rb') as input_file, open(output_file_path, 'wb') as output_file:
        output_file.write(iv)
