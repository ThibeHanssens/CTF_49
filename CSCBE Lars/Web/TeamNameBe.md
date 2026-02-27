Context:
CSCBE competition, 2026

Team:
Lars Declercq (solo)


Name:
TeamNameBe's

Category:
Web

Hints, info:
Your favorite team is back.

TeamNameBE finally built a website. It's sleek and it definitely has no security issues whatsoever. None. Zero. Don't even look.

Files:
Instance

Write-up:
1. I first checked the /robots.txt when trying to access it it threw a 404 but they left django debug on so it gave me a lot of info:
- admin/
- [name='home']
- founders/ [name='founders']
- blog/ [name='blog']
- blog/<slug:slug>/ [name='blog_detail']
- register/ [name='register']
- login/ [name='login']
- logout/ [name='logout']
- profile/ [name='profile']
- ^media/(?P<path>.*)$ 
  
2. I then decided to check the admin page and decided to try some obviously bad password and username combinations to see if I can finesse my way in it didn't work
3. I then checked the media files to see where they are stored, when entering a bad url i see "/srv/app/media/flag" does not exist so i will now try to path my way to other stuff
4. I think the media is a dead end when trying to access anything outside of the path of "/srv/app/media it throws it is not allowed to do so