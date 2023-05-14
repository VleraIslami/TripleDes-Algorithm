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

iv = input_file.read(block_size)
        cipher = DES3.new(key, DES3.MODE_CBC, iv)
        while True:
            chunk = input_file.read(1024 * block_size)
            if len(chunk) == 0:
                break
            output_file.write(cipher.decrypt(chunk))

if name == 'main':
    key = b'\x01\x23\x45\x67\x89\xab\xcd\xef\x87\x65\x43\x21\xfe\xdc\xba\x98'
        
input_file_path = r'C:\Users\Online\Desktop\Siguri1\vlera.txt'
    encrypted_file_path = r'C:\Users\Online\Desktop\Siguri1\encrypted_file.bin'
    decrypted_file_path = r'C:\Users\Online\Desktop\Siguri1\decrypted_file.txt'

    # Encrypt file
    encrypt_file(input_file_path, encrypted_file_path, key)
    print('File encrypted successfully.')

    # Decrypt file
    decrypt_file(encrypted_file_path, decrypted_file_path, key)
    print('File decrypted successfully.')
