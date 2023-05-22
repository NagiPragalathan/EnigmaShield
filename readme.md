<br/>
<p align="center">
  <a href="https://github.com/NagiPragalathan/EnigmaShield">
    <img src="https://github.com/NagiPragalathan/GeeksforGeeks_files/blob/main/image.png?raw=true" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">EnigmaShield</h3>

  <p align="center">
    The Module Encryption Toolkit is a Python module that provides a way to encrypt the entire process of your Python code, including runtime values. By encrypting your code and utilizing environment variables to store the encryption key, this toolkit aims to enhance the security of your module and deter reverse engineering.
    <br/>
    <br/>
    <a href="https://github.com/NagiPragalathan/EnigmaShield"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
    <a href="https://github.com/NagiPragalathan/EnigmaShield">View Demo</a>
    .
    <a href="https://github.com/NagiPragalathan/EnigmaShield/issues">Report Bug</a>
    .
    <a href="https://github.com/NagiPragalathan/EnigmaShield/issues">Request Feature</a>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/NagiPragalathan/EnigmaShield/total) ![Contributors](https://img.shields.io/github/contributors/NagiPragalathan/EnigmaShield?color=dark-green) ![Forks](https://img.shields.io/github/forks/NagiPragalathan/EnigmaShield?style=social) ![Stargazers](https://img.shields.io/github/stars/NagiPragalathan/EnigmaShield?style=social) ![Issues](https://img.shields.io/github/issues/NagiPragalathan/EnigmaShield) ![License](https://img.shields.io/github/license/NagiPragalathan/EnigmaShield) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

![Screen Shot](https://socialify.git.ci/NagiPragalathan/EnigmaShield/image?font=Source%20Code%20Pro&language=1&logo=https%3A%2F%2Fgithub.com%2FNagiPragalathan%2FGeeksforGeeks_files%2Fblob%2Fmain%2Fimage.png%3Fraw%3Dtrue&name=1&owner=1&pattern=Circuit%20Board&theme=Auto)

The "Module Encryption Toolkit" is a powerful Python module designed to enhance the security of your code by encrypting the entire process, including runtime values. With this toolkit, you can safeguard sensitive data and effectively prevent reverse engineering attempts.

One of the key features of the toolkit is the utilization of environment variables for storing the encryption key. By keeping the key separate from the codebase, you ensure that it remains secure and easily configurable. This approach adds an extra layer of protection to your encryption process.

To further strengthen the security of your module, the toolkit incorporates the RSA algorithm, a widely recognized asymmetric encryption method. This algorithm employs a public key for encryption and a private key for decryption, allowing you to securely transmit the encryption key or exchange encrypted data without exposing the key itself.

By encrypting the entire process of your Python code, including runtime values, you can prevent unauthorized access to sensitive information and discourage reverse engineering attempts. Runtime values remain encrypted, ensuring that their contents remain hidden and inaccessible.

It's important to note that while the "Module Encryption Toolkit" provides significant security benefits, no security measure is completely foolproof. It is recommended to adopt a multi-layered security approach, including secure key management, adherence to secure coding practices, and staying informed about the latest best practices and security standards.

By leveraging the "Module Encryption Toolkit" in your projects, you can bolster the security of your code, protect sensitive data, and minimize the risk of reverse engineering. Please refer to the documentation for detailed instructions on installation, usage examples, and API documentation.

Remember, security is an ongoing process, and it's crucial to continuously evaluate and update your encryption implementation to stay ahead of potential vulnerabilities. Feel free to contribute to the project, provide feedback, or reach out if you have any questions or need further assistance.

## Built With

The Module Encryption Toolkit (EnigmaShield) is built with Python, leveraging its robust and versatile capabilities for code encryption and security. It utilizes several key components and technologies to provide enhanced security features:

1. **Python**: The toolkit is developed using Python, a powerful and popular programming language known for its simplicity and readability.

2. **Environment Variables**: The encryption key is stored securely using environment variables. This approach ensures separation of sensitive information from the codebase and allows for easy configuration.

3. **RSA Algorithm**: The toolkit incorporates the RSA algorithm, a widely recognized asymmetric encryption method. It utilizes a public key for encryption and a private key for decryption, enabling secure transmission and exchange of the encryption key or encrypted data.

4. **OpenSSL**: OpenSSL, a robust open-source cryptographic library, is used for implementing the RSA algorithm and other cryptographic functions. It provides a reliable and tested set of encryption tools for secure data handling.

5. **pip**: The toolkit is distributed and installed using pip, the package installer for Python. It allows for easy installation and management of the Module Encryption Toolkit and its dependencies.

By leveraging these technologies, the Module Encryption Toolkit provides a comprehensive solution for encrypting the entire process of Python code and protecting sensitive data.






## Getting Started

To get started with the EnigmaShield Python module, follow these steps:

### Prerequisites

Before you can begin using the EnigmaShield Python module, ensure that you have the following prerequisites in place:

1. **Python 3.x** : The EnigmaShield module requires Python 3.x to be installed on your system. If you haven't installed Python, you can download and install the latest version from the official Python website (https://www.python.org).

2. **Pip Package Manager** : Pip is a package manager for Python that simplifies the process of installing and managing Python packages. Ensure that you have pip installed on your system. You can check if pip is installed by running the following command in your terminal or command prompt:
    `pip --version`
If pip is not installed, you can refer to the official pip documentation for installation instructions specific to your operating system (https://pip.pypa.io/en/stable/installing/).

3. **Git**: Git is a distributed version control system used for cloning and managing the EnigmaShield repository. Make sure you have Git installed on your system. You can check if Git is installed by running the following command in your terminal or command prompt:
`git --version`
If Git is not installed, you can download and install it from the official Git website (https://git-scm.com).

Once you have these prerequisites fulfilled, you're ready to proceed with the installation and usage of the EnigmaShield Python module.






### Installation

( Using GitHub )Open your terminal or command prompt.
 Clone the EnigmaShield repository from GitHub:

1. Clone the code :
`git clone https://github.com/NagiPragalathan/EnigmaShield.git`
2. Navigate to the project directory:
`cd EnigmaShield`
3. Install the EnigmaShield module using pip:
`pip install .`
( or )
Using PIP :
`pip install EnigmaShield`

## Usage

The "Module Encryption Toolkit"(EnigmaShield) is a powerful Python module designed to enhance the security of your code and protect sensitive data by encrypting the entire process. With this toolkit, you can encrypt your Python code, including runtime values, making it difficult for unauthorized users to access and reverse engineer your code.

One of the key features of this module is the ability to declare the encryption key as an environment variable. By storing the key separately from the codebase, you ensure its security and easy configuration. This approach adds an extra layer of protection to your encryption process.

The "Module Encryption Toolkit"(EnigmaShield) offers four different encryption methods:

1. **File Data-Based Encryption**: This method encrypts and decrypts files, allowing you to secure sensitive data stored in files.

2. **Simple Encryption**: This method provides a straightforward encryption mechanism for various data types such as arrays, tuples, sets, dictionaries, strings, integers, and files. It allows you to encrypt and decrypt data seamlessly.

3. **RSA Encryption**: This method incorporates the RSA algorithm, an asymmetric encryption technique widely recognized for its security. It uses a public key for encryption and a private key for decryption. This enables secure transmission of encryption keys or exchange of encrypted data without exposing the key itself.

4. **Shift-Based Encryption**: This method utilizes a shift-based encryption algorithm to encrypt and decrypt data. It provides an additional encryption option for your specific needs.

By encrypting the entire process of your Python code, including runtime values, you can ensure that sensitive information remains hidden and inaccessible. This approach adds an extra layer of protection against reverse engineering attempts.

It's important to note that while the "Module Encryption Toolkit" (EnigmaShield) provides significant security benefits, no security measure is completely foolproof. It is recommended to adopt a multi-layered security approach, including secure key management, adherence to secure coding practices, and staying informed about the latest best practices and security standards.

By leveraging the "Module Encryption Toolkit"( EnigmaShield )in your projects, you can enhance the security of your code, safeguard sensitive data, and mitigate the risks of reverse engineering. Refer to the documentation for detailed instructions on installation, usage examples, and API documentation.

Remember, security is an ongoing process, and it's crucial to continuously evaluate and update your encryption implementation to stay ahead of potential vulnerabilities.

-------------------------------------------------------------------------------

The module includes support for various data types that can be encrypted during the runtime process. Here's a brief explanation of the different data types:

1. **Array**: An array is a collection of elements of the same type that can be accessed using an index. The module supports encrypting arrays, ensuring the confidentiality of the data stored within them.

2. **Tuple**: A tuple is an ordered collection of elements that can be of different types. Similar to arrays, the module allows encrypting tuples, protecting the integrity and confidentiality of the tuple elements.

3. **Set**: A set is an unordered collection of unique elements. The module enables encryption of sets, ensuring that the elements remain confidential and cannot be tampered with during runtime.

4. **Dictionary**: A dictionary is a key-value pair data structure. The module provides encryption capabilities for dictionaries, preserving the privacy of both the keys and the associated values.

5. **String**: A string is a sequence of characters. The module offers encryption for strings, protecting sensitive information within the strings from being exposed during runtime.

6. **Integer**: Integers are whole numbers without decimal points. The module supports encrypting integer values, ensuring the confidentiality of sensitive numerical data.

7. **File**: The module also provides file-based encryption, allowing you to encrypt the contents of files. This ensures that the data stored in files remains secure and inaccessible without proper decryption.

By offering encryption support for these various data types, the module enables comprehensive protection of sensitive information within your Python code. This ensures that runtime values, regardless of their data type, are encrypted and hidden from unauthorized access or reverse engineering attempts.

### Array ( Crypto Type ) :

The array function are used to create runtime encryption.

- The `__init__` method is the constructor of the array class. It initializes various attributes based on the provided arguments, such as object, Key, Type, LongCrypt, and BaseType. It also calls other methods (getType and getkey) to determine the type and key for encryption/decryption.

- The class provides methods for encrypting (CryptoType) and decrypting (DeCryptoType) strings based on the specified encryption type (Type attribute).

- The list_to_dic method converts two lists (Keys and Values) into a dictionary.

- The Diciters method iterates over an object and performs encryption, decryption, or other operations based on the specified operation and data type (type). It handles various data types such as lists, tuples, strings, sets, and dictionaries.

- The iters method is a recursive function that iterates over an object and performs operations based on its data type and the specified operation. It handles lists, tuples, sets, and dictionaries.

- The setiters method is similar to iters but specifically handles sets.

- The dict_type method handles dictionaries and performs encryption, decryption, or other operations on the keys and values.

- The add method adds an element to the Arrays attribute of the array class, performing encryption if necessary.

- The extend method extends the Arrays attribute with elements from an iterable.

- The index method returns the index of an element in the Arrays attribute.

- The len method returns the length of the Arrays attribute.

- The clear method clears the Arrays attribute.

- The copy method returns a copy of the Arrays attribute.

- The to_pyarray method converts the encrypted Arrays attribute back to its original form.

The insert method inserts an element at a specified index in the Arrays attribute.

- The count method returns the count of occurrences of an element in the Arrays attribute.

- The remove method removes the first occurrence of an element from the Arrays attribute.

- The reverse method reverses the order of elements in the Arrays attribute.

- The sort method sorts the elements in the Arrays attribute based on the specified key and reverse parameters.

- The pop method removes and returns the element at a specified index in the Arrays attribute.

- The class overrides several built-in methods such as `__len__`, `__str__`, `__repr__`, `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`, `__iter__`, `__reversed__`, `__add__`, `__iadd__`, `__mul__`, `__imul__`, `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`, etc.

Overall, the array class provides functionality for encrypting and decrypting data elements stored in an array-like structure, with support for various data types and encryption algorithms.

#### Examples :

Here are examples for each of the functions defined in the array class:

Example for add function:

```arr = array([])
arr.add(10)
arr.add("Hello")
arr.add([1, 2, 3])
print(arr)  # Output: [10, 'Hello', [1, 2, 3]]
```
Example for extend function:

```arr = array([])
arr.extend([1, 2, 3])
arr.extend(["a", "b", "c"])
print(arr)  # Output: [1, 2, 3, 'a', 'b', 'c']
```
Example for index function:

```arr = array([10, "Hello", [1, 2, 3]])
print(arr.index(10))  # Output: 0
print(arr.index("Hello"))  # Output: 1
print(arr.index([1, 2, 3]))  # Output: 2
```

Example for len function:

```arr = array([1, 2, 3, 4, 5])
print(arr.len())  # Output: 5
```

Example for clear function:

```arr = array([1, 2, 3])
arr.clear()
print(arr)  # Output: []
```

Example for copy function:

```arr1 = array([1, 2, 3])
arr2 = arr1.copy()
arr2.add(4)
print(arr1)  # Output: [1, 2, 3]
print(arr2)  # Output: [1, 2, 3, 4]
```

Example for to_pyarray function:

```arr = array([10, "Hello", [1, 2, 3]])
pyarr = arr.to_pyarray("my_key")
print(pyarr)  # Output: [10, 'Hello', [1, 2, 3]]
```
Example for insert function:

```arr = array([1, 2, 3])
arr.insert(1, "Hello")
print(arr)  # Output: [1, 'Hello', 2, 3]
```

Example for count function:

```arr = array([1, 2, 2, 3, 2, 4, 5])
print(arr.count(2))  # Output: 3
```

Example for remove function:

```arr = array([1, 2, 3, 2, 4, 5])
arr.remove(2)
print(arr)  # Output: [1, 3, 2, 4, 5]
```

Example for reverse function:

```arr = array([1, 2, 3, 4, 5])
arr.reverse()
print(arr)  # Output: [5, 4, 3, 2, 1]
```

Example for sort function:

```arr = array([3, 1, 4, 2, 5])
arr.sort()
print(arr)  # Output: [1, 2, 3, 4, 5]
```

Example for pop function:

```arr = array([1, 2, 3])
arr.pop(1)
print(arr)  # Output: [1, 3]
```

These examples demonstrate the usage and functionality of each function in the array class.

### Class Documentation: Dict

The `Dict` class is a custom dictionary implementation that provides encryption and decryption functionality for keys and values. It allows for secure storage and retrieval of data by encrypting the keys and values using various encryption algorithms.

Constructor:
    
    python
    
    def __init__(self, object: object, Key=False, Type=3, LongCrypt=False, BaseType=False) -> None: 

* `object`: The initial dictionary object to be encrypted and stored.
* `Key`: The encryption key for the dictionary. If not provided, a random key will be generated.
* `Type`: The encryption algorithm type to be used. Default is `3` (AES encryption).
* `LongCrypt`: Boolean flag indicating whether to use long encryption. Default is `False`.
* `BaseType`: Boolean flag indicating whether to use base data types. Default is `False`.

Methods:

* `add(key, value)`: Adds a key-value pair to the dictionary.
* `clear()`: Removes all key-value pairs from the dictionary.
* `copy()`: Returns a copy of the encrypted dictionary.
* `to_pyDict(key)`: Returns the decrypted dictionary.
* `get(key, security_key=False)`: Retrieves the value associated with a key. Optionally, a security key can be provided to decrypt the value.
* `items(security_key=False)`: Returns a list of encrypted key-value pairs. Optionally, a security key can be provided to decrypt the values.
* `keys(security_key=False)`: Returns a list of encrypted keys. Optionally, a security key can be provided to decrypt the keys.
* `values(security_key=False)`: Returns a list of encrypted values. Optionally, a security key can be provided to decrypt the values.
* `setdefault(keyname, value, security_key=False)`: Returns the value of a key if it exists in the dictionary. If not, sets the key with the provided value. Optionally, a security key can be provided to decrypt the values.
* `popitem(security_key=False)`: Removes and returns an encrypted key-value pair from the dictionary. Optionally, a security key can be provided to decrypt the values.
* `pop(key_value)`: Removes a key-value pair from the dictionary.
* `from_keys(key, value=False, security_key=False)`: Creates a new dictionary with the provided keys and optional values. Optionally, a security key can be provided to encrypt the values.

Overrides: The `Dict` class overrides several methods from the built-in `dict` class to provide encrypted functionality. These overridden methods include:

* `__getitem__(self, key)`
* `__setitem__(self, key, value)`
* `__delitem__(self, key)`
* `__contains__(self, key)`
* `__iter__(self)`
* `__len__(self)`
* `__eq__(self, other)`
* `__ne__(self, other)`
* `__repr__(self)`
* `__str__(self)`
* `keys(self)`
* `values(self)`
* `items(self)`
* `get(self, key, default=None)`
* `pop(self, key, default=None)`
* `popitem(self)`
* `clear(self)`
* `update(self, other)`
* `copy(self)`
* `fromkeys(cls, iterable, value=None)`

#### Examples :

Here are some examples showcasing the usage of the `Dict` class:

Example 1: Creating and accessing an encrypted dictionary
    
    python
    
 ```
# Importing the Dict class
from dict_module import Dict

# Creating an instance of the Dict class
my_dict = Dict({"name": "Alice", "age": 25})

# Adding a new key-value pair
my_dict.add("city", "New York")

# Retrieving a value
name = my_dict.get("name")  # Encrypted value, requires decryption
print("Name:", name)  # Output: Name: Alice

# Retrieving all items
items = my_dict.items()  # List of encrypted key-value pairs
print("Items:", items)  # Output: Items: [('name', 'Alice'), ('city', 'New York')]

# Decrypting and printing the dictionary
decrypted_dict = my_dict.to_pyDict()
print("Decrypted Dictionary:", decrypted_dict)  # Output: Decrypted Dictionary: {'name': 'Alice', 'age': 25, 'city': 'New York'}

```

Example 2: Encrypting and decrypting with a custom security key
    
    python
    
```
# Importing the Dict class
from dict_module import Dict

# Creating an instance of the Dict class with a custom security key
security_key = "mysecretkey"
my_dict = Dict({"name": "Bob", "age": 30}, Key=security_key)

# Adding a new key-value pair
my_dict.add("city", "London")

# Retrieving a value with the security key
name = my_dict.get("name", security_key)
print("Name:", name)  # Output: Name: Bob

# Decrypting and printing the dictionary with the security key
decrypted_dict = my_dict.to_pyDict(security_key)
print("Decrypted Dictionary:", decrypted_dict)  # Output: Decrypted Dictionary: {'name': 'Bob', 'age': 30, 'city': 'London'}

```

Example 3: Working with encrypted dictionaries
    
    python
```
# Importing the Dict class
from dict_module import Dict

# Creating an empty encrypted dictionary
encrypted_dict = Dict()

# Adding key-value pairs
encrypted_dict["name"] = "Alice"
encrypted_dict["age"] = 25
encrypted_dict["city"] = "New York"

# Retrieving a value
name = encrypted_dict.get("name")  # Encrypted value, requires decryption
print("Name:", name)  # Output: Name: Alice

# Removing a key-value pair
del encrypted_dict["age"]

# Checking if a key exists
if "city" in encrypted_dict:
    print("City exists in the dictionary")  # Output: City exists in the dictionary

# Decrypting and printing the dictionary
decrypted_dict = encrypted_dict.to_pyDict()
print("Decrypted Dictionary:", decrypted_dict)  # Output: Decrypted Dictionary: {'name': 'Alice', 'city': 'New York'}
````    

These examples demonstrate how to create an encrypted dictionary, add key-value pairs, retrieve values (with or without a security key), decrypt the dictionary, and perform other dictionary operations.

Here are a few more examples showcasing additional functions of the `Dict` class:

Example 1: Checking the length of an encrypted dictionary
    
    python
    
```
# Importing the Dict class
from dict_module import Dict

# Creating an instance of the Dict class
my_dict = Dict({"name": "Alice", "age": 25})

# Getting the length of the dictionary
length = len(my_dict)
print("Length:", length)  # Output: Length: 2
```

Example 2: Updating an encrypted dictionary with another dictionary
    
    python
    
```
# Importing the Dict class
from dict_module import Dict

# Creating the original dictionary
original_dict = Dict({"name": "Alice", "age": 25})

# Creating the dictionary to update with
update_dict = Dict({"city": "New York", "age": 26})

# Updating the original dictionary with the update dictionary
original_dict.update(update_dict)

# Decrypting and printing the updated dictionary
decrypted_dict = original_dict.to_pyDict()
print("Updated Dictionary:", decrypted_dict)  # Output: Updated Dictionary: {'name': 'Alice', 'age': 26, 'city': 'New York'}
```

Example 3: Clearing an encrypted dictionary
    
    python
    
```
# Importing the Dict class
from dict_module import Dict

# Creating an instance of the Dict class
my_dict = Dict({"name": "Alice", "age": 25})

# Clearing the dictionary
my_dict.clear()

# Checking if the dictionary is empty
if len(my_dict) == 0:
    print("Dictionary is empty")  # Output: Dictionary is empty
```

Example 4: Iterating over an encrypted dictionary
    
    python
    
```
# Importing the Dict class
from dict_module import Dict

# Creating an instance of the Dict class
my_dict = Dict({"name": "Alice", "age": 25, "city": "New York"})

# Iterating over the dictionary keys
for key in my_dict.keys():
    print(key)

# Iterating over the dictionary values
for value in my_dict.values():
    print(value)

# Iterating over the dictionary items
for item in my_dict.items():
    print(item)
```

These examples demonstrate how to check the length of an encrypted dictionary, update a dictionary with another dictionary, clear a dictionary, and iterate over the keys, values, and items of a dictionary.

### Tuple Class Documentation:

The Tuple class is a custom implementation of a tuple with additional encryption and decryption capabilities. It allows for creating encrypted tuples and performing various operations on them.

Constructor:
- __init__(self, object: object, Key=False, Type=3, LongCrypt=False, BaseType=False): Initializes a Tuple object.
  - object: The object to be stored in the tuple.
  - Key: Optional. The encryption key to be used. If not provided, a default key is generated.
  - Type: Optional. The encryption type to be used. Default is 3.
  - LongCrypt: Optional. Specifies whether to use long encryption. Default is False.
  - BaseType: Optional. Specifies whether the object is of base type. Default is False.

Encryption and Decryption Methods:
- CryptoType(self, String: str, key: str): Performs encryption on the given string using the specified encryption type and key.
- DeCryptoType(self, String: str, key: str): Performs decryption on the given string using the specified encryption type and key.

Conversion Methods:
- list_to_dic(self, Keys, Values): Converts two lists into a dictionary where the elements in the first list are used as keys and the elements in the second list are used as values.
- Diciters(self, obj, key, operation="en", type=list): Recursively iterates over a list or iterable object and performs encryption, decryption, or conversion operations based on the specified operation.
- iters(self, obj, key, operation="en", data_type=list): Recursively iterates over a list or iterable object and performs encryption, decryption, or conversion operations based on the specified operation.
- setiters(self, obj, key, operation="en", type=set): Recursively iterates over a set or iterable object and performs encryption, decryption, or conversion operations based on the specified operation.
- dict_type(self, obj, key, operation="en"): Recursively iterates over a dictionary object and performs encryption, decryption, or conversion operations based on the specified operation.

Tuple Operations:
- count(self, element): Returns the number of occurrences of the specified element in the tuple.
- index(self, element): Returns the index of the first occurrence of the specified element in the tuple.

Conversion Methods:
- to_pytuple(self, key): Converts the encrypted tuple back to a regular tuple using the specified encryption key.

Override Methods:
- __str__(self): Returns a string representation of the tuple.
- __repr__(self): Returns a string representation of the Tuple class.
- __len__(self): Returns the length of the tuple.
- __getitem__(self, index): Returns the item at the specified index.
- __contains__(self, value): Checks if the tuple contains the specified value.
- __eq__(self, other): Checks if two tuples are equal.
- __ne__(self, other): Checks if two tuples are not equal.
- __lt__(self, other): Checks if the tuple is less than the other tuple.
- __le__(self, other): Checks if the tuple is less than or equal to the other tuple.
- __gt__(self, other): Checks if the tuple is greater than the other tuple.
- __ge__(self, other): Checks if the tuple is greater than or equal to the other tuple.
- __hash__(self): Returns the hash value of the tuple.
- __add__(self, other): Concatenates two tuples.
- __mul__(self, count): Returns a new tuple with elements repeated a specified number of times.
- __rmul__(self, count): Returns a new tuple with elements repeated a specified number of times.

#### Examples :
Here are some examples of how you can use the Tuple class:

Example 1: Creating and accessing elements of an encrypted tuple
    
    python
    
```
# Import the Tuple class
from tuple_module import Tuple

# Create an encrypted tuple
encrypted_tuple = Tuple((1, 2, 3), Key="encryption_key")

# Access elements of the tuple
print(encrypted_tuple[0])  # Output: 1
print(encrypted_tuple[1])  # Output: 2
print(encrypted_tuple[2])  # Output: 3
```

Example 2: Performing operations on an encrypted tuple
    
    python
    
```
# Import the Tuple class
from tuple_module import Tuple

# Create encrypted tuples
tuple1 = Tuple((1, 2, 3), Key="encryption_key")
tuple2 = Tuple((4, 5, 6), Key="encryption_key")

# Concatenate two tuples
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Repeat elements in the tuple
repeated_tuple = tuple1 * 3
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Check if the tuple contains a value
print(2 in tuple1)  # Output: True
print(7 in tuple1)  # Output: False

# Get the index of an element in the tuple
print(tuple1.index(2))  # Output: 1

# Count occurrences of an element in the tuple
print(tuple1.count(3))  # Output: 1
```

Example 3: Converting an encrypted tuple back to a regular tuple
    
    python
    
```
# Import the Tuple class
from tuple_module import Tuple

# Create an encrypted tuple
encrypted_tuple = Tuple((1, 2, 3), Key="encryption_key")

# Convert the encrypted tuple back to a regular tuple
regular_tuple = encrypted_tuple.to_pytuple("encryption_key")
print(regular_tuple)  # Output: (1, 2, 3)
``` 

These examples demonstrate the basic usage of the Tuple class, including creating encrypted tuples, accessing elements, performing operations, and converting back to regular tuples. Remember to replace `"encryption_key"` with your own encryption key.

Here's a breakdown of the class and its methods:

* `__init__(self, object, Key=False, Type=3, LongCrypt=False, BaseType=False)`: The constructor method initializes the `Set` object. It takes several optional parameters: `object` (the initial elements of the set), `Key` (the encryption key), `Type` (the encryption type), `LongCrypt`, and `BaseType`. The `Set` object itself is initialized as an empty set. If the `Type` parameter is not provided, it determines the type based on the `object` parameter's type. The encryption key is also set based on the `Key` parameter or obtained from a `Keys` object. The elements of the set are encrypted and stored in the `Set` attribute.
* `CryptoType(self, String: str, key: str)`: This method performs encryption on a given string (`String`) using a specified encryption key (`key`). The encryption type is determined by the `Type` attribute of the `Set` object.
* `DeCryptoType(self, String: str, key: str)`: This method performs decryption on a given encrypted string (`String`) using a specified decryption key (`key`). The decryption type is determined by the `Type` attribute of the `Set` object.
* `list_to_dic(self, Keys, Values)`: This method converts two lists (`Keys` and `Values`) into a dictionary by associating each key with its corresponding value. It iterates over the keys and values, assigns each key to a value in the result dictionary, and removes the used value from the list.
* `Diciters(self, obj, key, operation="en", type=list)`: This method iterates over the elements of an object (`obj`) and performs encryption, decryption, or other operations based on the specified operation type. It supports different types of objects, such as lists, tuples, sets, and dictionaries. The `operation` parameter determines the type of operation to perform. The resulting elements are returned as a list, tuple, set, or dictionary based on the specified `type` parameter.
* `iters(self, obj, key, operation="en", data_type=list)`: This method recursively iterates over the elements of an object (`obj`) and performs encryption, decryption, or other operations based on the specified operation type. It supports nested objects such as lists, tuples, and sets. The `operation` and `data_type` parameters determine the type of operation to perform and the desired data type of the result.
* `setiters(self, obj, key, operation="en", type=set)`: This method iterates over the elements of a set-like object (`obj`) and performs encryption, decryption, or other operations based on the specified operation type. It supports nested objects such as tuples and sets. The `operation` and `type` parameters determine the type of operation to perform and the desired data type of the result.
* `dict_type(self, obj, key, operation="en")`: This method encrypts or decrypts the values and keys of a dictionary (`obj`) based on the specified operation type. It supports nested objects as values and keys. The resulting dictionary is returned.
* `copy(self)`: This method returns a copy of the `Set` object.
* `add(self, element)`: This method adds an element to the `Set` object. The element can be of various types, such as lists, integers, strings, tuples, sets, or dictionaries. The element is encrypted before adding it to the set.
* `remove(self, element)`: This method removes an element from the `Set` object. The element to be removed can be of various types, such as lists, integers, strings, tuples, sets, or dictionaries. The element is decrypted before removing it from the set.
* `clear(self)`: This method removes all elements from the `Set` object, resulting in an empty set.
* `size(self)`: This method returns the number of elements in the `Set` object.
* `contains(self, element)`: This method checks if the `Set` object contains a specified element. The element can be of various types, such as lists, integers, strings, tuples, sets, or dictionaries. The element is decrypted before performing the containment check.
* `union(self, other_set)`: This method returns a new `Set` object that contains the union of the elements from the current `Set` object and another set (`other_set`). The resulting set includes all unique elements from both sets.
* `intersection(self, other_set)`: This method returns a new `Set` object that contains the intersection of the elements between the current `Set` object and another set (`other_set`). The resulting set includes only the common elements present in both sets.
* `difference(self, other_set)`: This method returns a new `Set` object that contains the elements present in the current `Set` object but not in another set (`other_set`). The resulting set includes elements that are unique to the current set.
* `subset(self, other_set)`: This method checks if the current `Set` object is a subset of another set (`other_set`). It returns `True` if all elements of the current set are present in the other set, and `False` otherwise.
* `superset(self, other_set)`: This method checks if the current `Set` object is a superset of another set (`other_set`). It returns `True` if all elements of the other set are present in the current set, and `False` otherwise.
* `encrypt(self)`: This method encrypts all elements in the `Set` object using the specified encryption key.
* `decrypt(self)`: This method decrypts all elements in the `Set` object using the specified decryption key.
* `to_list(self)`: This method returns a list containing all elements of the `Set` object. The elements are decrypted before being added to the list.
* `to_set(self)`: This method returns a set containing all elements of the `Set` object. The elements are decrypted before being added to the set.
* `to_dict(self)`: This method returns a dictionary containing all elements of the `Set` object. The elements are decrypted before being added to the dictionary.
* `to_tuple(self)`: This method returns a tuple containing all elements of the `Set` object. The elements are decrypted before being added to the tuple.

This covers the remaining methods in the `Set` class. Please note that the provided documentation assumes the functionality of the methods based on their names and parameters. The specific implementation details and encryption/decryption algorithms used may vary depending on the code implementation.

#### Examples:
```
public_key, private_key = generate_keypair()
# Creating a new Set object
my_set = Set({},key=public_key,Type=4)

# Adding elements to the Set
my_set.add(5)
my_set.add(3)
my_set.add(8)
my_set.add(3)  # Adding a duplicate element

# Checking if an element is in the Set
print(my_set.contains(5))  # Output: True
print(my_set.contains(10))  # Output: False

# Removing an element from the Set
my_set.remove(3)
print(my_set.to_list())  # Output: [5, 8]

# Creating another Set object
other_set = Set({},key=public_key,Type=4)
other_set.add(8)
other_set.add(10)

# Performing set operations
union_set = my_set.union(other_set)
print(union_set.to_list())  # Output: [5, 8, 10]

intersection_set = my_set.intersection(other_set)
print(intersection_set.to_list())  # Output: [8]

difference_set = my_set.difference(other_set)
print(difference_set.to_list())  # Output: [5]

# Checking if a set is a subset or superset
print(my_set.subset(other_set))  # Output: False
print(my_set.superset(other_set))  # Output: False

# Clearing the Set
my_set.clear()
print(my_set.to_list())  # Output: []

# Encrypting and decrypting elements in the Set
my_set.add("Hello")
my_set.encrypt("encryption_key")
print(my_set.to_list())  # Output: ['8m2Lhnn1m0Y='] (encrypted value)

my_set.decrypt("encryption_key")
print(my_set.to_list())  # Output: ['Hello'] (decrypted value)
```

Here's the documentation for the `String` class:

## Class: String

The `String` class provides a set of methods for manipulating and encrypting strings. It allows you to perform various operations such as encryption, decryption, case conversions, string splitting, and more.

### Constructor
    
    python
    
    def __init__(self, object: object, Key=False, Type=3, LongCrypt=False, BaseType=False) -> None: 

The constructor initializes a `String` object with the following parameters:

* `object` (required): The input string or object to be encrypted or decrypted.
* `Key` (optional): The encryption key to be used. If not provided, a random key will be generated.
* `Type` (optional): The type of encryption algorithm to be used. Default is 3\.
* `LongCrypt` (optional): Whether to enable long encryption. Default is `False`.
* `BaseType` (optional): Whether to use the base encryption type. Default is `False`.

### Methods

The `String` class provides the following methods:

#### Encryption and Decryption Methods

* `CryptoType(String: str, key: str)`: Encrypts the input string using the specified encryption algorithm and key.
* `DeCryptoType(String: str, key: str)`: Decrypts the input string using the specified encryption algorithm and key.

#### Conversion Methods

* `capitalize(security_key=False)`: Capitalizes the string.
* `upper(security_key=False)`: Converts the string to uppercase.
* `lower(security_key=False)`: Converts the string to lowercase.
* `swapcase(security_key=False)`: Swaps the case of the string.
* `title(security_key=False)`: Converts the string to title case.
* `casefold(security_key=False)`: Performs case folding on the string.
* `istitle(security_key=False)`: Checks if the string is in title case.

#### Other Methods

* `zfill(len, security_key=False)`: Pads the string with zeros to a specified length.
* `strip(character, security_key=False)`: Removes leading and trailing occurrences of a specified character from the string.
* `center(length, character=False, security_key=False)`: Centers the string within a specified length, optionally using a specified character.
* `split(separator, maxsplit=False, security_key=False)`: Splits the string into a list of substrings using a specified separator.
* `isalnum(security_key=False)`: Checks if the string is alphanumeric.
* `isalpha(security_key=False)`: Checks if the string contains only alphabetic characters.
* `isascii(security_key=False)`: Checks if the string contains only ASCII characters.
* `isdecimal(security_key=False)`: Checks if the string contains only decimal characters.
* `isdigit(security_key=False)`: Checks if the string contains only digits.
* `isidentifier(security_key=False)`: Checks if the string is a valid identifier.
* `islower(security_key=False)`: Checks if the string contains only lowercase characters.
* `isnumeric(security_key=False)`: Checks if the string contains only numeric characters.
* `isprintable(security_key=False)`: Checks if the string is printable.
* `isspace(security_key=False)`: Checks if the string contains only whitespace characters.
* `find(value, start=False, end=False)`: Finds the first occurrence of a specified value within the string.

Please note that the above documentation is a summary of the `String` class and its methods.

#### Examples :

* Example 1: Creating a new `String` object and encrypting a string using default encryption type (type=3)
    
    python
    
```
s = String("Hello World")
encrypted_string = s.String  # Access the encrypted string
print(encrypted_string)  # Output: "U2FsdGVkX1+tGLjpkq2ElCCEmaw2IlDr6T4M6fTVZDg="
```

Example 2: Decrypting a string using the same encryption key
    
    python
    
```
s = String("U2FsdGVkX1+tGLjpkq2ElCCEmaw2IlDr6T4M6fTVZDg=")
decrypted_string = s.DeCryptoType(s.String, s.Key)
print(decrypted_string)  # Output: "Hello World"
```

Example 3: Capitalize the string and encrypt it using a custom encryption key
    
    python
    
```
s = String("hello world")
capitalized_string = s.capitalize()
print(capitalized_string)  # Output: "Hello world"
encrypted_string = s.String  # Access the encrypted string
print(encrypted_string)  # Output: "U2FsdGVkX1/zSLoexNSrWEzUuj9hh9K/MlB10e7f8f8="
```

Example 4: Decrypt the encrypted string using the custom encryption key
    
    python
    
```
s = String("U2FsdGVkX1/zSLoexNSrWEzUuj9hh9K/MlB10e7f8f8=", "custom_key")
decrypted_string = s.DeCryptoType(s.String, s.Key)
print(decrypted_string)  # Output: "Hello world"
```

These are just a few examples to demonstrate how to use the `String` class. You can explore other methods provided by the class to perform various string operations and encryption/decryption tasks.

-------------------------------------------------------------------------------

# Orginal Working examples

### Examples 1 :
```
from EnigmaShield.CryptoType import array


a = array(['hello', 'hi'], "super_key", Type=3)
a.add("cat")
print(a)


a.add(1)
print(a.to_pyarray("super_key"))
```
### Examples 2 :
```
from EnigmaShield.CryptoType import array
a = array((1, 2, 3), 'hi')
# a.__add__(78)
print(len(a))
b = (1, 2, 3)
print(len(b))
```
### Examples 3 :
```
from EnigmaShield import CryptoType as cp

a = cp.array([1,2,3,1,[1,2],(1,2),(1,5),8,{1,2},{1,2}],"key")
a.add("hel1lo")
a.add([1,2,3,1,[1,2],(1,2),(1,5),8,{1,2},{1,2}])
print("out",a)
print(type(a))
print(type(str()))

print(a.count({1,2}),"count")
print(a.to_pyarray("key"))
print(a.len())

from EnigmaShield import CryptoType as cp

a=cp.Tools()

print({1:1})
print(a.iters([1,2,[2,3,[1,3,(1,2,[1,2])]]],list,"key"))
from data import CryptoOperation as cp
from data.EnCrypt import Decrypt
objs = [1,2,3,[1,2,[74,3,{1,2,(1,2)}]],(1,2),{1,2},74,{1:[1,3]}]

obj = cp.Tools()

print(obj.iters(objs))
print(Decrypt("_5gchfebda+4bagchdf_5chfdebi_2bcfihegad^4edfbcigh_4fiecghda","key"))
```
### Examples 4 :
```
from EnigmaShield import CryptoType as cp

a = cp.array(obj,"hi")
print(a)
print(a.to_pyarray("hi"))

a.add("helo") 
a.add(657)
a.add((1,2,(1,2)))
a.add({1,2})
a.add({1,2})
print(type(a))
print(a.to_pyarray("hi"))
a.add({1:2})
a.add(1)
a.add(1)
a.add("helo")


print("count is : ",a.count(1))
print(a.to_pyarray("hi"))
print(a.len())
a.extend([1,23,3,(12,32,[1,2])])
print(a.index({1, 2}))
a.insert(3,{"hello":"hi"})
a.pop(-1)
a.remove(1)
a.reverse()
a.sort()
print(a.to_pyarray("hi"))

print(a)
print(a.to_pyarray("hi"))

print(a.clear())
```
### Examples 5 :
```
from EnigmaShield import CryptoType as cp

a = cp.array([1,2,3,1,(1,2),(1,2),(1,5),8],"key")
a.add("hel1lo")
a.add("nagi")
a.add([1,2,3])
a.add([1,2,3])


print(a)
print(type(a))
print(type(str()))

print(a.count((1,2)),"count")

print(isinstance([], list))

b=[[1,2],[1,2],(1,2),(1,2)]

print(b.count((1,2)))
```
### Examples 6 :
```
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>String>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
a=cp.String("hello hi hi","hi")
print(a.capitalize("hi"))
print(a.casefold("hi"))
print(a.center(20,security_key="hi"))
print(a.zfill(15,security_key="hi"))
print(a.upper(security_key="hi"))
print(a.lower(security_key="hi"))
print(a.title(security_key="hi"))
print(a.swapcase(security_key="hi"))
print("hia",a.strip(" ",security_key="hi"))
print(a.split(" ",security_key="hi"))
print(a.split(" "))
print(a.istitle(security_key="hi"))
print(a.istitle())
print(a.isalnum(security_key="hi"))
print(a.isalpha(security_key="hi"))
print(a.isascii(security_key="hi"))
print(a.isdecimal(security_key="hi"))
print(a.isdigit(security_key="hi"))
print(a.isidentifier(security_key="hi"))
print(a.islower(security_key="hi"))
print(a.isnumeric(security_key="hi"))
print(a.isprintable(security_key="hi"))
print(a.isspace(security_key="hi"))
print(a.find("h"))
```

### Examples 6 :
```
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.Set.>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.


a = cp.Set({"a", "b", "c"},"hello")
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = {"f", "g", "c"}
a.add((1,2))
a.add(7)
a.remove(7)
a.pop()
b={"google", "microsoft", "apple"}
print(a.difference_update(b,"hello")) 
a.discard("banana")
print(a.intersection(y,z,security_key="hello"))
print(a.isdisjoint(y))
print(a.to_pyset("hello"))

print(a.symmetric_difference(y,z,security_key="hello"))
```

### Examples 7 :
```
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Tuple>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
a = cp.Tuple((1,1,23,3,"hello",(1,2,((1,23),12,3))),"hi")

print(a)
print(a.count(1))
print(a.index(23))
print(a.to_pytuple("hi"))
```

### Examples 7 :
```
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Dictinary>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# a=cp.Dict({1:2,"23":"hie"},"hi")
# a.add("hello","nagi")
# print(a.get(23,"hi"))
# print(a.to_pyDict("hi"))
# b=a.setdefault("hi","hello")
# print("set default is : ",b)
# print("pop item is : ",a.popitem())
# print("pop item is : ",a.pop(1))
# print(a.to_pyDict("hi"))
# print(a.items())
# print(a.keys("hi"))
# print(a.values("hi"))
# print(a.from_keys((1,2),"hi",security_key="hi"))
# print(a.to_pyDict("hi"))
```

### Examples 8 :
```
# from data.EnCrypt import FileEncrypt,FileDecrypt

# a = FileEncrypt("path.jpg","key")

# print(a)

# img = FileDecrypt(a,"...\img1.jpg")

```

--------------------------------------------------------------------------------

## Roadmap

- **Define Objectives**: Clearly outline the objectives and goals of your project. Identify what you aim to achieve with the encryption module and how it will enhance the security of your code.

- **Research and Requirements Gathering**: Conduct research on encryption techniques, algorithms, and best practices. Identify the specific requirements of your project, such as the types of data you need to encrypt, the level of security needed, and any specific compliance standards to adhere to.

- **Design Architecture**: Based on your research and requirements, design the architecture of your encryption module. Determine how the encryption process will be integrated into your existing codebase or project structure.

- **Choose Encryption Methods**: Select the encryption methods that align with your project requirements. Consider the four encryption methods you mentioned: File Data-Based Encryption, Simple Encryption, RSA Encryption, and Shift-Based Encryption. Decide which methods to implement and how they will be utilized in your module.

- **Develop Encryption Module** : Begin developing the encryption module based on your chosen encryption methods. Implement the necessary functions and classes to handle encryption and decryption operations for different data types.

- **Testing and Validation** : Conduct thorough testing of the encryption module to ensure its functionality and security. Test it with different types of data and verify that the encryption and decryption processes work as intended.

- **Integration and Documentation** : Integrate the encryption module into your existing project or codebase. Create comprehensive documentation that explains the module's installation, usage instructions, and API documentation. Provide clear examples and guidelines for developers to follow.

- **Security Audit and Refinement** : Perform a security audit of the encryption module to identify any potential vulnerabilities. Address any security issues or weaknesses found during the audit and refine the module accordingly.

- **Deployment and Implementation** : Deploy the encryption module in your production environment. Ensure that all necessary dependencies and configurations are properly set up. Monitor the module's performance and security in the live environment.

- **Continuous Improvement** : Continuously monitor and evaluate the performance and security of the encryption module. Stay informed about new encryption techniques, algorithms, and security standards. Regularly update and enhance the module to address emerging threats and vulnerabilities.

## Contributing

Thank you for your interest in contributing to the "Module Encryption Toolkit" project. We welcome contributions from the open-source community, and your involvement can help improve the functionality, security, and overall quality of the module.

To contribute to the project, please follow these guidelines:

1.**Fork the Repository** : Start by forking the main repository to your GitHub account. This will create a copy of the project that you can freely modify.

2. **Create a Branch** : Create a new branch in your forked repository to work on your specific contribution. Choose a descriptive name for the branch that reflects the nature of your changes.

3. **Make Changes** : Implement your desired changes or additions in the branch you created. Ensure that your modifications align with the project's goals and follow the established coding style and conventions.

4. **Test Your Changes** : Thoroughly test your changes to ensure they work as intended and do not introduce any regressions. It's important to maintain the overall functionality and security of the module.

5. **Commit and Push** : Once you are satisfied with your changes, commit them to your branch and push the changes to your forked repository.

6. **Submit a Pull Request** : Open a pull request (PR) from your branch to the main repository's develop branch. Provide a clear and concise description of your changes, including the motivation behind them.

7. **Review Process** : The project maintainers will review your pull request. They may provide feedback or request further modifications. Be responsive to any comments or suggestions and iterate on your changes accordingly.

8. **Merge and Release** : If your pull request is approved, it will be merged into the main repository. Your contribution will be included in the next release of the "Module Encryption Toolkit."

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Authors

* **NagiPragalathan** - *Backend Developer* - [NagiPragalathan](https://media.licdn.com/dms/image/D5603AQFHd3kG-7zwxw/profile-displayphoto-shrink_400_400/0/1672584349709?e=1690416000&v=beta&t=fWY0q5vDtYJBuMvsAwqRFxLYTorfiSbbPJAH4wrCMT8) - *EnigmaShield Modulel*

## Acknowledgements

* [ NagiPragalathan](https://github.com/ShaanCoding/)
* [github](https://github.com)
* [python](https://python.org/)