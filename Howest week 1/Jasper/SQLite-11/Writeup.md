# Description
Combining the results of the last two challenges can you tell how much Thomas made via Airbnb bookings? Use the amount of money to form a flag in the following form HCTF-FLAG-ThomasIncome (e.g. if he has made 100 Euro, the flag would be HCTF-FLAG-100)
# Resources
airbnb.sqlite
# Solution
1. open the advertisers.db file with sqlite3 `sqlite3 advertisers.db`
2. use `.header on` and `.mode column` to make it easier to read
3. query id thomas: `select reviewer_id from reviews where reviewer_id in (select host_id from listings where neighbourhood = 'Muide - Meulestede - Afrikalaan');`
4. use this to get thomas'listing id: `select id from listings where host_id = (select reviewer_id from reviews where reviewer_id in (select host_id from listings where neighbourhood = 'Muide - Meulestede - Afrikalaan'));`
5. and now we need how many days his airbnb was rented and the price: `select c.listing_id, count(*) - sum(c.available), l.price from calendar c join listings l on c.listing_id = l.id where l.id = (select id from listings where host_id = (select reviewer_id from reviews where reviewer_id in (select host_id from listings where neighbourhood = 'Muide - Meulestede - Afrikalaan'))) group by c.listing_id;`
6. now just multiply the 2 numbers and you have the flag HCTF-FLAG-(the number)