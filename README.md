# Log Analysis
Analyse logs of news articles by fetching results using postgres sql quries.

Tools Used
----------------
prerequisite: newsdata.sql
Python (v3.6.3 and above)
Postgress SQL
Virtual Machine v5.1
Vagrant v1.9.1

Steps to Run:
-------------
1. newsdata.sql already loaded in postress sql installed in VM Vagrant
2. Clone git repository https://github.com/mosesmaxwell/udacity-logs-analysis.git or Download the zip file
3. Unzip/Go to the downloaded folder
4. Copy the project folder in to your VM vagrant folder
5. Run the news.py python file in terminal
6. Analysis results will show in the VM terminal

Logs Description
----------------
1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

Output
----------------
*******************
Top three articles!
*******************
1. Candidate is jerk, alleges rival - 338647 views
2. Bears love berries, alleges bear - 253801 views
3. Bad things gone, say good people - 170098 views


*******************
Popular article authors!
*******************
1. Ursula La Multa - 507594 views
2. Rudolf von Treppenwitz - 423457 views
3. Anonymous Contributor - 170098 views
4. Markoff Chaney - 84557 views


*******************
Days with more than 1% of errors!
*******************
July 17, 2016 - 2.3 % errors
