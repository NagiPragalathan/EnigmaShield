# import random

# def generate_key(length):
#     """
#     Generate a random symmetric key of the specified length.
#     """
#     key = ""
#     for i in range(length):
#         key += chr(random.randint(0, 255))
#     return key

# def encrypt(message, key):
#     """
#     Encrypt the message using the provided key.
#     """
#     encrypted_message = ""
#     for i in range(len(message)):
#         char = message[i]
#         key_char = key[i % len(key)]
#         encrypted_message += chr(ord(char) ^ ord(key_char))
#     return encrypted_message

# def decrypt(encrypted_message, key):
#     """
#     Decrypt the encrypted message using the provided key.
#     """
#     decrypted_message = ""
#     for i in range(len(encrypted_message)):
#         char = encrypted_message[i]
#         key_char = key[i % len(key)]
#         decrypted_message += chr(ord(char) ^ ord(key_char))
#     return decrypted_message

# # Example usage
# key = generate_key(16)
# message = "This is a secret message."
# encrypted_message = encrypt(message, key)
# decrypted_message = decrypt(encrypted_message, key)
# print("Original message: ", message)
# print("Encrypted message:", encrypted_message)
# print("Decrypted message:", decrypted_message)

import random
import math

def generate_prime_number():
    """Generate a random prime number."""
    while True:
        prime_candidate = random.randint(2**10, 2**11)
        if is_prime(prime_candidate):
            return prime_candidate

def is_prime(num):
    """Check if a number is prime."""
    if num == 2 or num == 3:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, math.isqrt(num) + 1, 2):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    """Calculate the greatest common divisor using Euclid's algorithm."""
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """Extended Euclidean algorithm to find modular inverse."""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def generate_keypair():
    """Generate public and private keys for RSA encryption."""
    p = generate_prime_number()
    q = generate_prime_number()
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Find e such that 1 < e < phi and gcd(e, phi) = 1
    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            break
    
    # Find d such that d is the modular inverse of e
    _, d, _ = extended_gcd(e, phi)
    d = d % phi
    
    # Public key: (e, n), Private key: (d, n)
    return (e, n), (d, n)

def encrypt(message, public_key):
    """Encrypt a message using the public key."""
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def decrypt(encrypted_message, private_key):
    """Decrypt an encrypted message using the private key."""
    d, n = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    return "".join(decrypted_message)

# Example usage
message = "246564"
public_key, private_key = generate_keypair()
print(public_key,private_key)
encrypted = encrypt(message, public_key)
decrypted = decrypt(encrypted, private_key)

print("Original message:", message)
print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)
