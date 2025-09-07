# Proton Mail + GoDaddy Manual DNS Setup Guide

## Step 1: Add Verification TXT Record

1. Log in to your [GoDaddy account](https://account.godaddy.com)
2. Click on **My Products**
3. Find **loudfair.com** and click **DNS** button
4. Click **Add** button in the DNS Records section
5. Add the following record:
   - **Type:** TXT
   - **Name:** @ 
   - **Value:** `protonmail-verification=6d50e400e1ecc8b9c648c50477e351385a242bb1`
   - **TTL:** 1 Hour
6. Click **Save**

## Step 2: Verify Domain in Proton Mail

1. Go back to Proton Mail domain settings
2. Click **Verify** button
3. Wait for verification (may take 5-15 minutes)
4. Once verified, Proton Mail will show you the email DNS records

## Step 3: Add Email DNS Records in GoDaddy

Go back to GoDaddy DNS management and add these records:

### MX Records (for receiving email)

**First MX Record:**
- **Type:** MX
- **Name:** @
- **Priority:** 10
- **Value:** mail.protonmail.ch
- **TTL:** 1 Hour

**Second MX Record:**
- **Type:** MX
- **Name:** @
- **Priority:** 20
- **Value:** mailsec.protonmail.ch
- **TTL:** 1 Hour

### SPF Record (for email authentication)
- **Type:** TXT
- **Name:** @
- **Value:** `v=spf1 include:_spf.protonmail.ch ~all`
- **TTL:** 1 Hour

### DKIM Records (Proton Mail will provide these after verification)
You'll need to add 3 CNAME records. They will look like:

**DKIM 1:**
- **Type:** CNAME
- **Name:** protonmail._domainkey
- **Value:** [Proton Mail will provide]
- **TTL:** 1 Hour

**DKIM 2:**
- **Type:** CNAME
- **Name:** protonmail2._domainkey
- **Value:** [Proton Mail will provide]
- **TTL:** 1 Hour

**DKIM 3:**
- **Type:** CNAME
- **Name:** protonmail3._domainkey
- **Value:** [Proton Mail will provide]
- **TTL:** 1 Hour

### Update DMARC Record
You already have a DMARC record. You'll need to edit it:

1. Find the existing DMARC TXT record (_dmarc)
2. Click **Edit**
3. Change the value to: `v=DMARC1; p=quarantine; rua=mailto:dmarc@loudfair.com`
   (Replace dmarc@loudfair.com with your actual email address)
4. Save

## Important Notes:

- **Delete any existing MX records** before adding Proton Mail's MX records
- DNS changes can take up to 24-48 hours to fully propagate
- The @ symbol in the Name field means the record applies to your root domain
- Don't add quotes around any values
- Make sure to copy values exactly as shown

## After DNS Setup:

1. In Proton Mail, go to **Settings** > **All settings** > **Proton Mail** > **Addresses**
2. Click **Add address** to create email addresses (e.g., info@loudfair.com)

## Troubleshooting:

- If verification fails, double-check the TXT record value is copied exactly
- Use [MXToolbox](https://mxtoolbox.com/SuperTool.aspx) to verify your DNS records
- Check [DNS Checker](https://dnschecker.org) to see propagation status
