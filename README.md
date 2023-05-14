## Encryption/Decryption of a file with TripleDES Algorithm (3DES-2Key) with CBC mode

This Python script allows you to encrypt and decrypt files using the TripleDES algorithm with a 2-key option and CBC mode. The script uses the `pycryptodome` library, which provides a comprehensive collection of cryptographic modules.

### Prerequisites

- Python 3.6 or later
- `pycryptodome` library

### How to use

1. Clone the repository to your local machine
2. Install the `pycryptodome` library with the command `pip install pycryptodome`
3. Open the `main.py` file and update the following variables:
   - `key`: set the encryption/decryption key
   - `input_file_path`: set the path to the input file
   - `encrypted_file_path`: set the path to the output encrypted file
   - `decrypted_file_path`: set the path to the output decrypted file
4. Run the script with the command `python main.py`
5. The encrypted file will be created at the `encrypted_file_path` location. The decrypted file will be created at the `decrypted_file_path` location.
