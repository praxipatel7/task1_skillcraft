def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Only shift alphabets
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result


def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)


# Main Program
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted = caesar_cipher_encrypt(message, shift)
decrypted = caesar_cipher_decrypt(encrypted, shift)

print(f"\nOriginal:  {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")