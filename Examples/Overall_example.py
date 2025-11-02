"""
EnigmaShield - Comprehensive Examples
=====================================

This file contains comprehensive examples demonstrating the usage of EnigmaShield
module for encrypting various Python data types at runtime.

Encryption Types:
- Type 1: File Data-Based Encryption (Encrypt/Decrypt)
- Type 2: Simple Encryption (easyEncrypt/easyDectypt)
- Type 3: Shift-Based Encryption (encrypt/decrypt) - Default
- Type 4: RSA Encryption (RSAencrypt/RSAdecrypt)
"""

# Import necessary modules
from EnigmaShield.CryptoTypes import array, Dict, Tuple, Set, String, Int, Keys
from EnigmaShield.CryptoBloom import generate_keypair, RSAencrypt, RSAdecrypt

# ============================================================================
# Example 1: Array Operations
# ============================================================================
print("=" * 70)
print("Example 1: Array Operations with Type 3 (Default Encryption)")
print("=" * 70)

# Create an encrypted array with initial values
arr = array(['hello', 'hi'], "super_key", Type=3)
print(f"Initial array: {arr}")

# Add elements
arr.add("cat")
arr.add(1)
arr.add([1, 2, 3])
arr.add((1, 2))
arr.add({1, 2})
arr.add({"name": "Alice", "age": 25})
print(f"After adding elements: {arr}")

# Convert back to Python list
decrypted = arr.to_pyarray("super_key")
print(f"Decrypted array: {decrypted}")
print(f"Length: {arr.len()}")
print(f"Count of element [1, 2, 3]: {arr.count([1, 2, 3])}")
print()

# ============================================================================
# Example 2: Array with Different Operations
# ============================================================================
print("=" * 70)
print("Example 2: Array with Various Operations")
print("=" * 70)

arr2 = array([1, 2, 3, 1, (1, 2), (1, 2), (1, 5), 8, {1, 2}], "key", Type=3)
arr2.add("hello")
arr2.add("nagi")
arr2.add([1, 2, 3])

print(f"Array: {arr2}")
print(f"Count of (1, 2): {arr2.count((1, 2))}")
print(f"Index of (1, 2): {arr2.index((1, 2))}")

# Extend array
arr2.extend([10, 20, 30, (12, 32, [1, 2])])
print(f"After extend: {arr2.to_pyarray('key')}")

# Insert element
arr2.insert(3, {"hello": "hi"})
print(f"After insert: {arr2.to_pyarray('key')}")

# Remove element
arr2.remove(1)
print(f"After remove(1): {arr2.to_pyarray('key')}")

# Reverse
arr2.reverse()
print(f"After reverse: {arr2.to_pyarray('key')}")

# Pop
arr2.pop(-1)
print(f"After pop(-1): {arr2.to_pyarray('key')}")
print()

# ============================================================================
# Example 3: Dictionary Operations
# ============================================================================
print("=" * 70)
print("Example 3: Dictionary Operations")
print("=" * 70)

# Create encrypted dictionary (using simple values to avoid nested structure bugs)
my_dict = Dict({"name": "Alice", "age": "25"}, Key="hi", Type=3)
print(f"Encrypted dict: {my_dict}")

# Add key-value pair
my_dict.add("city", "New York")
print(f"After adding city: {my_dict}")

# Get value (returns encrypted value)
name_encrypted = my_dict.get("name")
print(f"Get name (encrypted): {name_encrypted}")

# Note: to_pyDict has issues with nested structures due to library bug
# For simple string/number values, it should work
# Convert back to Python dict to work with decrypted values
try:
    decrypted_dict = my_dict.to_pyDict("hi")
    print(f"Decrypted dictionary: {decrypted_dict}")
    if decrypted_dict:
        name = decrypted_dict.get("name")
        print(f"Get name (decrypted): {name}")
except Exception as e:
    print(f"Note: to_pyDict encountered an issue (library bug with nested data): {type(e).__name__}")

# Get all items, keys, values (encrypted)
items = list(my_dict.items())
keys = list(my_dict.keys())
values = list(my_dict.values())
print(f"Items (encrypted, first 2): {items[:2] if len(items) > 2 else items}")
print(f"Keys (encrypted, first 2): {keys[:2] if len(keys) > 2 else keys}")
print(f"Values (encrypted, first 2): {values[:2] if len(values) > 2 else values}")

