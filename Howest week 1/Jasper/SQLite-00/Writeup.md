# Description
In CTF we will be using SQLite as our database engine. Open SQLite3 in your terminal using sqlite3 command which comes included with your Linux distribution. Download the BankChurners.sqlite file. In your terminal, browse to the directory that contains this file. Enter the following command to load the database and enter the SQLite environment: sqlite3 BankChurners.sqlite

Inspect the database
Start browsing the database using the following command that shows the tables in the database: .tables As you see the output indicates there is only one table in this database which is called customers_anon. Use one of the following command to see the columns in this table.

Using .schema

 .schema customers_anon
Or pragma:

 .header on
 .mode column
 pragma table_info('customers_anon');
Based on the columns in this table, you can already tell that it contains information about the customers of a bank.

Tip: When using with databases, don't forget to pay extra attention to typos. Don't forget to reading the errors message patiently. They usually contain enough information to help you :)

Based on the columns in this table, you can already tell that it contains information about the customers of a bank.

Start querying the database
Now that we know more about the structure of data is in this database, let's start querying its table to gain more insights. Querying tables in SQLite is very similar to SQL Server (what we hope you to still remember from last semester). One of the few differences is the syntax for limiting the number of results returned by a query. In SQL Server, this is done using the TOP keyword, while in SQLite, you use the limit clause. Here’s how you can inspect the first 10 rows in the table:

    select * from customers_anon limit 10;
To warm up let's check the number of rows in this table using the following command:

    select count(*) from customers_anon;
Now let's see what values certain columns of the table can take. Inspect the values that column Gender, Education_Level, Marital_Status and Income_Category can take.

select distinct Gender from customers_anon;
select distinct Education_Level from customers_anon;
select distinct Marital_Status from customers_anon;
select distinct Income_Category from customers_anon;
Capture the Flag:
As you have noticed, the table contains a Customer_Age column. Use the age of the youngest and oldest customer to form the flag in the following form HCTF-FLAG-YougestOldest. For example, if the youngest customer is 12 and the oldest is 99 the flag will be HCTF-FLAG-1299).

# Resources
- BankChurners.sqlite

# Solution
flag is HCTF-FLAG-YoungesOldest
youngest = select min(Customer_Age) from customers_anon; -> 26
olders = select max(Customer_Age) from customers_anon; -> 73
so flag becoes HCTF-FLAG-2673