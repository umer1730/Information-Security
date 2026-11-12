dictionary = {
    'A': '5',
    'B': '6',
    'C': '7',
    'D': '8',
    'E': '9',
    'F': '10',
    'G': '1',
    'H': '2',
    'I': '3',
    'J': '4',
    'K': '15',
    'L': '16',
    'M': '17',
    'N': '18',
    'O': '19',
    'P': '20',
    'Q': '11',
    'R': '12',
    'S': '13',
    'T': '14',
    'U': '15',
    'V': '25',
    'W': '26',
    'X': '44',
    'Y': '32',
    'Z': '50'
}

def monoalphabetic_encrypt(text):
    result = ""

    for char in text:
        result += dictionary[char]

    return result


text = input("Enter text: ").upper()

encrypted = monoalphabetic_encrypt(text)

print("Original:", text)
print("Encrypted:", encrypted)