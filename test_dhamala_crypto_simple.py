import unittest
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# ----------------------
# Utility Crypto Functions
# ----------------------

def get_key(password):
    salt = b'salt_'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def add_padding(data):
    padder = padding.PKCS7(128).padder()
    return padder.update(data) + padder.finalize()

def remove_padding(data):
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(data) + unpadder.finalize()

def encrypt_content(key, content):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_data = add_padding(content)
    encrypted = encryptor.update(padded_data) + encryptor.finalize()
    return iv + encrypted

def decrypt_content(key, encrypted_content):
    iv = encrypted_content[:16]
    ciphertext = encrypted_content[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(ciphertext) + decryptor.finalize()
    return remove_padding(decrypted)

# ----------------------
# Unit Tests
# ----------------------

class TestCryptoFunctions(unittest.TestCase):

    def test_key_derivation(self):
        """test_key_derivation"""
        key = get_key("mypassword")
        self.assertEqual(len(key), 32)

    def test_same_password_gives_same_key(self):
        """test_same_password_gives_same_key"""
        key1 = get_key("abc123")
        key2 = get_key("abc123")
        self.assertEqual(key1, key2)

    def test_padding_unpadding(self):
        """test_padding_unpadding"""
        data = b"hello world"
        padded = add_padding(data)
        unpadded = remove_padding(padded)
        self.assertEqual(data, unpadded)

    def test_encrypt_decrypt(self):
        """test_encrypt_decrypt"""
        password = "dhamala123"
        content = b"This is a test message."
        key = get_key(password)
        encrypted = encrypt_content(key, content)
        decrypted = decrypt_content(key, encrypted)
        self.assertEqual(content, decrypted)

    def test_random_iv_output(self):
        """test_random_iv_output"""
        key = get_key("uniqueKey")
        content = b"same data"
        out1 = encrypt_content(key, content)
        out2 = encrypt_content(key, content)
        self.assertNotEqual(out1, out2)

# ----------------------
# Run All Tests with Custom Output
# ----------------------

if __name__ == '__main__':
    print("Running Tests...")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCryptoFunctions)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
