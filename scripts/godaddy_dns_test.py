#!/usr/bin/env python3
"""
Test GoDaddy API credentials with different approaches
"""

import requests
import json

# GoDaddy API credentials
API_KEY = "eogjnQkV8bZr_R4T4V7zpCbdSG9Tpro7AXs"
API_SECRET = "SCVmm8QT4qfNhcan1QpDjf"
DOMAIN = "loudfair.com"

# Test different endpoints and auth formats
def test_auth_formats():
    """Test different authorization header formats"""
    
    endpoints = [
        ("Production", "https://api.godaddy.com"),
        ("OTE/Test", "https://api.ote-godaddy.com")
    ]
    
    auth_formats = [
        ("sso-key", f"sso-key {API_KEY}:{API_SECRET}"),
        ("Bearer", f"Bearer {API_KEY}:{API_SECRET}"),
        ("Basic", f"{API_KEY}:{API_SECRET}")
    ]
    
    for env_name, base_url in endpoints:
        print(f"\n=== Testing {env_name} Environment ===")
        
        for auth_name, auth_value in auth_formats:
            print(f"\nTrying {auth_name} format...")
            
            headers = {
                "Authorization": auth_value,
                "Content-Type": "application/json"
            }
            
            # Try domain availability check (simpler endpoint)
            try:
                url = f"{base_url}/v1/domains/available?domain=test.com"
                response = requests.get(url, headers=headers, timeout=5)
                print(f"  Availability check: {response.status_code}")
                if response.status_code != 200:
                    print(f"  Response: {response.text[:200]}")
            except Exception as e:
                print(f"  Failed: {str(e)}")
            
            # Try getting domain records
            try:
                url = f"{base_url}/v1/domains/{DOMAIN}/records"
                response = requests.get(url, headers=headers, timeout=5)
                print(f"  Domain records: {response.status_code}")
                if response.status_code == 200:
                    print(f"  ✓ SUCCESS! This format works!")
                    records = response.json()
                    print(f"  Found {len(records)} DNS records")
                    return True, base_url, headers
                elif response.status_code != 200:
                    print(f"  Response: {response.text[:200]}")
            except Exception as e:
                print(f"  Failed: {str(e)}")
    
    return False, None, None

if __name__ == "__main__":
    print("Testing GoDaddy API Credentials")
    print("=" * 50)
    
    success, working_url, working_headers = test_auth_formats()
    
    if success:
        print(f"\n✓ Found working configuration!")
        print(f"  URL: {working_url}")
        print(f"  Headers: {working_headers}")
    else:
        print("\n✗ Could not find a working configuration")
        print("\nTroubleshooting steps:")
        print("1. Verify your API key and secret are correct")
        print("2. Check if the API key is activated in your GoDaddy account")
        print("3. Ensure the API key has the right permissions")
        print("4. Try regenerating the API key in GoDaddy developer portal")
