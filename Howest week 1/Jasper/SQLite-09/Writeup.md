# Description
Previous challenges all used a database with only one table. In the remaining challenges for this category, we will use airbnb.sqlite a multitable a database created using the open data from Inside Airbnb for the city of Gent in Belgium. The description of each table:

listings: this table contains the inventory of Airbnb units (e.g., rooms, apartments, etc.) located in Gent..
calendar: this table provides an overview of the availability of operating inventories in Gent for a specified period.
reviews: this table lists the submitted user reviews for the inventories in Gent.
☝️ Good to know: SQLite does not have a storage class set aside for storing dates and/or times. That is why in the airbnb database, date enteries are stored as TEXT.

☝️ Good to know: SQLite does not have a storage class set aside for storing Boolean values. It uses Integer values to represent true (1) and false (0). It however recognizes the keywords TRUE and FALSE, which are really just alternative spellings for the integer literals 1 and 0 respectively.

## Challenge: Identify Thomas in the Database
You have heard Shirin and Thomas having a conversation over Airbnb. This is what you heard:

Thomas is a host in Gent with an inventory located in "Muide - Meulestede - Afrikalaan" neigberhood.
Thomas has ever written a review for an Airbnb inventory in Gent.
In this exercise we want to identify Thomas in the database. Since he is a privacy freak he won't be using his real name as the username in airbnb. Can you out smart him and find him in this database? Use Thomas' user identifier to form the flag in the following form HCTF-FLAG-UserID (e.g. if Thomas ID is 111111 the flag will be HCTF-FLAG-111111)

### Disclosure: All the storylines in CTF challenges are fictitious. When teachers' names are used, it is only to add flavor to the challenge. Any resemblance to real persons, personal data, or real locations is purely coincidental.
# Resources
airbnb.sqlite
# Solution
1. open the advertisers.db file with sqlite3 `sqlite3 advertisers.db`
2. use `.header on` and `.mode column` to make it easier to read
3. Thomas has an airbnb in "Muide - Meulestede - Afrikalaan" and has posted a review.
4. So if we want to find Thomas his ID we have to find who meets both these requirements.
5. We do this with the query `select * from reviews where reviewer_id in (select host_id from listings where neighbourhood = 'Muide - Meulestede - Afrikalaan');`