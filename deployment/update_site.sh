#!/bin/bash
# Simple script to update your landing page

echo "🚀 Updating loudfair.com..."

# Add all changes
git add .

# Commit with message
if [ -z "$1" ]; then
    git commit -m "Update landing page"
else
    git commit -m "$1"
fi

# Push to GitHub (will prompt for credentials if needed)
git push origin main

echo "✅ Site updated! Changes will appear in 1-2 minutes."
echo "🌐 View at: https://loudfair.com"
