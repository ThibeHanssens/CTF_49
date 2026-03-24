# Description
As you might have noticed, this database doesn't contain any obvious personal information (e.g. name, or identity numbers). The bank would argue that is a so-called "anonymized" dataset that can't be used for identifying individual customers. However, as you will see in this challenge, data anonymization is a very difficult tasks and there are multiple ways in which you can identify individuals in a dataset and figure out their income.

## Identify Wouter
Let's imagine that you're trying to figure out Wouter's income. You know that he recently turned 61 and that he is divorced. As a proof of your work, enter his client ID as the flag identifier HCTF-FLAG-CLIENTNUM.

### Disclosure: All the storylines in CTF challenges are fictitious. When teachers' names are used, it is only to add flavor to the challenge. Any resemblance to real persons, personal data, or real locations is purely coincidental.

# Resources
- BankChurners.sqlite
# Solution
The flag is in the format HCTF-FLAG-(client id num)

We know Wouter is 61, divorced and a man. with that information we can make this query:
select * from customers_anon where customer_age = 61 and marital_status = 'Divorced' and gender = 'M';