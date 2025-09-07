#!/usr/bin/env python3
"""
GoDaddy DNS Setup for Proton Mail
"""

import requests
import json
import time

# GoDaddy API credentials
API_KEY = "eogjnQkV8bZr_SCC7Dn7S5VnZUU6URuVKLy"
API_SECRET = "W2Bi6TmrsTFhaZeYBK3TaY"
DOMAIN = "loudfair.com"

# GoDaddy API endpoint
BASE_URL = "https://api.godaddy.com"  # Production endpoint
HEADERS = {
    "Authorization": f"sso-key {API_KEY}:{API_SECRET}",
    "Content-Type": "application/json"
}

def test_api_credentials():
    """Test if API credentials are valid"""
    url = f"{BASE_URL}/v1/domains/available"
    params = {"domain": "test12345.com"}
    print(f"Testing API credentials...")
    response = requests.get(url, headers=HEADERS, params=params)
    
    if response.status_code == 200:
        print("✓ API credentials are valid!")
        return True
    else:
        print(f"✗ API credential test failed: {response.status_code}")
        print(response.text)
        return False

def get_dns_records():
    """Get current DNS records"""
    url = f"{BASE_URL}/v1/domains/{DOMAIN}/records"
    print(f"Requesting: {url}")
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error getting records: {response.status_code}")
        print(response.text)
        # Try to check if it's a test/production issue
        if response.status_code == 403:
            print("\nPossible issues:")
            print("1. API key might not have domain management permissions")
            print("2. Domain might not be in your GoDaddy account")
            print("3. API credentials might need to be regenerated")
        return None

def add_dns_record(record_type, name, data, ttl=3600, priority=None):
    """Add a DNS record"""
    url = f"{BASE_URL}/v1/domains/{DOMAIN}/records"
    
    # Get existing records
    existing_records = get_dns_records()
    if existing_records is None:
        return False
    
    # Create new record
    new_record = {
        "type": record_type,
        "name": name,
        "data": data,
        "ttl": ttl
    }
    
    if priority and record_type == "MX":
        new_record["priority"] = priority
    
    # Check if record already exists
    exists = False
    for record in existing_records:
        if (record.get("type") == record_type and 
            record.get("name") == name and 
            record.get("data") == data):
            print(f"Record already exists: {record_type} {name} -> {data}")
            exists = True
            break
    
    if not exists:
        # Add the new record to existing records
        existing_records.append(new_record)
        
        # Update all records
        response = requests.put(url, headers=HEADERS, json=existing_records)
        
        if response.status_code in [200, 204]:
            print(f"✓ Added {record_type} record: {name} -> {data}")
            return True
        else:
            print(f"✗ Error adding record: {response.status_code}")
            print(response.text)
            return False
    
    return True

def add_proton_verification():
    """Add Proton Mail verification TXT record"""
    print("\n=== Adding Proton Mail Verification Record ===")
    return add_dns_record(
        "TXT", 
        "@", 
        "protonmail-verification=6d50e400e1ecc8b9c648c50477e351385a242bb1",
        ttl=3600
    )

def add_proton_mail_records():
    """Add all Proton Mail DNS records (MX, SPF, etc.)"""
    print("\n=== Adding Proton Mail Email Records ===")
    
    success = True
    
    # Add MX records
    print("\nAdding MX records...")
    success &= add_dns_record("MX", "@", "mail.protonmail.ch", ttl=3600, priority=10)
    success &= add_dns_record("MX", "@", "mailsec.protonmail.ch", ttl=3600, priority=20)
    
    # Add OPTIMIZED SPF record (with -all instead of ~all)
    print("\nAdding optimized SPF record...")
    success &= add_dns_record("TXT", "@", "v=spf1 include:_spf.protonmail.ch -all", ttl=3600)
    
    return success

