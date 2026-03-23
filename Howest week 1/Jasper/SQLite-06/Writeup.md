# Description
The Museum of Modern Art (MoMA) make information about its collection publicaly available. The dataset artists.db represents all the artists who have work in MoMA's collection. Artists of which nationality are mostly represented in MoMA's collection? Use this nationality to form the flag in the following form. For example if the most frequent nationality Utopian is your flag will be HCTF-FLAG-Utopian.
# Resources
artists.db
# Solution
1. open the artists.db file with sqlite3 `sqlite3 artists.db`
2. with `.schema` we see that there is one artists table.
3. use `.header on` and `.mode column` to make it easier to read
4. We need to find the most common nationality. We do this with this query: `select count(*), Nationality from artists group by(Nationality) order by count(*) desc LIMIT 1;`
5. Then the flag is just HCTF-FLAG-(the nationality)