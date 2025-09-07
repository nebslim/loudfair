#!/usr/bin/env python3
"""
Monitor DNS propagation for spam fix
"""

import subprocess
import time
import sys

def check_dns():
    """Check if DNS changes have propagated"""
    
    print("Checking DNS propagation for loudfair.com...")
    print("=" * 50)
    
    # Check DMARC
    print("\n1. DMARC Record:")
    dmarc = subprocess.run(["dig", "+short", "TXT", "_dmarc.loudfair.com"], 
                          capture_output=True, text=True).stdout.strip()
    print(f"   Current: {dmarc}")
    
    if "p=none" in dmarc:
        print("   ✅ DMARC fixed! (p=none)")
    elif "p=quarantine" in dmarc:
        print("   ❌ DMARC still set to quarantine (SPAM ISSUE)")
    else:
        print("   ⚠️  No DMARC record found")
    
    # Check SPF
    print("\n2. SPF Record:")
    txt_records = subprocess.run(["dig", "+short", "TXT", "loudfair.com"], 
                                capture_output=True, text=True).stdout.strip()
    
    spf = None
    for line in txt_records.split('\n'):
        if 'spf1' in line:
            spf = line
            print(f"   Current: {spf}")
            break
    
    if spf:
        if "-all" in spf and "~all" not in spf:
            print("   ✅ SPF optimized! (-all)")
        elif "~all" in spf:
            print("   ⚠️  SPF still using ~all (should be -all)")
    else:
        print("   ⚠️  No SPF record found")
    
    # Check from multiple DNS servers
    print("\n3. Checking propagation from different locations:")
    dns_servers = {
        "Google": "8.8.8.8",
        "Cloudflare": "1.1.1.1",
        "OpenDNS": "208.67.222.222"
    }
    
    for name, server in dns_servers.items():
        dmarc_check = subprocess.run(["dig", f"@{server}", "+short", "TXT", "_dmarc.loudfair.com"], 
                                   capture_output=True, text=True).stdout.strip()
        if "p=none" in dmarc_check:
            print(f"   ✅ {name} DNS: Updated")
        else:
            print(f"   ❌ {name} DNS: Not updated yet")
    
    # Summary
    print("\n" + "=" * 50)
    if "p=none" in dmarc:
        print("✅ SPAM FIX APPLIED! Your emails should now go to inbox.")
        print("   Test with a real email (not 'test') in 5-10 minutes.")
    else:
        print("❌ DNS changes not propagated yet.")
        print("   Make sure you saved the changes in GoDaddy.")
        print("   DNS updates can take 5-30 minutes.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--watch":
        # Watch mode - check every 2 minutes
        while True:
            check_dns()
            print("\nChecking again in 2 minutes... (Ctrl+C to stop)")
            time.sleep(120)
    else:
        check_dns()
        print("\nRun with --watch to monitor continuously:")
