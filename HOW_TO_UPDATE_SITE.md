# How to Update Your Site

## Quick Update Steps

### 1. Change Text on Website

Edit `index.html`:
```html
<h1><span class="full-opacity">an eye</span> <span class="reduced-opacity">for ai</span></h1>
```

### 2. Save and Push Changes

Run these commands:
```bash
git add index.html
git commit -m "Update text"
git push origin main
```

Changes appear in 1-2 minutes!

### 3. Add an Image

1. Put image in `images/` folder
2. Add to HTML:
```html
<img src="images/your-image.jpg" alt="Description" style="width: 100px;">
```
3. Push changes:
```bash
git add images/your-image.jpg index.html
git commit -m "Add image"
git push origin main
```

## Common Updates

### Change Background Color
In `index.html`, find:
```css
background-color: #0d0d0d;
```
Change to any color you want.

### Change Text Size
Find:
```css
font-size: 1.2rem;
```
Make it bigger or smaller.

### Change Email
Find all instances of:
```
bm@loudfair.com
```
Replace with new email.

## Check Site Status

```bash
# See if site is working
curl -I https://loudfair.com

# Check DNS
dig loudfair.com

# View locally
open index.html
```

## Need Help?

1. All scripts are in `scripts/` folder
2. Documentation in `docs/` folder
3. Email: bm@loudfair.com

Remember: Always test locally before pushing!
