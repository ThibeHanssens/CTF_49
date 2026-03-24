# Description
Online advertisement, is one of the channels political parties use to promote themselves to online users. Google services, such as YouTube is one of the attractive advertisement channels. Google is legally required to publish data about its political advertisement. advertisers.db contains advertisement information of Belgian, Flemish polictical parties. One party spent the highest amount of money on online advertisement, how much does this party spent on its advertisement? Use this number to form the flag. For example they spent 123 the flag would be HCTF-FLAG-123
# Resources
advertisers.db
# Solution
1. open the advertisers.db file with sqlite3 `sqlite3 advertisers.db`
2. with `.schema` we see that there is a political_ads table.
3. use `.header on` and `.mode column` to make it easier to read
4. We need to find the highest spend_eur in the table. Use the query `select max(spend_EUR) from political_ads;`
5. Then the flag is just HCTF-FLAG-(the value found)