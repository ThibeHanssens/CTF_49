# Description
Find the flag
# Resources
yet_another_poetery.db
# Solution
1. open the poetery.db file with sqlite3 `sqlite3 yet_another_poetery.db`
2. with `.schema` we see that there is the table romantic_poet with the columns ID and poem.
3. use `.header on` and `.mode column` to make it easier to read
4. The ID column is a number and auto incrementing and the poem is text. So it is most likely that the flag is somewhere in poem.
5. With the query `select * from romantic_poet where poem LIKE "%HCTF%";` we look for any poem that contains 'HCTF'
6. Then just look in the text for the flag