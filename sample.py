import random

def generate_key(length):
    """
    Generate a random symmetric key of the specified length.
    """
    key = ""
    for i in range(length):
        key += chr(random.randint(0, 255))
    return key

def encrypt(message, key):
    """
    Encrypt the message using the provided key.
    """
    encrypted_message = ""
    for i in range(len(message)):
        char = message[i]
        key_char = key[i % len(key)]
        encrypted_message += chr(ord(char) ^ ord(key_char))
    return encrypted_message

def decrypt(encrypted_message, key):
    """
    Decrypt the encrypted message using the provided key.
    """
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        key_char = key[i % len(key)]
        decrypted_message += chr(ord(char) ^ ord(key_char))
    return decrypted_message

# Example usage
key = generate_key(16)
message = "This is a secret message."
encrypted_message = encrypt(message, key)
decrypted_message = decrypt(encrypted_message, key)
print("Original message: ", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)
