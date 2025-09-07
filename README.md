# Loudfair.com - An Eye for AI

A minimal landing page hosted on GitHub Pages with custom domain and Proton Mail integration.

## 🌐 Live Site
- **URL:** https://loudfair.com
- **GitHub Pages:** https://nebslim.github.io/loudfair/
- **Repository:** https://github.com/nebslim/loudfair

## 📁 Project Structure

```
/Users/bc-02-m3/00-loudfair.com/
├── index.html              # Main landing page
├── CNAME                   # GitHub Pages custom domain file
├── images/                 # Directory for images
├── scripts/                # Python scripts for DNS and email setup
│   ├── godaddy_dns_setup.py
│   ├── check_domain_status.py
│   ├── check_dns_records.py
│   └── fix_gmail_spam.py
├── docs/                   # Documentation and guides
│   ├── protonmail-godaddy-manual-setup.md
│   ├── dns-setup-checklist.txt
│   └── URGENT_DNS_FIXES.txt
├── deployment/             # Deployment related files
│   └── update_site.sh
└── venv/                   # Python virtual environment

```

## 🚀 Quick Start

### Update the Website
```bash
# Edit index.html with your changes
# Then run:
git add index.html
git commit -m "Update site"
git push origin main
```

### Check Domain Status
```bash
source venv/bin/activate
python scripts/check_domain_status.py
```

## 📧 Email Configuration

**Email:** bm@loudfair.com (Proton Mail)

### Current DNS Records:
- **MX Records:** Pointing to Proton Mail
- **SPF:** Configured for Proton Mail
- **DKIM:** 3 CNAME records for email authentication
- **DMARC:** Set to p=none for deliverability

## 🎨 Design

- **Background:** Off-black (#0d0d0d)
- **Text:** Off-white with varying opacity
- **Font:** SF Pro Display/Text
- **Style:** Minimal, centered layout
- **Content:** "an eye for ai" with email link

## 🔧 Technical Details

### GitHub Pages Setup
1. Custom domain configured via CNAME file
2. DNS A records pointing to GitHub's IPs:
   - 185.199.108.153
   - 185.199.109.153
   - 185.199.110.153
   - 185.199.111.153
3. SSL certificate automatically provisioned by GitHub

### Dependencies
- Python 3.x for scripts
- requests library (pip install -r requirements.txt)

## 📝 Common Tasks

### Add an Image
1. Place image in `images/` directory
2. Reference in HTML: `<img src="images/filename.jpg">`
3. Commit and push changes

### Update Email Address
1. Edit index.html
2. Change `bm@loudfair.com` to new email
3. Update mailto link

### Check DNS Propagation
```bash
dig +short A loudfair.com
dig +short MX loudfair.com
```

## 🔒 Security Notes

- GitHub token has been removed from scripts
- Use environment variables for sensitive credentials
- SSL certificate managed automatically by GitHub Pages

## 📞 Support

For issues:
1. Check domain status with provided scripts
2. Verify DNS records in GoDaddy
3. Email: bm@loudfair.com

---
Created: September 7, 2025
Last Updated: September 8, 2025
