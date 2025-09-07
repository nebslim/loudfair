#!/usr/bin/env python3
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
