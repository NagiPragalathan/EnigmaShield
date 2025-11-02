"""
Example 5: Secure Password Manager
==================================
A complete password manager application using EnigmaShield.
Demonstrates real-world encryption for sensitive credential storage.
"""

from EnigmaShield.CryptoTypes import Dict, String, array, Keys
from EnigmaShield.CryptoBloom import generate_keypair
import getpass
import hashlib

class SecurePasswordManager:
    """A secure password manager with encrypted storage."""
    
    def __init__(self, master_password):
        """
        Initialize password manager with master password.
        
        Args:
            master_password: Master password for accessing the vault
        """
        # Generate encryption key from master password
        self.master_key = self._derive_key(master_password)
        self.vault = Dict({}, Key=self.master_key, Type=3)
        self.credentials = []
        
        print(f"[VAULT] Password manager initialized")
        print(f"  Master key derived from password")
    
    def _derive_key(self, password):
        """Derive encryption key from master password."""
        # In production, use proper key derivation (PBKDF2, Argon2, etc.)
        hash_obj = hashlib.sha256(password.encode())
        return hash_obj.hexdigest()[:32]  # Use first 32 chars as key
    
    def add_credential(self, service, username, password, notes=""):
        """
        Add a new credential to the vault.
        
        Args:
            service: Service name (e.g., "gmail.com")
            username: Username or email
            password: Password to encrypt
            notes: Additional notes (optional)
        """
        print(f"\n[ADD] Adding credential for: {service}")
        
        # Encrypt password and notes
        encrypted_password = String(password, Key=self.master_key, Type=3)
        encrypted_username = String(username, Key=self.master_key, Type=3)
        encrypted_notes = String(notes, Key=self.master_key, Type=3) if notes else ""
        
        # Create credential entry
        credential_id = f"{service}_{username}"
        
        credential_data = {
            "service": service,
            "username": str(encrypted_username),
            "password": str(encrypted_password),
            "notes": str(encrypted_notes) if encrypted_notes else ""
        }
        
        # Store in encrypted vault
        self.vault.add(credential_id, credential_data)
        self.credentials.append({
            "id": credential_id,
            "service": service,
            "username": username  # Store unencrypted for display only
        })
        
        print(f"  [OK] Credential encrypted and stored")
        print(f"    Service: {service}")
        print(f"    Username: {username}")
    
    def get_credential(self, service, username=None):
        """
        Retrieve and decrypt a credential.
        
        Args:
            service: Service name
            username: Username (optional, retrieves first match if not provided)
        """
        print(f"\n[GET] Retrieving credential for: {service}")
        
        try:
            if username:
                credential_id = f"{service}_{username}"
            else:
                # Find first matching service
                matching = [c for c in self.credentials if c["service"] == service]
                if not matching:
                    print(f"  [FAIL] No credentials found for {service}")
                    return None
                credential_id = matching[0]["id"]
            
            encrypted_data = self.vault.get(credential_id)
            
            if encrypted_data:
                # Decrypt credential data
                encrypted_username = String(encrypted_data.get("username", ""),
                                          Key=self.master_key, Type=3)
                encrypted_password = String(encrypted_data.get("password", ""),
                                          Key=self.master_key, Type=3)
                encrypted_notes = String(encrypted_data.get("notes", ""),
                                       Key=self.master_key, Type=3) if encrypted_data.get("notes") else None
                
                credential = {
                    "service": encrypted_data.get("service", service),
                    "username": encrypted_username.topystr(self.master_key),
                    "password": encrypted_password.topystr(self.master_key),
                    "notes": encrypted_notes.topystr(self.master_key) if encrypted_notes else ""
                }
                
                print(f"  [OK] Credential decrypted")
                print(f"    Service: {credential['service']}")
                print(f"    Username: {credential['username']}")
                print(f"    Password: {'*' * len(credential['password'])}")
                if credential['notes']:
                    print(f"    Notes: {credential['notes']}")
                
                return credential
            else:
                print(f"  [FAIL] Credential not found")
                return None
        except Exception as e:
            print(f"  [FAIL] Error: {e}")
            return None
    
    def list_credentials(self):
        """List all stored credentials (service and username only)."""
        print(f"\n[LIST] Stored Credentials:")
        print("-" * 70)
        
        if not self.credentials:
            print("  No credentials stored")
            return
        
        for i, cred in enumerate(self.credentials, 1):
            print(f"  {i}. {cred['service']:20s} - {cred['username']}")
    
    def delete_credential(self, service, username):
        """Delete a credential from the vault."""
        print(f"\n[DELETE] Removing credential: {service} / {username}")
        
        credential_id = f"{service}_{username}"
        
        # Remove from credentials list
        self.credentials = [c for c in self.credentials if c["id"] != credential_id]
        
        # Remove from vault (would need to work with decrypted dict)
        print(f"  [OK] Credential removed from list")
        print(f"    Note: Fully removing from encrypted vault requires decryption")
    
    def search_credentials(self, query):
        """Search for credentials by service name or username."""
        print(f"\n[SEARCH] Searching for: '{query}'")
        
        results = []
        for cred in self.credentials:
            if query.lower() in cred["service"].lower() or query.lower() in cred["username"].lower():
                results.append(cred)
        
        if results:
            print(f"  Found {len(results)} matching credential(s):")
            for cred in results:
                print(f"    - {cred['service']} / {cred['username']}")
        else:
            print(f"  No matches found")
        
        return results


def main():
    """Main demonstration."""
    print("=" * 70)
    print("EXAMPLE 5: Secure Password Manager")
    print("=" * 70)
    
    # Simulate master password (in real app, get from user input)
    master_password = "MySecureMasterPassword123!"
    
    # Create password manager
    pm = SecurePasswordManager(master_password)
    
    # Add credentials
    print("\n" + "-" * 70)
    print("Adding Credentials:")
    print("-" * 70)
    
    pm.add_credential(
        service="gmail.com",
        username="alice@example.com",
        password="SuperSecureGmailPass456!",
        notes="Personal email account"
    )
    
    pm.add_credential(
        service="github.com",
        username="alice_dev",
        password="GitHubToken_xyz789",
        notes="Developer account"
    )
    
    pm.add_credential(
        service="banking.com",
        username="alice.bank",
        password="BankPassword2024!",
        notes="Primary banking account"
    )
    
    pm.add_credential(
        service="aws.amazon.com",
        username="alice@example.com",
        password="AWS_AccessKey_SECRET123",
        notes="AWS Console access"
    )
    
    # List all credentials
    pm.list_credentials()
    
    # Search credentials
    print("\n" + "-" * 70)
    print("Searching Credentials:")
    print("-" * 70)
    
    pm.search_credentials("gmail")
    pm.search_credentials("alice")
    
    # Retrieve credentials
    print("\n" + "-" * 70)
    print("Retrieving Credentials:")
    print("-" * 70)
    
    pm.get_credential("gmail.com")
    pm.get_credential("github.com", "alice_dev")
    pm.get_credential("banking.com")
    
    # Delete credential
    print("\n" + "-" * 70)
    print("Deleting Credential:")
    print("-" * 70)
    
    pm.delete_credential("aws.amazon.com", "alice@example.com")
    pm.list_credentials()
    
    print("\n" + "=" * 70)
    print("Demonstration completed!")
    print("=" * 70)
    print("\nSecurity Notes:")
    print("  - Master password should be strong and unique")
    print("  - In production, use proper key derivation (PBKDF2/Argon2)")
    print("  - Consider adding two-factor authentication")
    print("  - Regularly backup encrypted vault")


if __name__ == "__main__":
    main()

