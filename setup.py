from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.13'
DESCRIPTION = 'The "Module Encryption Toolkit" is a powerful Python module designed to enhance the security of your code by encrypting the entire process, including runtime values. With this toolkit, you can safeguard sensitive data and effectively prevent reverse engineering attempts.'
LONG_DESCRIPTION = 'The Module Encryption Toolkit is a Python module that provides a way to encrypt the entire process of your Python code, including runtime values. By encrypting your code and utilizing environment variables to store the encryption key, this toolkit aims to enhance the security of your module and deter reverse engineering.'

# Setting up
setup(
    name="EnigmaShield",
    version='0.0.1',
    author="NagiPragalathan N",
    author_email="<nagipragalathan@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[     ],  # Replace with actual dependencies
    keywords=['python', 'cryptography', 'encryption', 'decryption', 'security',"Cryptosystem","Cipher","Key","Key management","Key exchange","Public key cryptography","Symmetric key cryptography","Asymmetric key cryptography","Hash function","Digital signatures","Secure communication","Authentication","Confidentiality","Integrity","Non-repudiation","Cryptanalysis"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

