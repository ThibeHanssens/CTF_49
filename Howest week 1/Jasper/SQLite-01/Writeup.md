# Description
Using the BankChurners.sqlite file from challenge SQLite-00, write a query to find out how many customers have the most frequent income category in this bank. Your flag will be the total number of customer having that income level HCTF-FLAG-TotalCustomers. For example if there are 9999 customers with that income, your flag will be HCTF-FLAG-9999.
# Resources
- BankChurners.sqlite
# Solution
flag is HCTF-FLAG-(amount of most common income category)

to get the most common income category we use this query:
select count(*),income_category from customers_anon group by(income_category) order by count(*) desc limit 1;