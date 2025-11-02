"""
Example 4: Secure Message Queue
===============================
This example demonstrates encrypting messages in a queue system.
Useful for secure messaging, logging, or inter-process communication.
"""

from EnigmaShield.CryptoTypes import array, String, Keys
from datetime import datetime
import uuid

class SecureMessageQueue:
    """A secure message queue that encrypts all messages."""
    
    def __init__(self, queue_name="default", encryption_key=None, encryption_type=3):
        """
        Initialize secure message queue.
        
        Args:
            queue_name: Name of the queue
            encryption_key: Encryption key (default: auto-generated)
            encryption_type: Encryption type (1-4)
        """
        self.queue_name = queue_name
        self.encryption_type = encryption_type
        
        if encryption_key:
            self.encryption_key = encryption_key
        else:
            # Generate a default key
            self.encryption_key = f"queue_{queue_name}_key_{uuid.uuid4().hex[:16]}"
        
        self.messages = array([], Key=self.encryption_key, Type=encryption_type)
        self.message_metadata = []
        
        print(f"[QUEUE] Initialized '{queue_name}' queue")
        print(f"  Encryption Type: {encryption_type}")
        print(f"  Key: {self.encryption_key[:30]}...")
    
    def enqueue(self, message, priority="normal", sender="anonymous"):
        """
        Add an encrypted message to the queue.
        
        Args:
            message: Message content to encrypt
            priority: Message priority (low, normal, high)
            sender: Sender identifier
        """
        print(f"\n[ENQUEUE] Adding message to queue '{self.queue_name}'...")
        
        # Create message object
        message_obj = {
            "id": str(uuid.uuid4()),
            "timestamp": datetime.now().isoformat(),
            "message": message,
            "priority": priority,
            "sender": sender
        }
        
        # Encrypt the entire message
        encrypted_message = String(str(message_obj), Key=self.encryption_key, Type=self.encryption_type)
        
        # Add to queue
        self.messages.add(str(encrypted_message))
        self.message_metadata.append({
            "id": message_obj["id"],
            "priority": priority,
            "sender": sender,
            "timestamp": message_obj["timestamp"]
        })
        
        print(f"  [OK] Message encrypted and queued")
        print(f"    ID: {message_obj['id'][:8]}...")
        print(f"    Priority: {priority}")
        print(f"    Sender: {sender}")
        print(f"    Queue size: {self.messages.len()}")
    
    def dequeue(self):
        """Remove and decrypt the next message from the queue."""
        print(f"\n[DEQUEUE] Retrieving message from queue '{self.queue_name}'...")
        
        if self.messages.len() == 0:
            print(f"  [FAIL] Queue is empty")
            return None
        
        try:
            # Get encrypted message
            encrypted_message = self.messages[0]
            
            # Decrypt message
            encrypted_str = String(encrypted_message, Key=self.encryption_key, Type=self.encryption_type)
            decrypted_message_str = encrypted_str.topystr(self.encryption_key)
            
            # Parse message (in real scenario, use proper JSON parsing)
            # For demonstration, we'll return the decrypted string
            self.messages.pop(0)
            
            if self.message_metadata:
                metadata = self.message_metadata.pop(0)
            
            print(f"  [OK] Message decrypted and retrieved")
            print(f"    Content: {decrypted_message_str[:50]}...")
            
            return decrypted_message_str
        except Exception as e:
            print(f"  [FAIL] Error: {e}")
            return None
    
    def peek(self):
        """Peek at the next message without removing it."""
        print(f"\n[PEEK] Viewing next message in queue '{self.queue_name}'...")
        
        if self.messages.len() == 0:
            print(f"  [FAIL] Queue is empty")
            return None
        
        try:
            encrypted_message = self.messages[0]
            encrypted_str = String(encrypted_message, Key=self.encryption_key, Type=self.encryption_type)
            decrypted = encrypted_str.topystr(self.encryption_key)
            
            print(f"  [OK] Next message: {decrypted[:50]}...")
            return decrypted
        except Exception as e:
            print(f"  [FAIL] Error: {e}")
            return None
    
    def get_queue_size(self):
        """Get the number of messages in the queue."""
        return self.messages.len()
    
    def clear_queue(self):
        """Clear all messages from the queue."""
        print(f"\n[CLEAR] Clearing queue '{self.queue_name}'...")
        self.messages.clear()
        self.message_metadata.clear()
        print(f"  [OK] Queue cleared")


