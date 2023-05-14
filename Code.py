from Crypto.Cipher import DES3
import os


def encrypt_file(input_file_path, output_file_path, key1, key2):
    block_size = DES3.block_size
    iv = os.urandom(block_size)
    cipher = DES3.new(key1, DES3.MODE_CBC, iv=iv)
    cipher2 = DES3.new(key2, DES3.MODE_CBC, iv=iv)
    with open(input_file_path, 'rb') as input_file, open(output_file_path, 'wb') as output_file:
        output_file.write(iv)
  while True:
            chunk = input_file.read(1024 * block_size)
            if len(chunk) == 0:
                break
            elif len(chunk) % block_size != 0:
                chunk += b' ' * (block_size - len(chunk) % block_size)
            ciphered_chunk = cipher.encrypt(chunk)
            ciphered_chunk2 = cipher2.encrypt(ciphered_chunk)
            output_file.write(ciphered_chunk2)      
