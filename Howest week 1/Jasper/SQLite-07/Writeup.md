# Description
The infosec-jobs.com performed a survey to collect information about the salaries of professionals working in cybersecurity. Which job has the highest number of employees in this database? Use the job title to form the flag using CamelCase convention in case the job title is multiword. For example if the job title is "Being An Engineer" the flag will be HCTF-FLAG-BeingAnEngineer.
# Resources
cyber-jobs.db
# Solution
1. open the cyber-jobs.db file with sqlite3 `sqlite3 cyber-jobs.db`
2. with `.schema` we see that there is a cyber_employees table.
3. use `.header on` and `.mode column` to make it easier to read
4. We need to find the most common job. We do this with this query: `select count(*), job_title from cyber_employees group by(job_title) order by count(*) desc LIMIT 1;`
5. Then the flag is just HCTF-FLAG-(the job in camelcase)