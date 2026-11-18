from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import os


key = b'0123456789abcdef'


def encrypt_image(filename):

    with open(filename, 'rb') as f:
        image_data = f.read() # file se data read krke image_data me data store krna 

    print("\nProcessing:", filename)
    print(f"Original size: {len(image_data)} bytes")

    padded_data = pad(image_data, 16)

    # ECB Encryption

    cipher_ecb = AES.new(key, AES.MODE_ECB)

    encrypted_ecb = cipher_ecb.encrypt(padded_data)

    ecb_filename = filename.split('.', 1)[0] + "_ECB.bin"

    with open(ecb_filename, 'wb') as f:
        f.write(encrypted_ecb)

    # CBC Encryption

    iv = get_random_bytes(16)

    cipher_cbc = AES.new(key,AES.MODE_CBC,iv=iv)

    encrypted_cbc = cipher_cbc.encrypt(padded_data)

    cbc_filename = filename.split('.', 1)[0] + "_CBC.bin"

    with open(cbc_filename, 'wb') as f:
        f.write(iv)
        f.write(encrypted_cbc)

    print("ECB file:", ecb_filename)
    print("CBC file:", cbc_filename)


# PROCESS THREE IMAGES

images = [
    'amongus.png',
    'groot.jpg',
    'WalterWhite.png'
]

for image in images:
    if os.path.exists(image):
        encrypt_image(image)
    else:
        print("File not found:", image)