def update_dmarc_for_deliverability():
    """Update DMARC to p=none for new domain deliverability"""
    print("\n=== Updating DMARC for Inbox Delivery ===")
    
    # Get existing records
    records = get_dns_records()
    if not records:
        return False
    
    # Find and update DMARC record
    updated = False
    for i, record in enumerate(records):
        if record.get("type") == "TXT" and record.get("name") == "_dmarc":
            print(f"Found existing DMARC: {record['data']}")
            # Update to p=none for deliverability
            records[i]["data"] = "v=DMARC1; p=none; pct=100; rua=mailto:postmaster@loudfair.com; fo=1"
            updated = True
            break
    
    if updated:
        # Update all records
        url = f"{BASE_URL}/v1/domains/{DOMAIN}/records"
        response = requests.put(url, headers=HEADERS, json=records)
        
        if response.status_code in [200, 204]:
            print("✓ DMARC updated to p=none for better deliverability")
            return True
        else:
            print(f"✗ Error updating DMARC: {response.status_code}")
            return False
    else:
        # Add new DMARC if doesn't exist
        return add_dns_record("TXT", "_dmarc", 
                            "v=DMARC1; p=none; pct=100; rua=mailto:postmaster@loudfair.com; fo=1", 
                            ttl=3600)

def add_inbox_optimization_records():
    """Add additional DNS records for maximum inbox delivery"""
    print("\n=== Adding Inbox Optimization Records ===")
    
    success = True
    
    # Add BIMI record (Brand Indicators)
    print("\nAdding BIMI record...")
    success &= add_dns_record("TXT", "default._bimi", "v=BIMI1; l=; a=;", ttl=3600)
    
    # Add MTA-STS record
    print("\nAdding MTA-STS record...")
    success &= add_dns_record("TXT", "_mta-sts", "v=STSv1; id=20250907", ttl=3600)
    
    # Add TLSRPT record
    print("\nAdding TLSRPT record...")
    success &= add_dns_record("TXT", "_smtp._tls", "v=TLSRPTv1; rua=mailto:tlsrpt@loudfair.com", ttl=3600)
    
    print("\nNote: Don't forget to:")
    print("- Sign up for Google Postmaster Tools: https://postmaster.google.com")
    print("- Sign up for Microsoft SNDS: https://sendersupport.olc.protection.outlook.com/snds/")
    
    return success

def display_current_records():
    """Display current DNS records"""
    print("\n=== Current DNS Records ===")
    records = get_dns_records()
    
    if records:
        for record in records:
            record_str = f"{record['type']:<6} {record['name']:<20} {record['data']}"
            if record.get('priority'):
                record_str += f" (Priority: {record['priority']})"
            print(record_str)
    
    return records

if __name__ == "__main__":
    print(f"GoDaddy DNS Setup for {DOMAIN}")
    print("=" * 50)
    
    import sys
    
    # Test API credentials first
    if not test_api_credentials():
        print("\n✗ API credentials are not working. Please check:")
        print("1. Make sure the API key and secret are correct")
        print("2. Ensure the API key is for production (not OTE/test)")
        print("3. Check if the API key has been activated")
        print("4. Make sure you have 10+ domains in your GoDaddy account")
        exit(1)
    
    # Display current records
    display_current_records()
    
    if "--optimize" in sys.argv:
        # Full optimization mode - add all records for inbox delivery
        print("\n🚀 FULL INBOX OPTIMIZATION MODE")
        
        # 1. Fix DMARC for deliverability
        update_dmarc_for_deliverability()
        
        # 2. Add optimized email records
        add_proton_mail_records()
        
        # 3. Add inbox optimization records
        add_inbox_optimization_records()
        
        print("\n✓ All optimization records added!")
        print("\nIMPORTANT:")
        print("1. Add DKIM records from Proton Mail (they provide after verification)")
        print("2. Sign up for Google Postmaster Tools")
        print("3. Wait 15-30 minutes for DNS propagation")
        print("4. Test with REAL email content (not 'test')")
        
    elif "--email" in sys.argv:
        # Just add email records
        add_proton_mail_records()
        update_dmarc_for_deliverability()
        print("\n✓ Email records added with deliverability optimization!")
        print("\nNote: You'll still need to add DKIM records from Proton Mail after verification")
        
    else:
        # Default: just add verification record
        if add_proton_verification():
            print("\n✓ Verification record added successfully!")
            print("\nNext steps:")
            print("1. Wait 5-10 minutes for DNS propagation")
            print("2. Go back to Proton Mail and click 'Verify'")
            print("3. Once verified, run with --optimize flag for full inbox delivery setup:")
            print(f"   python {sys.argv[0]} --optimize")
        else:
            print("\n✗ Failed to add verification record")