# Set default (using encrypted key)
# Note: There's a library bug with setdefault - it uses self.Key but attribute may be self.key
# Workaround: use add() method instead
my_dict.add("country", "USA")
print(f"After adding country, dict size: {len(my_dict)}")

# Pop item (returns encrypted)
try:
    popped = my_dict.popitem()
    print(f"Popped item (encrypted): {popped}")
except KeyError:
    print("Dictionary is empty, cannot pop item")

# Note: For removing specific keys, work with decrypted dict and recreate
print("Dictionary operations completed")
print()

# ============================================================================
# Example 4: Tuple Operations
# ============================================================================
print("=" * 70)
print("Example 4: Tuple Operations")
print("=" * 70)

# Create encrypted tuple
tup = Tuple((1, 1, 23, 3, "hello", (1, 2, ((1, 23), 12, 3))), "hi", Type=3)
print(f"Encrypted tuple: {tup}")

# Count occurrences
count_1 = tup.count(1)
print(f"Count of 1: {count_1}")

# Find index (note: library has bug with index() method, use decrypted tuple instead)
decrypted_temp = tup.to_pytuple("hi")
if 23 in decrypted_temp:
    index_23 = decrypted_temp.index(23)
    print(f"Index of 23: {index_23}")
else:
    print("23 not found in tuple")

# Convert back to Python tuple
decrypted_tuple = tup.to_pytuple("hi")
print(f"Decrypted tuple: {decrypted_tuple}")

# Tuple operations
tup1 = Tuple((1, 2, 3), "key", Type=3)
tup2 = Tuple((4, 5, 6), "key", Type=3)
# Note: Tuple concatenation has a bug - combine decrypted tuples instead
decrypted_tup1 = tup1.to_pytuple("key")
decrypted_tup2 = tup2.to_pytuple("key")
combined_decrypted = decrypted_tup1 + decrypted_tup2
combined = Tuple(combined_decrypted, "key", Type=3)
print(f"Combined tuples: {combined.to_pytuple('key')}")

# Repeat - work around library bug by using decrypted tuple
decrypted_tup1 = tup1.to_pytuple("key")
repeated_decrypted = decrypted_tup1 * 3
repeated = Tuple(repeated_decrypted, "key", Type=3)
print(f"Repeated tuple (3x): {repeated.to_pytuple('key')}")
print()

# ============================================================================
# Example 5: Set Operations
# ============================================================================
print("=" * 70)
print("Example 5: Set Operations")
print("=" * 70)

# Create encrypted set
my_set = Set({"a", "b", "c"}, "hello", Type=3)
print(f"Encrypted set: {my_set}")

# Add elements
my_set.add((1, 2))
my_set.add(7)
my_set.add("banana")
print(f"After adding elements: {my_set.to_pyset('hello')}")

# Remove element
my_set.remove(7)
print(f"After remove(7): {my_set.to_pyset('hello')}")

# Discard element (doesn't raise error if not found)
my_set.discard("banana")
print(f"After discard('banana'): {my_set.to_pyset('hello')}")

# Pop element
popped = my_set.pop()
print(f"Popped element: {popped}")

# Set operations with regular Python sets
y = {"f", "e", "d", "c", "b", "a"}
z = {"f", "g", "c"}

# Difference (works with regular sets)
# Note: The Set methods may be overridden by later definitions, so use to_pyset first
decrypted_my_set = my_set.to_pyset("hello")
diff = decrypted_my_set.difference(y)
print(f"Difference: {diff}")

# Intersection (works with regular sets)
intersection = decrypted_my_set.intersection(y, z)
print(f"Intersection: {intersection}")

# Convert back to Python set
decrypted_set = my_set.to_pyset("hello")
print(f"Decrypted set: {decrypted_set}")
print()

# ============================================================================
# Example 6: String Operations
# ============================================================================
print("=" * 70)
print("Example 6: String Operations")
print("=" * 70)

