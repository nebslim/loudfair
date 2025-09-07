#!/usr/bin/env python3
"""
Security-conscious alternative to p=none
"""

print("=== SECURE ALTERNATIVE: Use pct Parameter ===\n")

print("Instead of changing to p=none, you can keep p=quarantine but reduce percentage:\n")

print("CURRENT:")
print("v=DMARC1; p=quarantine; rua=mailto:postmaster@loudfair.com; pct=100; sp=none")

print("\nCHANGE TO:")
print("v=DMARC1; p=quarantine; rua=mailto:postmaster@loudfair.com; pct=10; sp=none")

print("\nThis means:")
print("- 90% of your emails bypass DMARC quarantine")
print("- 10% still get quarantined (for testing)")
print("- More secure than p=none")
print("- Should reduce spam classification significantly")

print("\n=== EVEN BETTER: Subdomain Policy ===")
print("\nAdd this to separate your sending domain:")
print("1. Create subdomain: mail.loudfair.com")
print("2. Set main domain: p=reject (maximum security)")
print("3. Set subdomain: sp=none (for sending)")

print("\n=== IMMEDIATE WORKAROUND ===")
print("While keeping current DMARC, do these:")
print("1. Add sender to Gmail contacts")
print("2. Create Gmail filter: from:loudfair.com → Never send to spam")
print("3. Send 5-10 legitimate emails and mark 'Not Spam'")
print("4. Gmail will learn your domain is legitimate")

print("\n=== Check Real Threats ===")
print("See if anyone is actually spoofing you:")
print("1. Check your DMARC reports at: postmaster@loudfair.com")
print("2. Or use: https://dmarcian.com/dmarc-inspector/")
print("3. If no spoofing detected → safe to use p=none temporarily")
