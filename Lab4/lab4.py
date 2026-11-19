def vigenere_encrypt(text,key):
    result = ""
    j = 0

    for ch in text:
        base = 32
        shift = ord(key[j % len(key)]) - ord("A")
        result += chr((ord(ch) - base + shift) % 95 + base)
        j += 1
    return result

#column
def columnar_encrypt(text,columns):
    result = ""

    for col in range(columns):
        for pos in range(len(text)):
            if pos % columns == col:
                result += text[pos]
    return result

plaintext = "HELLO"
key = "USK"
columns = int(input("Columns we use: "))

vigenere_result = vigenere_encrypt(plaintext, key)
print("Vigenere:", vigenere_result)

final_result = columnar_encrypt(vigenere_result, columns)
print("column:", final_result)