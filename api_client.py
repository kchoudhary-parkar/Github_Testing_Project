"""
GTP-002: API Client Module
This module handles external API communications
WARNING: This file intentionally contains exposed credentials and insecure practices
"""

import requests
import json
import hashlib

class APIClient:
    """Client for external API communications"""
    
    def __init__(self):
        # SECURITY ISSUE: Hardcoded API credentials
        self.api_key = "pk_live_51HyperSecretAPIKey123456789"
        self.api_secret = "sk_live_SecretKeyForProduction987654321"
        self.base_url = "https://api.production.com"
        
        # SECURITY ISSUE: OAuth credentials in code
        self.oauth_client_id = "client_id_1234567890"
        self.oauth_client_secret = "client_secret_abcdefghijklmnop"
        self.oauth_token = "oauth2_token_ABCDEFGHIJKLMNOPQRSTUVWXYZ123456"
        
    def make_authenticated_request(self, endpoint, data):
        """
        SECURITY ISSUE: API key in URL parameters
        """
        url = f"{self.base_url}/{endpoint}?api_key={self.api_key}"
        headers = {
            "Authorization": f"Bearer {self.api_secret}",
            "X-API-Key": self.api_key
        }
        # SECURITY ISSUE: No SSL verification
        response = requests.post(url, json=data, headers=headers, verify=False)
        return response.json()
    
    def upload_file_to_s3(self, file_path, bucket_name):
        """
        SECURITY ISSUE: AWS credentials hardcoded
        """
        aws_access_key = "AKIAIOSFODNN7EXAMPLE"
        aws_secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
        
        # Insecure S3 client initialization
        import boto3
        s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key
        )
        s3_client.upload_file(file_path, bucket_name, file_path)
    
    def send_webhook(self, event_data):
        """
        SECURITY ISSUE: Webhook URL with embedded token
        """
        webhook_url = "https://webhooks.company.com/api/v1/events?token=webhook_secret_token_xyz789"
        headers = {"X-Webhook-Secret": "webhook_signing_key_123456"}
        response = requests.post(webhook_url, json=event_data, headers=headers)
        return response.status_code
    
    def fetch_user_data(self, user_id):
        """
        SECURITY ISSUE: Credentials in request
        """
        headers = {
            "X-Master-Key": "master_key_abcdef123456",
            "X-Admin-Token": "admin_token_ghijkl789012"
        }
        url = f"{self.base_url}/users/{user_id}"
        response = requests.get(url, headers=headers)
        return response.json()

# SECURITY ISSUE: Global API credentials
PAYMENT_GATEWAY_KEY = "pg_live_1234567890abcdefghijklmnop"
PAYMENT_GATEWAY_SECRET = "pgs_secret_zyxwvutsrqponmlkjihgfedcba"
MERCHANT_ID = "merchant_prod_98765"

class PaymentProcessor:
    """Handles payment processing"""
    
    def __init__(self):
        # SECURITY ISSUE: Credit card test data in code
        self.test_card = "4532-1488-0343-6467"
        self.test_cvv = "123"
        self.test_exp = "12/25"
    
    def process_payment(self, amount, card_number, cvv):
        """
        SECURITY ISSUE: Payment credentials hardcoded
        """
        api_url = "https://payments.gateway.com/charge"
        payload = {
            "merchant_id": MERCHANT_ID,
            "api_key": PAYMENT_GATEWAY_KEY,
            "secret": PAYMENT_GATEWAY_SECRET,
            "amount": amount,
            "card": card_number,
            "cvv": cvv
        }
        # SECURITY ISSUE: No SSL verification
        response = requests.post(api_url, json=payload, verify=False)
        return response.json()
    
    def refund_transaction(self, transaction_id):
        """
        SECURITY ISSUE: Admin password in function
        """
        admin_user = "payment_admin"
        admin_pass = "PaymentAdminPass2024!"
        
        auth = (admin_user, admin_pass)
        url = f"https://payments.gateway.com/refund/{transaction_id}"
        response = requests.post(url, auth=auth)
        return response.json()

# SECURITY ISSUE: Third-party service credentials
TWILIO_ACCOUNT_SID = "AC1234567890abcdef1234567890abcdef"
TWILIO_AUTH_TOKEN = "1234567890abcdef1234567890abcdef"
SENDGRID_API_KEY = "SG.1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklm.123456"

def send_sms(phone_number, message):
    """
    SECURITY ISSUE: Twilio credentials hardcoded
    """
    from twilio.rest import Client
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=message,
        from_='+1234567890',
        to=phone_number
    )
    return message.sid

def send_email(to_email, subject, body):
    """
    SECURITY ISSUE: SendGrid API key exposed
    """
    import sendgrid
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    # Email sending logic...
    pass

# SECURITY ISSUE: Firebase credentials in code
FIREBASE_CONFIG = {
    "apiKey": "AIzaSyABCDEFGHIJKLMNOPQRSTUVWXYZ123456",
    "authDomain": "myapp.firebaseapp.com",
    "databaseURL": "https://myapp.firebaseio.com",
    "projectId": "myapp-prod",
    "storageBucket": "myapp.appspot.com",
    "messagingSenderId": "1234567890",
    "appId": "1:1234567890:web:abcdef123456",
    "privateKey": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC...\n-----END PRIVATE KEY-----\n"
}

print("[API_CLIENT] API client module loaded with exposed credentials")
