# Description
Using airbnb.sqlite your next flag will be the total booking days for inventories in the neighborhood "Moscou - Vogelhoek" in the following form HCTF-FLAG-TotalSum. For example if these inventories are booked in total for 999 days, your flag will be HCTF-FLAG-999.
# Resources
airbnb.sqlite
# Solution
1. open the advertisers.db file with sqlite3 `sqlite3 advertisers.db`
2. use `.header on` and `.mode column` to make it easier to read
3. To find the solution we need to find for every listing in "Moscou - Vogelhoek" the amount of days on the calendar minus the amount of booked days in the calendar.
4. The query for this: `SELECT c.listing_id, count(*) - sum(c.available)
FROM calendar c
JOIN listings l ON c.listing_id = l.listing_id
WHERE l.neighbourhood = 'Moscou - Vogelhoek'
GROUP BY c.listing_id;`
5. Then just take the sum of those numbers