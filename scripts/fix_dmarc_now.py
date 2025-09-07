#!/usr/bin/env python3
"""
Generate the exact DNS change needed to fix Gmail spam issue
"""

print("=== COPY THESE DNS CHANGES TO GODADDY ===\n")

print("1. GO TO: https://dcc.godaddy.com/control/loudfair.com/dns")
print("\n2. FIND THE DMARC RECORD:")
print("   Type: TXT")
print("   Name: _dmarc")
print("   Current Value: v=DMARC1; p=quarantine; rua=mailto:postmaster@loudfair.com; pct=100; sp=none")

print("\n3. CLICK EDIT AND CHANGE TO:")
print("   Name: _dmarc")
print("   Value: v=DMARC1; p=none; rua=mailto:postmaster@loudfair.com")
print("\n   (Remove quotes if GoDaddy adds them automatically)")

print("\n4. SAVE THE RECORD")

print("\n=== WHY THIS FIXES SPAM ===")
print("- p=quarantine tells receivers to treat your email suspiciously")
print("- p=none tells receivers to monitor but not take action")
print("- New domains should ALWAYS start with p=none")
print("- After building reputation (2-4 weeks), change back to p=quarantine")

print("\n=== TEST IMMEDIATELY AFTER ===")
print("1. Wait 5 minutes for DNS to update")
print("2. Send an email with REAL content (not 'test'):")
print("   Subject: 'Meeting follow-up from Ben'")
print("   Body: 'Hi, Thanks for our discussion today about the project...'")
print("3. It should go directly to inbox!")

print("\n=== OPTIONAL: Quick SPF Adjustment ===")
print("Your current SPF ends with '~all' (softfail)")
print("Change to: v=spf1 include:_spf.protonmail.ch -all")
print("(The -all is stricter and can improve reputation)")

input("\nPress Enter to see the DNS update command...")
