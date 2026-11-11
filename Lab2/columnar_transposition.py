def columnar_encrypt(text):
    c1 = ""
    c2 = ""

    for i in range(len(text)):
        if i % 2 == 0:
            c1 += text[i]
        else:
            c2 += text[i]

    return c1 + c2


def columnar_decrypt(cipher):
    n = len(cipher)

    first_half = (n + 1) // 2

    c1 = cipher[:first_half]
    c2 = cipher[first_half:]

    plaintext = ""

    for i in range(len(c1)):
        plaintext += c1[i]
# check c2 also contain character on these index if yes then also add character
        if i < len(c2): 
            plaintext += c2[i]

    return plaintext


text = input("Enter message: ")

encrypted = columnar_encrypt(text)
decrypted = columnar_decrypt(encrypted)

print("Original:", text)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)