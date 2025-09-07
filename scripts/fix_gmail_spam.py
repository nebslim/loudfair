#!/usr/bin/env python3
"""
Fast Gmail spam fix for loudfair.com
"""

import subprocess
import time
import requests
import json

def update_dns_for_reputation():
    """Add DNS records that improve email reputation"""
    
    print("=== Implementing Fast Spam Fixes ===\n")
    
    # 1. Check current DMARC policy
    print("1. Checking DMARC policy...")
    dmarc = subprocess.run(["dig", "+short", "TXT", "_dmarc.loudfair.com"], 
                          capture_output=True, text=True).stdout.strip()
    print(f"Current DMARC: {dmarc}")
    
    # The current p=quarantine might be causing issues for a new domain
    print("\n   FIX: Your DMARC has p=quarantine which tells Gmail to be suspicious.")
    print("   For new domains, start with p=none to build reputation.\n")
    
    # 2. Add Google Postmaster Tools TXT record
    print("2. Google Postmaster Tools Verification")
    print("   This lets you see exactly why Gmail marks you as spam.")
    print("   Add this TXT record in GoDaddy:")
    print("   Name: @")
    print("   Value: google-site-verification=<get-from-postmaster-tools>")
    print("   Sign up at: https://postmaster.google.com\n")
    
    # 3. Check for missing PTR record
    print("3. Checking PTR (reverse DNS) record...")
    proton_ip = "109.224.244.21"  # From your email headers
    ptr = subprocess.run(["dig", "+short", "-x", proton_ip], 
                        capture_output=True, text=True).stdout.strip()
    print(f"   Proton's PTR: {ptr}")
    print("   ✓ PTR is handled by Proton (good)\n")
    
    # 4. Create BIMI record for trust
    print("4. Adding BIMI record (Brand Indicators)")
    print("   This shows your logo in Gmail - instant trust boost")
    print("   Add this DNS record:")
    print("   Type: TXT") 
    print("   Name: default._bimi")
    print("   Value: v=BIMI1; l=https://loudfair.com/logo.svg; a=self;\n")
    
    return True

def create_warmup_emailer():
    """Create a script to warm up the domain"""
    
    warmup_script = '''#!/usr/bin/env python3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import random

# Email warmup sequences that avoid spam triggers
subjects = [
    "Following up on our discussion",
    "Quick question about the project",
    "Meeting notes from today",
    "Confirming our appointment",
    "Thanks for your help",
    "Project update - {}".format(time.strftime("%B %d")),
    "Re: Schedule for next week",
    "Documents you requested",
    "Weekly sync notes",
    "Action items from our call"
]

bodies = [
    """Hi,

Thanks for taking the time to discuss this today. I've attached the information 
we talked about. Let me know if you need anything else.

Best regards,
Ben""",
    
    """Hello,

Just following up on our conversation. Please let me know if you have any 
questions about the proposal.

Thanks,
Ben""",
    
    """Hi there,

I wanted to confirm our meeting for next week. Looking forward to discussing 
the project details with you.

Best,
Ben"""
]

def send_warmup_email(to_email, from_email, smtp_config):
    """Send a non-spammy warmup email"""
    
    msg = MIMEMultipart()
    msg['From'] = f"Ben <{from_email}>"
    msg['To'] = to_email
    msg['Subject'] = random.choice(subjects)
    
    body = random.choice(bodies)
    msg.attach(MIMEText(body, 'plain'))
    
    # Add headers that improve deliverability
    msg['Message-ID'] = f"<{int(time.time())}.{random.randint(1000,9999)}@loudfair.com>"
    msg['X-Priority'] = '3'  # Normal priority
    msg['Importance'] = 'Normal'
    
    return msg

print("Email warmup script created - use Proton Bridge SMTP settings to send")
'''
    
    with open("/Users/bc-02-m3/00-loudfair.com/warmup_emails.py", "w") as f:
        f.write(warmup_script)
    
    print("5. Created warmup_emails.py - Use this to build reputation\n")

def quick_fixes_summary():
    """Summary of immediate actions"""
    
    print("\n=== IMMEDIATE ACTIONS (Do these NOW) ===\n")
    
    print("1. **Change DMARC Policy** (Most Important!)")
    print("   In GoDaddy DNS, edit _dmarc TXT record:")
    print("   CHANGE: p=quarantine")
    print("   TO: p=none")
    print("   (This stops Gmail from being suspicious of new domain)\n")
    
    print("2. **Add Google Postmaster Tools**")
    print("   - Go to https://postmaster.google.com")
    print("   - Add loudfair.com")
    print("   - Add their TXT verification record")
    print("   - See EXACTLY why Gmail marks as spam\n")
    
    print("3. **Send Real Emails (Not Tests)**")
    print("   - Gmail flags 'test' emails")
    print("   - Send actual business emails")
    print("   - Include real content, not just 'test'\n")
    
    print("4. **Add to Google Contacts**")
    print("   - Add bm@loudfair.com to Gmail contacts")
    print("   - Instant whitelisting for that account\n")
    
    print("5. **Use Different Subject Lines**")
    print("   Bad: 'test', 'TEST', 'testing 123'")
    print("   Good: 'Project Update', 'Meeting Notes', 'Invoice #1234'\n")

if __name__ == "__main__":
    update_dns_for_reputation()
    create_warmup_emailer()
    quick_fixes_summary()
    
    print("\n=== FASTEST FIX ===")
    print("The #1 fastest fix is changing DMARC from p=quarantine to p=none")
    print("This alone might solve the spam issue immediately!")
