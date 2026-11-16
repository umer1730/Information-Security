from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad # pad adds bytes if plaintextx have not 16 bytes
import binascii # convert binary data into readable hexadecimal representation

key = b'0123456789abcdef' # b means byte objects
plaintext = b'A' * 16 + b'B' * 16 + b'A' * 16

cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(plaintext,16))
print(binascii.hexlify(ciphertext))

print("Block 1:",binascii.hexlify(ciphertext[:16]))
print("Block 3:",binascii.hexlify(ciphertext[32:48]))

print()

iv = b"1234567890abcdef"
cipher_cbc = AES.new(key,AES.MODE_CBC,iv)
ciphertext_cbc = cipher_cbc.encrypt(pad(plaintext,16))

print("CBC Block 1:",binascii.hexlify(ciphertext_cbc[:16]))
print("CBC Block 3:",binascii.hexlify(ciphertext_cbc[32:48]))