class SecureLogger:
    """A secure logger that encrypts log messages."""
    
    def __init__(self, log_key="logger_secret_key", encryption_type=3):
        self.log_key = log_key
        self.encryption_type = encryption_type
        self.logs = array([], Key=log_key, Type=encryption_type)
    
    def log(self, level, message):
        """Log an encrypted message."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}"
        
        encrypted_log = String(log_entry, Key=self.log_key, Type=self.encryption_type)
        self.logs.add(str(encrypted_log))
        
        print(f"[LOG] {log_entry}")
    
    def get_logs(self, count=10):
        """Retrieve and decrypt recent logs."""
        print(f"\n[LOGS] Retrieving last {count} log entries...")
        
        try:
            decrypted_logs = self.logs.to_pyarray(self.log_key)
            recent_logs = decrypted_logs[-count:] if len(decrypted_logs) > count else decrypted_logs
            
            print(f"  Found {len(recent_logs)} log entries:")
            for i, log in enumerate(recent_logs, 1):
                if isinstance(log, str):
                    encrypted_str = String(log, Key=self.log_key, Type=self.encryption_type)
                    decrypted = encrypted_str.topystr(self.log_key)
                    print(f"    {i}. {decrypted}")
            
            return recent_logs
        except Exception as e:
            print(f"  [FAIL] Error: {e}")
            return []


def main():
    """Main demonstration."""
    print("=" * 70)
    print("EXAMPLE 4: Secure Message Queue")
    print("=" * 70)
    
    # Create secure message queue
    queue = SecureMessageQueue(
        queue_name="user_notifications",
        encryption_key="notification_queue_key_2024",
        encryption_type=3
    )
    
    # Enqueue messages
    print("\n" + "-" * 70)
    print("Enqueueing Messages:")
    print("-" * 70)
    
    queue.enqueue("Welcome to our service!", priority="high", sender="system")
    queue.enqueue("Your order has been processed", priority="normal", sender="order_service")
    queue.enqueue("Payment received: $99.99", priority="high", sender="payment_service")
    queue.enqueue("Reminder: Update your profile", priority="low", sender="system")
    queue.enqueue("Security alert: New login detected", priority="high", sender="security")
    
    # Check queue size
    print(f"\n[QUEUE] Current queue size: {queue.get_queue_size()}")
    
    # Peek at next message
    queue.peek()
    
    # Dequeue messages
    print("\n" + "-" * 70)
    print("Dequeueing Messages:")
    print("-" * 70)
    
    for i in range(3):
        queue.dequeue()
    
    print(f"\n[QUEUE] Remaining queue size: {queue.get_queue_size()}")
    
    # Secure Logger Example
    print("\n" + "=" * 70)
    print("Secure Logger Example")
    print("=" * 70)
    
    logger = SecureLogger(log_key="app_logger_key", encryption_type=3)
    
    logger.log("INFO", "Application started")
    logger.log("WARNING", "High memory usage detected: 85%")
    logger.log("ERROR", "Database connection failed")
    logger.log("INFO", "User login successful: user123")
    logger.log("SECURITY", "Suspicious activity detected from IP: 192.168.1.100")
    
    logger.get_logs(5)
    
    print("\n" + "=" * 70)
    print("Demonstration completed!")
    print("=" * 70)


if __name__ == "__main__":
    main()