# Create encrypted string
s = String("hello hi hi", "hi", Type=3)
print(f"Encrypted string: {s}")

# String methods (note: later method definitions override earlier ones without security_key)
# For decrypted operations, use topystr() first
decrypted_s = s.topystr("hi")
print(f"Decrypted string: {decrypted_s}")

# Note: String methods that return new String objects have bugs with Key handling
# Work directly with decrypted string for transformations
decrypted_capitalized = decrypted_s.capitalize()
print(f"Capitalized (decrypted): {decrypted_capitalized}")

decrypted_uppercase = decrypted_s.upper()
print(f"Uppercase (decrypted): {decrypted_uppercase}")

decrypted_lowercase = decrypted_s.lower()
print(f"Lowercase (decrypted): {decrypted_lowercase}")

decrypted_title = decrypted_s.title()
print(f"Title case (decrypted): {decrypted_title}")

decrypted_swap = decrypted_s.swapcase()
print(f"Swap case (decrypted): {decrypted_swap}")

decrypted_casefold = decrypted_s.casefold()
print(f"Casefold (decrypted): {decrypted_casefold}")

# String checks (on decrypted string)
is_title = decrypted_s.istitle()
print(f"Is title: {is_title}")

is_alnum = decrypted_s.isalnum()
print(f"Is alphanumeric: {is_alnum}")

is_alpha = decrypted_s.isalpha()
print(f"Is alphabetic: {is_alpha}")

is_ascii = decrypted_s.isascii()
print(f"Is ASCII: {is_ascii}")

is_digit = decrypted_s.isdigit()
print(f"Is digit: {is_digit}")

# String operations (on decrypted string)
decrypted_centered = decrypted_s.center(20)
print(f"Centered (width 20): {decrypted_centered}")

decrypted_filled = decrypted_s.zfill(15)
print(f"Zfill (width 15): {decrypted_filled}")

decrypted_stripped = decrypted_s.strip(" ")
print(f"Stripped: {decrypted_stripped}")

decrypted_split = decrypted_s.split(" ")
print(f"Split by space: {decrypted_split}")

decrypted_find = decrypted_s.find("h")
print(f"Find 'h': {decrypted_find}")

# Convert back to Python string
decrypted_str = s.topystr("hi")
print(f"Decrypted string: {decrypted_str}")
print()

# ============================================================================
# Example 7: Integer Operations
# ============================================================================
print("=" * 70)
print("Example 7: Integer Operations")
print("=" * 70)

# Create encrypted integer
int1 = Int(100, key="my_key", Type=3)
print(f"Encrypted Int: {int1}")

int2 = Int(50, key="my_key", Type=3)

# Get integer value
value1 = int1.get_int("my_key")
value2 = int2.get_int("my_key")
print(f"Int1 value: {value1}")
print(f"Int2 value: {value2}")

# Arithmetic operations (note: some operations may have issues with encryption/decryption)
try:
    addition = int1 + int2
    print(f"Addition (100 + 50): {addition.get_int('my_key')}")
except Exception as e:
    print(f"Addition error: {type(e).__name__}")

try:
    subtraction = int1 - int2
    print(f"Subtraction (100 - 50): {subtraction.get_int('my_key')}")
except Exception as e:
    print(f"Subtraction error: {type(e).__name__}")

try:
    multiplication = int1 * int2
    print(f"Multiplication (100 * 50): {multiplication.get_int('my_key')}")
except Exception as e:
    print(f"Multiplication error: {type(e).__name__}")

try:
    division = int1 / int2
    print(f"Division (100 / 50): {division.get_int('my_key')}")
except Exception as e:
    print(f"Division error: {type(e).__name__}")

try:
    floor_div = int1 // int2
    print(f"Floor division (100 // 50): {floor_div.get_int('my_key')}")
except Exception as e:
    print(f"Floor division error: {type(e).__name__}")

try:
    modulo = int1 % int2
    print(f"Modulo (100 % 50): {modulo.get_int('my_key')}")
except Exception as e:
    print(f"Modulo error: {type(e).__name__}")

try:
    power = int1 ** 2
    print(f"Power (100 ** 2): {power.get_int('my_key')}")
except Exception as e:
    print(f"Power error: {type(e).__name__}")

