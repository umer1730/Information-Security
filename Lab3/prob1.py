from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii

key = b'0123456789abcdef'
# b means this is a byte object
message = b'\x00' * 32

# ECB
cipher_ecb = AES.new(key, AES.MODE_ECB)

ciphertext_ecb = cipher_ecb.encrypt(pad(message, 16))

print("ECB:",binascii.hexlify(ciphertext_ecb).decode())

# CBC
iv = b'1234567890abcdef'

cipher_cbc = AES.new(key,AES.MODE_CBC,iv)

ciphertext_cbc = cipher_cbc.encrypt(pad(message, 16))
print()

print("CBC:",binascii.hexlify(ciphertext_cbc).decode()) #.decode() convert bytes into a string