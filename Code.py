from Crypto.Cipher import DES3
import os


def encrypt_file(input_file_path, output_file_path, key):
    block_size = DES3.block_size
    iv = os.urandom(block_size)
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    with open(input_file_path, 'rb') as input_file, open(output_file_path, 'wb') as output_file:
        output_file.write(iv)
        while True:
            chunk = input_file.read(1024 * block_size)
            if len(chunk) == 0:
                break
            elif len(chunk) % block_size != 0:
                chunk += b' ' * (block_size - len(chunk) % block_size)
            output_file.write(cipher.encrypt(chunk))

def decrypt_file(input_file_path, output_file_path, key):
    block_size = DES3.block_size
    with open(input_file_path, 'rb') as input_file, open(output_file_path, 'wb') as output_file:
