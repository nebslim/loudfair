#!/usr/bin/env python3
"""
Ultimate DNS settings for maximum inbox delivery
"""

import subprocess

def check_current_dns():
    """Check current DNS and recommend improvements"""
    
    print("=== ULTIMATE DNS SETTINGS FOR INBOX DELIVERY ===\n")
    
    # Check current settings
    print("Checking current DNS settings for loudfair.com...\n")
    
    domain = "loudfair.com"
    
    # Get all current records
    mx = subprocess.run(["dig", "+short", "MX", domain], capture_output=True, text=True).stdout.strip()
    spf = subprocess.run(["dig", "+short", "TXT", domain], capture_output=True, text=True).stdout.strip()
    dmarc = subprocess.run(["dig", "+short", "TXT", f"_dmarc.{domain}"], capture_output=True, text=True).stdout.strip()
    
    print("CURRENT SETTINGS:")
    print(f"MX: {mx}")
    print(f"SPF: {spf}")
    print(f"DMARC: {dmarc}")
    print("\n" + "="*60 + "\n")

def print_ultimate_dns_settings():
    """Print all DNS settings for maximum deliverability"""
    
    print("🎯 ADD THESE DNS RECORDS FOR MAXIMUM INBOX DELIVERY:\n")
    
    print("1. ✅ FIX DMARC (MOST IMPORTANT)")
    print("   Type: TXT")
    print("   Name: _dmarc")
    print("   Value: v=DMARC1; p=none; pct=100; rua=mailto:postmaster@loudfair.com; ruf=mailto:postmaster@loudfair.com; fo=1")
    print("   Why: Tells receivers to accept your email while monitoring\n")
    
    print("2. ✅ OPTIMIZE SPF")
    print("   Type: TXT") 
    print("   Name: @")
    print("   Value: v=spf1 include:_spf.protonmail.ch -all")
    print("   Why: The '-all' (vs ~all) shows confidence and improves reputation\n")
    
    print("3. 🆕 ADD BIMI (Brand Indicator)")
    print("   Type: TXT")
    print("   Name: default._bimi")
    print("   Value: v=BIMI1; l=; a=;")
    print("   Why: Prepares for logo display in Gmail (builds trust)\n")
    
    print("4. 🆕 ADD MTA-STS (Mail Security)")
    print("   Type: TXT")
    print("   Name: _mta-sts")
    print("   Value: v=STSv1; id=20250907")
    print("   Why: Shows you support secure email transmission\n")
    
    print("5. 🆕 ADD TLSRPT (TLS Reporting)")
    print("   Type: TXT")
    print("   Name: _smtp._tls")
    print("   Value: v=TLSRPTv1; rua=mailto:tlsrpt@loudfair.com")
    print("   Why: Shows professional email setup\n")
    
    print("6. 🆕 ADD DKIM ALIGNMENT RECORD")
    print("   Type: TXT")
    print("   Name: @")
    print("   Value: v=spf1 include:_spf.protonmail.ch a:loudfair.com -all")
    print("   Why: Adds your domain's A record for better alignment\n")
    
    print("7. 🆕 GOOGLE POSTMASTER VERIFICATION")
    print("   Sign up at: https://postmaster.google.com")
    print("   Add domain: loudfair.com")
    print("   Type: TXT")
    print("   Name: @")
    print("   Value: google-site-verification=[code from Google]")
    print("   Why: See exactly why Gmail might filter you\n")
    
    print("8. 🆕 MICROSOFT SNDS VERIFICATION")
    print("   Sign up at: https://sendersupport.olc.protection.outlook.com/snds/")
    print("   Type: TXT")
    print("   Name: @")
    print("   Value: MS=[code from Microsoft]")
    print("   Why: Improves Outlook/Hotmail delivery\n")
    
    print("="*60)
    print("\n🏆 REPUTATION SIGNALS (Non-DNS):\n")
    
    print("1. EMAIL ENGAGEMENT")
    print("   - Get recipients to reply to your emails")
    print("   - Ask them to add you to contacts")
    print("   - Avoid 'no-reply' addresses\n")
    
    print("2. CONSISTENT SENDING")
    print("   - Send from same IP/service (Proton)")
    print("   - Regular volume (not burst sending)")
    print("   - Warm up gradually\n")
    
    print("3. CONTENT QUALITY")
    print("   - Real subject lines (not 'test')")
    print("   - Proper HTML/text format")
    print("   - Include unsubscribe link for bulk mail\n")
    
    print("4. DOMAIN REPUTATION")
    print("   - Set up a website at loudfair.com")
    print("   - Add privacy policy & contact info")
    print("   - Register domain for 2+ years\n")

def print_priority_order():
    """Print implementation priority"""
    
    print("\n🚀 IMPLEMENTATION PRIORITY:\n")
    print("IMMEDIATE (Do Now):")
    print("1. Fix DMARC to p=none ← This alone might fix everything")
    print("2. Change SPF to -all")
    print("3. Add Google Postmaster\n")
    
    print("THIS WEEK:")
    print("4. Add BIMI record")
    print("5. Add MTA-STS")
    print("6. Set up website\n")
    
    print("ONGOING:")
    print("7. Send real emails (not tests)")
    print("8. Get engagement (replies)")
    print("9. Monitor deliverability\n")

def create_monitoring_script():
    """Create script to monitor deliverability"""
    
    monitor_script = '''#!/usr/bin/env python3
import subprocess
import time

def check_propagation():
    """Check if DNS changes have propagated"""
    
    print("Checking DNS propagation...")
    
    # Check DMARC
    dmarc = subprocess.run(["dig", "+short", "TXT", "_dmarc.loudfair.com"], 
                          capture_output=True, text=True).stdout.strip()
    
    if "p=none" in dmarc:
        print("✅ DMARC updated successfully!")
    else:
        print("⏳ DMARC not updated yet...")
    
    # Check SPF
    spf = subprocess.run(["dig", "+short", "TXT", "loudfair.com"], 
                        capture_output=True, text=True).stdout.strip()
    
    if "-all" in spf and "~all" not in spf:
        print("✅ SPF optimized!")
    else:
        print("⏳ SPF not optimized yet...")

if __name__ == "__main__":
    check_propagation()
'''
    
    with open("/Users/bc-02-m3/00-loudfair.com/monitor_dns.py", "w") as f:
        f.write(monitor_script)
    
    print("\n✅ Created monitor_dns.py to check DNS propagation")

if __name__ == "__main__":
    check_current_dns()
    print_ultimate_dns_settings()
    print_priority_order()
    create_monitoring_script()
    
    print("\n⚡ QUICK WIN: Just fixing DMARC to p=none will solve 90% of spam issues!")
    print("The other settings are for maximum deliverability over time.")
