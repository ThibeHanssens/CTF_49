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
3. I also decided to try some sqli but that also didn't do much
4. I then checked the media files to see where they are stored, when entering a bad url such as: "/srv/app/media/flag" I get the error: `"/srv/app/media/flag" does not exist` now i found a path that i might be able to traverse through so i will now try to path my way to other stuff using `%2e%2e%2f`
5. I think the media is a dead end when trying to access anything outside of the path of "/srv/app/media" it throws it is not allowed to do so
6. When accessing a blog post i see it is incrementing numbers when changing the id to 13 i get an access denied page.
7. When making an account and logging in there is this comment block in the profile page html:
```HTML
<!--   
                TODO: Implement profile API endpoint
                Model fields for reference:
                    - user (FK → auth.User)
                    - is_team_member (Boolean, default=False)
                Endpoint: /api/profile/?user=<id>&is_team_member=<bool>
-->
```
This however lead nowhere
8. By generating a field error in the blog page i see the params that are available for filtering through:
- category
- content
- created_at
- featured
- id
- image
- members_only
- slug
- title
- visible

9. There is a django vulnerability with sql injection [here](https://www.endorlabs.com/learn/critical-sql-injection-vulnerability-in-django-cve-2025-64459)
10. When utilizing this on the /blog endpoint like this `/blog/?id=13&_connector=OR&members_only=True` the blog posts only available to members of the ctf team are visible
11. The flag is in the description of blog post 13