from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes # encryption ke liye random bytes generate krna
import binascii

key = b'0123456789abcdef'

message = b'\x00' * 32

cipher_ecb1 = AES.new(key,AES.MODE_ECB)
ciphertext_ecb1 = cipher_ecb1.encrypt(pad(message,16))

cipher_ecb2 = AES.new(key,AES.MODE_ECB)
ciphertext_ecb2 = cipher_ecb2.encrypt(pad(message,16))

iv1 = get_random_bytes(16)

cipher_cbc1 = AES.new(key,AES.MODE_CBC,iv1)
ciphertext_cbc1 = cipher_cbc1.encrypt(pad(message,16))

iv2 = get_random_bytes(16)
cipher_cbc2 = AES.new(key,AES.MODE_CBC,iv2)
ciphertext_cbc2 = cipher_cbc2.encrypt(pad(message,16))

print("ECB Encryption 1:",binascii.hexlify(ciphertext_ecb1).decode())

print("ECB Encryption 2:",binascii.hexlify(ciphertext_ecb2).decode())

print("CBC Encryption 1:",binascii.hexlify(ciphertext_cbc1).decode())

print("CBC Encryption 2:",binascii.hexlify(ciphertext_cbc2).decode())

print("Which produce same")

print("ECB same: ",
      ciphertext_ecb1 == ciphertext_ecb2)

print("CBC same: ",
      ciphertext_cbc1 == ciphertext_cbc2)