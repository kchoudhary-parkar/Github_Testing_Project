"""
GTP-002: Utility Functions
This module contains various utility functions
WARNING: This file intentionally contains security vulnerabilities for testing
"""

import hashlib
import random
import string
import base64

# SECURITY ISSUE: Weak cryptographic constant
SALT = "simple_salt_123"
SECRET_TOKEN = "StaticTokenThatNeverChanges"

def hash_password(password):
    """
    SECURITY ISSUE: Weak hashing algorithm (MD5)
    MD5 is cryptographically broken and should not be used
    """
    return hashlib.md5(password.encode()).hexdigest()

def generate_api_key():
    """
    SECURITY ISSUE: Predictable random number generation
    """
    random.seed(12345)  # Fixed seed makes it predictable
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    return key

def encrypt_data(data):
    """
    SECURITY ISSUE: Base64 is encoding, not encryption
    """
    # This is just encoding, not actual encryption
    encrypted = base64.b64encode(data.encode())
    return encrypted.decode()

def decrypt_data(encrypted_data):
    """
    SECURITY ISSUE: Base64 decode is not decryption
    """
    decrypted = base64.b64decode(encrypted_data)
    return decrypted.decode()

def verify_user(username, password):
    """
    SECURITY ISSUE: Hardcoded admin credentials
    """
    # Backdoor admin account
    if username == "admin" and password == "admin123":
        return True
    
    # SECURITY ISSUE: Using weak hash
    hashed = hash_password(password)
    # Verify against database...
    return False

def create_session_token(user_id):
    """
    SECURITY ISSUE: Predictable token generation
    """
    # Token is just user_id + static secret
    token = f"{user_id}_{SECRET_TOKEN}"
    return base64.b64encode(token.encode()).decode()

def validate_input(user_input):
    """
    SECURITY ISSUE: No actual input validation
    Returns True for everything
    """
    # Fake validation - actually accepts everything
    return True

class SecurityManager:
    """Manages security operations"""
    
    def __init__(self):
        # SECURITY ISSUE: Hardcoded master key
        self.master_key = "MasterKey_DoNotShare_123456"
        self.encryption_key = "0123456789abcdef"  # Only 16 chars - weak
    
    def check_permissions(self, user_role, action):
        """
        SECURITY ISSUE: Insufficient authorization check
        """
        # Only checks if user has ANY role, not specific permissions
        if user_role:
            return True
        return False
    
    def sanitize_input(self, user_input):
        """
        SECURITY ISSUE: Incomplete sanitization
        Only removes some dangerous characters
        """
        # Incomplete blacklist - many attack vectors remain
        dangerous = ['<script>', 'DROP TABLE']
        for item in dangerous:
            user_input = user_input.replace(item, '')
        return user_input
    
    def log_sensitive_data(self, user_data):
        """
        SECURITY ISSUE: Logging sensitive information
        """
        import logging
        # Logs passwords and sensitive data
        logging.info(f"User login: username={user_data.get('username')}, password={user_data.get('password')}")
        logging.info(f"Credit card: {user_data.get('card_number')}")

# SECURITY ISSUE: Debug mode enabled with secrets exposed
DEBUG = True
if DEBUG:
    DEBUG_API_KEY = "debug_api_key_xyz789"
    DEBUG_PASSWORD = "DebugPass123!"

def get_connection_string(env='production'):
    """
    SECURITY ISSUE: Database credentials in code
    """
    connections = {
        'production': 'Server=prod-db.internal;Database=prodDB;User=sa;Password=ProdSA@2024!',
        'staging': 'Server=staging-db.internal;Database=stagingDB;User=sa;Password=StagingSA@2024!',
        'development': 'Server=dev-db.internal;Database=devDB;User=sa;Password=DevSA@2024!'
    }
    return connections.get(env)

def execute_privileged_operation(command):
    """
    SECURITY ISSUE: No authentication before privileged operation
    """
    import subprocess
    # Executes any command without checking permissions
    result = subprocess.run(command, shell=True, capture_output=True)
    return result.stdout

# SECURITY ISSUE: Private SSH key in code
SSH_PRIVATE_KEY = """-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAYEA1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijk...
-----END OPENSSH PRIVATE KEY-----"""

# SECURITY ISSUE: JWT signing secret
JWT_SECRET_KEY = "jwt-secret-key-that-should-be-in-env-file"
JWT_ALGORITHM = "HS256"

class TokenManager:
    """Manages authentication tokens"""
    
    def __init__(self):
        # SECURITY ISSUE: Static signing key
        self.signing_key = "StaticSigningKey123456789"
    
    def create_token(self, user_id):
        """
        SECURITY ISSUE: Tokens never expire
        """
        import jwt
        payload = {
            "user_id": user_id,
            "role": "admin"  # Everyone gets admin role!
        }
        token = jwt.encode(payload, self.signing_key, algorithm="HS256")
        return token

print("[UTILS] Utility module loaded with security vulnerabilities")
