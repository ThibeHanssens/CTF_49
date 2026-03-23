# Description
Can you identify Shirin in the database. As a proof of your work, enter her client ID as the flag identifier HCTF-FLAG-CLIENTNUM

Hint 1: In case you forgot, Shirin has a PhD 🎓

Hint 2: To obtain more information about her you observed her at DAD today and noticed she paid for her meal using a Gold bank card.
# Resources
- BankChurners.sqlite
# Solution
flag is HCTF-FLAG-(shirin's client ID)

We know she has a doctorate, is a female and uses a gold card. with that information we can write this query to get her ID:

select * from customers_anon where education_level = 'Doctorate' and gender = 'F' and card_category = 'Gold';

However this gives us 3 results. one is 33, the others are 45 and 46. Shirin is not that old so if we try the id from 33 this is correct.