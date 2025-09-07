#!/usr/bin/env python3
"""
Check if loudfair.com is properly configured and live
"""

import subprocess
import requests
import time

def check_dns():
    """Check DNS configuration"""
    print("Checking DNS records for loudfair.com...")
    print("=" * 50)
    
    # Check A records
    print("\nA Records:")
    a_records = subprocess.run(["dig", "+short", "A", "loudfair.com"], 
                              capture_output=True, text=True).stdout.strip()
    
    github_ips = ["185.199.108.153", "185.199.109.153", "185.199.110.153", "185.199.111.153"]
    
    if a_records:
        print(a_records)
        found_ips = a_records.split('\n')
        missing = [ip for ip in github_ips if ip not in found_ips]
        if not missing:
            print("✅ All GitHub Pages IPs configured!")
        else:
            print(f"❌ Missing IPs: {missing}")
    else:
        print("❌ No A records found - add them in GoDaddy!")
    
    # Check CNAME for www
    print("\nWWW CNAME:")
    cname = subprocess.run(["dig", "+short", "CNAME", "www.loudfair.com"], 
                          capture_output=True, text=True).stdout.strip()
    if cname:
        print(f"www.loudfair.com → {cname}")
        if "nebslim.github.io" in cname:
            print("✅ WWW CNAME correctly configured!")
        else:
            print("❌ WWW CNAME should point to nebslim.github.io")
    else:
        print("❌ No CNAME record for www")

def check_website():
    """Check if website is accessible"""
    print("\n\nWebsite Status:")
    print("=" * 50)
    
    urls = [
        "https://loudfair.com",
        "https://www.loudfair.com",
        "http://loudfair.com"
    ]
    
    for url in urls:
        try:
            response = requests.get(url, timeout=5, allow_redirects=True)
            if response.status_code == 200:
                print(f"✅ {url} - LIVE! (Status: {response.status_code})")
                if "Loud and Fair" in response.text:
                    print("   Content verified!")
            else:
                print(f"⚠️  {url} - Status: {response.status_code}")
        except Exception as e:
            print(f"❌ {url} - Error: {str(e)}")

def check_github_pages():
    """Check GitHub Pages status"""
    print("\n\nGitHub Pages Status:")
    print("=" * 50)
    
    url = "https://nebslim.github.io/loudfair/"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"✅ GitHub Pages site is live at: {url}")
        else:
            print(f"⚠️  GitHub Pages status: {response.status_code}")
    except Exception as e:
        print(f"❌ GitHub Pages error: {str(e)}")

if __name__ == "__main__":
    check_dns()
    check_website()
    check_github_pages()
    
    print("\n" + "=" * 50)
    print("If DNS records are missing, add them in GoDaddy!")
    print("DNS propagation can take 5-60 minutes.")
    print("SSL certificate provisioning can take up to 24 hours.")
