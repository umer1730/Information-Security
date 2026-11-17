from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

key = b'0123456789abcdef'

message = b'ABCDABCD'

print("Original message: ",message)
print(f"Message size: {len(message)} bytes")
print(f"Message size: {len(message) * 8} bits")

#ecb mode
cipher_ecb = AES.new(key,AES.MODE_ECB)

padded_message = pad(message,AES.block_size)

encrypted_ecb = cipher_ecb.encrypt(padded_message)

print("ECB Ciphertext: ",encrypted_ecb.hex()) #it converts ciphertext bytes into a readable hexadecimal string

#cbc mode
iv_cbc = get_random_bytes(16)

cipher_cbc = AES.new(key,AES.MODE_CBC,iv=iv_cbc)

encrypted_cbc = cipher_cbc.encrypt(padded_message)

print("CBC IV: ",iv_cbc.hex())
print("CBC Ciphertext: ",encrypted_cbc.hex())

#cfb mode

iv_cfb = get_random_bytes(16)
cipher_cfb = AES.new(key,AES.MODE_CFB,iv=iv_cfb)

encrypted_cfb = cipher_cfb.encrypt(message)

print("CFB Ciphertext: ",encrypted_cfb.hex())

#OFB
iv_ofb = get_random_bytes(16)
cipher_ofb = AES.new(key,AES.MODE_OFB,iv=iv_ofb)

encrypted_ofb = cipher_ofb.encrypt(message)

print("OFB Ciphertext: ",encrypted_ofb.hex())

#CTR
nonce = get_random_bytes(8)
cipher_ctr = AES.new(key,AES.MODE_CTR,nonce = nonce)

encrypted_ctr = cipher_ctr.encrypt(message)
print("CTR Ciphertext: ",encrypted_ctr.hex())

