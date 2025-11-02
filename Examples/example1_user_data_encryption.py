"""
Example 1: User Data Encryption
================================
This example demonstrates encrypting and storing user data securely.
Perfect for applications that need to protect sensitive user information.
"""

from EnigmaShield.CryptoTypes import Dict, String, array, Keys

# Set a global encryption key (in production, use environment variables)
keys_manager = Keys()
keys_manager.setkey("my_secure_app_key_2024")
keys_manager.setType(3)  # Use Type 3 encryption (Shift-Based)

class SecureUserDatabase:
    """A secure user database that encrypts all user data."""
    
    def __init__(self):
        # Initialize encrypted storage for user data
        self.users = Dict({}, Key="my_secure_app_key_2024", Type=3)
        self.user_profiles = {}
    
    def register_user(self, username, password, email, age):
        """Register a new user with encrypted data."""
        print(f"\n[REGISTER] Registering user: {username}")
        
        # Encrypt sensitive data
        encrypted_password = String(password, Key="my_secure_app_key_2024", Type=3)
        encrypted_email = String(email, Key="my_secure_app_key_2024", Type=3)
        encrypted_age = String(str(age), Key="my_secure_app_key_2024", Type=3)
        
        # Store encrypted user data
        user_data = {
            "username": username,
            "password": str(encrypted_password),
            "email": str(encrypted_email),
            "age": str(encrypted_age)
        }
        
        # Add to encrypted dictionary
        self.users.add(username, user_data)
        
        print(f"[OK] User registered successfully!")
        print(f"  - Encrypted password: {str(encrypted_password)[:30]}...")
        print(f"  - Encrypted email: {str(encrypted_email)[:30]}...")
    
    def verify_user(self, username, password):
        """Verify user credentials."""
        print(f"\n[VERIFY] Verifying user: {username}")
        
        try:
            # Get encrypted user data
            user_data_encrypted = self.users.get(username)
            
            if user_data_encrypted:
                # Decrypt password for verification
                encrypted_pwd = String(user_data_encrypted.get("password", ""), 
                                     Key="my_secure_app_key_2024", Type=3)
                decrypted_password = encrypted_pwd.topystr("my_secure_app_key_2024")
                
                if decrypted_password == password:
                    print(f"[OK] Authentication successful!")
                    return True
                else:
                    print(f"[FAIL] Authentication failed: Invalid password")
                    return False
            else:
                print(f"[FAIL] User not found")
                return False
        except Exception as e:
            print(f"[ERROR] Error: {e}")
            return False
    
    def get_user_profile(self, username):
        """Retrieve and decrypt user profile."""
        print(f"\n[PROFILE] Retrieving profile for: {username}")
        
        try:
            user_data_encrypted = self.users.get(username)
            
            if user_data_encrypted:
                # Decrypt all user data
                encrypted_email = String(user_data_encrypted.get("email", ""),
                                       Key="my_secure_app_key_2024", Type=3)
                encrypted_age = String(user_data_encrypted.get("age", ""),
                                     Key="my_secure_app_key_2024", Type=3)
                
                profile = {
                    "username": username,
                    "email": encrypted_email.topystr("my_secure_app_key_2024"),
                    "age": encrypted_age.topystr("my_secure_app_key_2024")
                }
                
                print(f"[OK] Profile retrieved:")
                print(f"  - Email: {profile['email']}")
                print(f"  - Age: {profile['age']}")
                return profile
            else:
                print(f"[FAIL] User not found")
                return None
        except Exception as e:
            print(f"[ERROR] Error: {e}")
            return None


def main():
    """Main demonstration."""
    print("=" * 70)
    print("EXAMPLE 1: User Data Encryption")
    print("=" * 70)
    
    # Create secure database
    db = SecureUserDatabase()
    
    # Register users
    db.register_user("alice", "SecurePass123!", "alice@example.com", 28)
    db.register_user("bob", "MyPassword456", "bob@example.com", 35)
    db.register_user("charlie", "StrongP@ss789", "charlie@example.com", 22)
    
    # Verify users
    db.verify_user("alice", "SecurePass123!")
    db.verify_user("alice", "WrongPassword")
    
    # Retrieve profiles
    db.get_user_profile("alice")
    db.get_user_profile("bob")
    
    print("\n" + "=" * 70)
    print("Demonstration completed!")
    print("=" * 70)


if __name__ == "__main__":
    main()

