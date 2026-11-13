def vigenere_encrypt(text, key):
    result = ""
    j = 0 

    for ch in text:
                       
            shift = ord(key[j % len(key)]) - ord('A')
            result += chr((ord(ch) - 32 + shift) % 95 + 32)
            j += 1
            
    return result


message = "HELLO WORLD"
key = "KEY"

encrypted = vigenere_encrypt(message, key)
print("Encrypted:", encrypted)
