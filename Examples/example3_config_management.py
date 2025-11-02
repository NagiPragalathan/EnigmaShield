"""
Example 3: Secure Configuration Management
===========================================
This example demonstrates encrypting application configuration files.
Perfect for protecting API keys, database credentials, and settings.
"""

from EnigmaShield.CryptoTypes import Dict, String, array
import json
import os

class SecureConfigManager:
    """Manages encrypted application configuration."""
    
    def __init__(self, config_key="app_config_key_2024", encryption_type=3):
        """
        Initialize secure config manager.
        
        Args:
            config_key: Encryption key for configuration
            encryption_type: Encryption type (1-4)
        """
        self.config_key = config_key
        self.encryption_type = encryption_type
        self.config = Dict({}, Key=config_key, Type=encryption_type)
        
    def load_config_from_dict(self, config_dict):
        """Load configuration from a dictionary and encrypt it."""
        print(f"\n[CONFIG] Loading configuration...")
        
        for key, value in config_dict.items():
            if isinstance(value, str):
                # Encrypt string values
                encrypted_value = String(value, Key=self.config_key, Type=self.encryption_type)
                self.config.add(key, str(encrypted_value))
                print(f"  [OK] Encrypted: {key}")
            elif isinstance(value, (int, float, bool)):
                # Convert and encrypt numeric/boolean values
                encrypted_value = String(str(value), Key=self.config_key, Type=self.encryption_type)
                self.config.add(key, str(encrypted_value))
                print(f"  [OK] Encrypted: {key}")
            elif isinstance(value, dict):
                # Recursively encrypt nested dictionaries
                nested_dict = Dict(value, Key=self.config_key, Type=self.encryption_type)
                self.config.add(key, nested_dict)
                print(f"  [OK] Encrypted nested dict: {key}")
        
        print(f"[OK] Configuration loaded and encrypted")
    
    def get_config_value(self, key):
        """Get and decrypt a configuration value."""
        try:
            encrypted_config = self.config.get(key)
            
            if encrypted_config:
                # Try to decrypt if it's a String object
                if isinstance(encrypted_config, str):
                    encrypted_str = String(encrypted_config, Key=self.config_key, Type=self.encryption_type)
                    decrypted = encrypted_str.topystr(self.config_key)
                    return decrypted
                return encrypted_config
            return None
        except Exception as e:
            print(f"[FAIL] Error getting config value: {e}")
            return None
    
    def update_config(self, key, value):
        """Update a configuration value."""
        print(f"\n[CONFIG] Updating: {key}")
        
        if isinstance(value, str):
            encrypted_value = String(value, Key=self.config_key, Type=self.encryption_type)
            self.config.add(key, str(encrypted_value))
            print(f"  [OK] Updated")
        else:
            encrypted_value = String(str(value), Key=self.config_key, Type=self.encryption_type)
            self.config.add(key, str(encrypted_value))
            print(f"  [OK] Updated")
    
    def export_config_to_file(self, filename="secure_config.json"):
        """Export encrypted configuration to a file."""
        print(f"\n[EXPORT] Exporting configuration to {filename}...")
        
        try:
            # Get all encrypted config
            config_data = {}
            for key in self.config.keys():
                config_data[key] = str(self.config.get(key))
            
            with open(filename, 'w') as f:
                json.dump(config_data, f, indent=2)
            
            print(f"[OK] Configuration exported to {filename}")
            return True
        except Exception as e:
            print(f"[FAIL] Export error: {e}")
            return False
    
    def list_all_config_keys(self):
        """List all configuration keys."""
        print(f"\n[CONFIG] Available configuration keys:")
        keys = list(self.config.keys())
        for i, key in enumerate(keys, 1):
            print(f"  {i}. {key}")


def main():
    """Main demonstration."""
    print("=" * 70)
    print("EXAMPLE 3: Secure Configuration Management")
    print("=" * 70)
    
    # Create config manager
    config_manager = SecureConfigManager(
        config_key="my_app_secret_key",
        encryption_type=3
    )
    
    # Load application configuration
    app_config = {
        "database_url": "postgresql://user:password@localhost/mydb",
        "api_key": "sk_live_1234567890abcdef",
        "secret_token": "super_secret_token_xyz",
        "max_connections": "100",
        "debug_mode": "False",
        "admin_email": "admin@example.com",
        "payment_gateway": {
            "merchant_id": "MERCHANT123",
            "api_secret": "gateway_secret_key"
        }
    }
    
    config_manager.load_config_from_dict(app_config)
    
    # Retrieve and decrypt configuration values
    print("\n" + "-" * 70)
    print("Retrieving Configuration Values:")
    print("-" * 70)
    
    db_url = config_manager.get_config_value("database_url")
    print(f"\nDatabase URL: {db_url[:30]}..." if db_url else "Not found")
    
    api_key = config_manager.get_config_value("api_key")
    print(f"API Key: {api_key[:20]}..." if api_key else "Not found")
    
    secret_token = config_manager.get_config_value("secret_token")
    print(f"Secret Token: {secret_token[:20]}..." if secret_token else "Not found")
    
    admin_email = config_manager.get_config_value("admin_email")
    print(f"Admin Email: {admin_email}")
    
    # Update configuration
    print("\n" + "-" * 70)
    print("Updating Configuration:")
    print("-" * 70)
    
    config_manager.update_config("api_key", "sk_live_new_key_updated")
    new_api_key = config_manager.get_config_value("api_key")
    # print(f"Updated API Key: {new_api_key[:20]}...")
    
    # List all keys
    config_manager.list_all_config_keys()
    
    # Export configuration
    config_manager.export_config_to_file("secure_config.json")
    
    print("\n" + "=" * 70)
    print("Demonstration completed!")
    print("=" * 70)
    print("\nNote: In production, store the encryption key securely")
    print("      (e.g., in environment variables, not in code)")


if __name__ == "__main__":
    main()

