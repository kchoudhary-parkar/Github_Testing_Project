"""
GTP-002: Application Configuration
This module contains application settings and credentials
WARNING: This file intentionally contains security vulnerabilities for testing
"""

import os

# SECURITY ISSUE: Hardcoded credentials
DATABASE_URL = "postgresql://admin:SuperSecret123!@db.production.com:5432/maindb"
API_KEY = "sk-proj-abcd1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SECRET_KEY = "django-insecure-$#mwps8f@3!x%8k2z&9v*j4n6h7m5k3w2q1"

# SECURITY ISSUE: Exposed AWS credentials
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
AWS_REGION = "us-east-1"

# SECURITY ISSUE: Hardcoded OAuth tokens
GITHUB_TOKEN = "ghp_16C7e42F292c6912E7710c838347Ae178B4a"
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXX"

# SECURITY ISSUE: Private keys in code
STRIPE_SECRET_KEY = "sk_live_51AbCdEfGhIjKlMnOpQrStUvWxYz1234567890"
JWT_SECRET = "my_super_secret_jwt_key_do_not_share"

# SECURITY ISSUE: Database passwords
REDIS_PASSWORD = "redis_prod_password_123456"
MONGODB_CONNECTION = "mongodb://dbuser:dbpassword123@mongodb.example.com:27017/production"

# API Configuration
class Config:
    """Application configuration class"""
    
    # More hardcoded secrets
    OPENAI_API_KEY = "sk-ABcdEFghIJklMNopQRstUVwxYZ1234567890ABcdEFghIJk"
    AZURE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=mystorageaccount;AccountKey=abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ==;EndpointSuffix=core.windows.net"
    
    # Email credentials
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_USER = "admin@company.com"
    EMAIL_PASSWORD = "EmailPass123!"
    
    # Third-party API keys
    SENDGRID_API_KEY = "SG.1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.123456"
    TWILLIO_AUTH_TOKEN = "1234567890abcdef1234567890abcdef"
    
    def __init__(self):
        # SECURITY ISSUE: Password in constructor
        self.admin_password = "Admin123!@#"
        self.root_password = "root12345"

# SECURITY ISSUE: Crypto keys exposed
ENCRYPTION_KEY = b'ThisIsA32ByteEncryptionKeyForAES'
PRIVATE_KEY_PEM = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA1234567890ABCDEFGHIJKLMNOP...
-----END RSA PRIVATE KEY-----"""

# Production database credentials
PROD_DB_HOST = "prod-db-01.internal.company.com"
PROD_DB_USER = "prod_admin"
PROD_DB_PASS = "Pr0d@dm1nP@ss2024!"
PROD_DB_NAME = "production_database"

def get_connection_string():
    """Returns database connection string with embedded credentials"""
    # SECURITY ISSUE: Building connection string with hardcoded password
    return f"Server={PROD_DB_HOST};Database={PROD_DB_NAME};User Id={PROD_DB_USER};Password={PROD_DB_PASS};"

# SECURITY ISSUE: API tokens in dictionary
API_TOKENS = {
    "service_a": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0",
    "service_b": "Token abc123def456ghi789jkl012mno345pqr678",
    "service_c": "ApiKey-1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
}

print("[CONFIG] Loaded application configuration with all credentials")
