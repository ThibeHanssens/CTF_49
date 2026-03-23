# Description
Find the flag
# Resources
poetery.db
# Solution
1. open the poetery.db file with sqlite3 `sqlite3 poetery.db`
2. with `.schema` we see that there is only one table, sad_poet. this table has the columns ID, flag and remark.
3.  use `.header on` and `.mode column` to make it easier to read
4. if we look in the database with `select * from sad_poet limit 10` we see that they all have flag 0. The flag we are looking for probably has this value on 1.
5. To find the column with flag 1 we use this query: `select * from sad_poet where flag = 1;`