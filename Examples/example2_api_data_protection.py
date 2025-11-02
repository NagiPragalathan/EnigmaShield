"""
Example 2: API Data Protection
===============================
This example shows how to encrypt API responses and requests.
Useful for protecting sensitive data in transit or at rest.
"""

from EnigmaShield.CryptoTypes import array, Dict, String, Keys
from EnigmaShield.CryptoBloom import generate_keypair, RSAencrypt, RSAdecrypt

class SecureAPIClient:
    """A secure API client that encrypts all communication."""
    
    def __init__(self, encryption_type=3):
        """
        Initialize API client with encryption.
        
        Args:
            encryption_type: 1=File-based, 2=Simple, 3=Shift-based (default), 4=RSA
        """
        self.encryption_type = encryption_type
        
        if encryption_type == 4:
            # Generate RSA keypair for asymmetric encryption
            self.public_key, self.private_key = generate_keypair()
            print(f"[SETUP] RSA Keys generated")
            print(f"  Public Key (e, n): {self.public_key}")
        else:
            # Use symmetric encryption
            self.api_key = "api_secret_key_2024"
            print(f"[SETUP] Using symmetric encryption (Type {encryption_type})")
    
    def encrypt_request(self, data):
        """Encrypt API request data."""
        print(f"\n[REQUEST] Encrypting request data...")
        
        if self.encryption_type == 4:
            # RSA encryption
            encrypted_data = []
            for item in str(data):
                encrypted_data.append(RSAencrypt(item, self.public_key))
            print(f"[OK] Request encrypted with RSA")
            return encrypted_data
        else:
            # Symmetric encryption
            encrypted_array = array(data, Key=self.api_key, Type=self.encryption_type)
            print(f"[OK] Request encrypted")
            return encrypted_array
    
    def decrypt_response(self, encrypted_data, response_key=None):
        """Decrypt API response data."""
        print(f"\n[RESPONSE] Decrypting response data...")
        
        try:
            if self.encryption_type == 4:
                # RSA decryption
                decrypted = ""
                for item in encrypted_data:
                    decrypted += RSAdecrypt([item], self.private_key)
                print(f"[OK] Response decrypted with RSA")
                return decrypted
            else:
                # Symmetric decryption
                key = response_key or self.api_key
                if isinstance(encrypted_data, array):
                    decrypted = encrypted_data.to_pyarray(key)
                else:
                    decrypted = encrypted_data
                print(f"[OK] Response decrypted")
                return decrypted
        except Exception as e:
            print(f"[FAIL] Decryption error: {e}")
            return None
    
    def send_secure_request(self, endpoint, data):
        """Simulate sending an encrypted API request."""
        print(f"\n[API CALL] Sending request to: {endpoint}")
        
        # Encrypt the request data
        encrypted_data = self.encrypt_request(data)
        
        # Simulate API call (in real scenario, send encrypted_data to server)
        print(f"  → Encrypted data sent to server")
        print(f"  → Waiting for response...")
        
        # Simulate encrypted response (normally from server)
        return encrypted_data


class SecureAPIServer:
    """A secure API server that handles encrypted data."""
    
    def __init__(self):
        self.storage = Dict({}, Key="server_secret_key", Type=3)
        self.request_count = 0
    
    def process_request(self, encrypted_data, client_key=None):
        """Process encrypted request and return encrypted response."""
        print(f"\n[SERVER] Processing encrypted request...")
        
        self.request_count += 1
        
        # Decrypt request (in real scenario, use server's private key or shared key)
        try:
            # For demonstration, we'll simulate decryption
            print(f"  → Request #{self.request_count} received")
            print(f"  → Decrypting request...")
            
            # Simulate processing
            response_data = {
                "status": "success",
                "message": "Data processed securely",
                "request_id": self.request_count,
                "timestamp": "2024-01-15T10:30:00Z"
            }
            
            # Encrypt response
            encrypted_response = array([response_data], Key="server_secret_key", Type=3)
            print(f"  → Response encrypted and ready")
            
            return encrypted_response
        except Exception as e:
            print(f"  [FAIL] Server error: {e}")
            return None


def main():
    """Main demonstration."""
    print("=" * 70)
    print("EXAMPLE 2: API Data Protection")
    print("=" * 70)
    
    # Create secure API client (using Type 3 encryption)
    client = SecureAPIClient(encryption_type=3)
    
    # Prepare request data
    request_data = {
        "user_id": 12345,
        "action": "get_balance",
        "account_number": "ACC-789456"
    }
    
    # Send encrypted request
    encrypted_request = client.send_secure_request("/api/v1/balance", request_data)
    
    # Create server and process request
    server = SecureAPIServer()
    encrypted_response = server.process_request(encrypted_request)
    
    # Client decrypts response
    if encrypted_response:
        decrypted_response = client.decrypt_response(encrypted_response, "server_secret_key")
        print(f"\n[CLIENT] Received response:")
        if decrypted_response:
            print(f"  {decrypted_response}")
    
    # Demonstrate RSA encryption
    print("\n" + "-" * 70)
    print("Demonstrating RSA Encryption (Type 4)")
    print("-" * 70)
    
    rsa_client = SecureAPIClient(encryption_type=4)
    
    sensitive_data = "SuperSecretAPIKey12345"
    encrypted_rsa = rsa_client.encrypt_request(sensitive_data)
    print(f"\n[CLIENT] Encrypted with RSA: {str(encrypted_rsa)[:50]}...")
    
    decrypted_rsa = rsa_client.decrypt_response(encrypted_rsa)
    print(f"[CLIENT] Decrypted: {decrypted_rsa}")
    
    print("\n" + "=" * 70)
    print("Demonstration completed!")
    print("=" * 70)


if __name__ == "__main__":
    main()