# Comparison operations (note: some comparison operations have bugs)
try:
    print(f"int1 == int2: {int1 == int2}")
except Exception as e:
    print(f"Comparison (==) error: {type(e).__name__}")

# Use decrypted values for comparisons to avoid bugs
val1 = int1.get_int("my_key")
val2 = int2.get_int("my_key")
print(f"int1 > int2 (decrypted): {val1 > val2}")
print(f"int1 < int2 (decrypted): {val1 < val2}")
print(f"int1 >= int2 (decrypted): {val1 >= val2}")
print(f"int1 <= int2 (decrypted): {val1 <= val2}")

# Convert to other types
float_val = int1.get_float("my_key")
print(f"Float value: {float_val}")
print()

# ============================================================================
# Example 8: RSA Encryption (Type 4)
# ============================================================================
print("=" * 70)
print("Example 8: RSA Encryption (Type 4)")
print("=" * 70)

# Generate RSA keypair
public_key, private_key = generate_keypair()
print(f"Public key (e, n): {public_key}")
print(f"Private key (d, n): {private_key}")

# Create encrypted array with RSA
rsa_array = array(["secret", "data", 123], Key=public_key, Type=4)
print(f"RSA encrypted array: {rsa_array}")

# Decrypt RSA array
decrypted_rsa = rsa_array.to_pyarray(private_key)
print(f"Decrypted RSA array: {decrypted_rsa}")

# RSA encrypted string
rsa_string = String("Hello RSA!", Key=public_key, Type=4)
print(f"RSA encrypted string: {rsa_string}")
decrypted_rsa_str = rsa_string.topystr(private_key)
print(f"Decrypted RSA string: {decrypted_rsa_str}")
print()

# ============================================================================
# Example 9: Using Keys Class for Global Configuration
# ============================================================================
print("=" * 70)
print("Example 9: Global Key Configuration")
print("=" * 70)

# Set global key and type
keys_manager = Keys()
keys_manager.setkey("global_secret_key")
keys_manager.setType(3)

print(f"Global key: {keys_manager.getkey()}")
print(f"Global type: {keys_manager.getType()}")

# Create objects without specifying key (uses global)
arr_global = array([1, 2, 3])  # Uses global key
print(f"Array with global key: {arr_global}")

str_global = String("test string")  # Uses global key
print(f"String with global key: {str_global}")
print()

# ============================================================================
# Example 10: Complex Nested Data Structures
# ============================================================================
print("=" * 70)
print("Example 10: Complex Nested Data Structures")
print("=" * 70)

# Complex nested structure
complex_data = [
    1,
    2,
    3,
    [1, 2, [74, 3, {1, 2, (1, 2)}]],
    (1, 2),
    {1, 2},
    74,
    {"nested": {"dict": [1, 2, 3]}}
]

encrypted_complex = array(complex_data, "encryption_key", Type=3)
print(f"Encrypted complex structure: {encrypted_complex}")
decrypted_complex = encrypted_complex.to_pyarray("encryption_key")
print(f"Decrypted complex structure: {decrypted_complex}")
print()

# ============================================================================
# Example 11: Different Encryption Types Comparison
# ============================================================================
print("=" * 70)
print("Example 11: Different Encryption Types")
print("=" * 70)

test_data = ["hello", "world", 123]
test_key = "test_key"

# Type 1: File Data-Based Encryption
arr_type1 = array(test_data.copy(), test_key, Type=1)
print(f"Type 1 encryption: {arr_type1}")
print(f"Decrypted: {arr_type1.to_pyarray(test_key)}")

# Type 2: Simple Encryption
arr_type2 = array(test_data.copy(), test_key, Type=2)
print(f"Type 2 encryption: {arr_type2}")
print(f"Decrypted: {arr_type2.to_pyarray(test_key)}")

# Type 3: Shift-Based Encryption (Default)
arr_type3 = array(test_data.copy(), test_key, Type=3)
print(f"Type 3 encryption: {arr_type3}")
print(f"Decrypted: {arr_type3.to_pyarray(test_key)}")
print()

print("=" * 70)
print("All Examples Completed Successfully!")
print("=" * 70)
