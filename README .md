# Log Analysis Project BY Mahmoud Magdy	

-This is project to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.
   
-This Project answered the three Quation:

   - What are the most popular three articles of all time?
   - Who are the most popular article authors of all time?
   - On which days did more than 1% of requests lead to errors?
   
            ******************************************
            
-How to run the project :-  
  
  - Install Vagrant and VirtualBox Link :"https://www.vagrantup.com/".
  - Download the VM configuration Link : "https://www.virtualbox.org/"
     - use Github to fork and clone the repository	
        "https://github.com/udacity/fullstack-nanodegree-vm".
  - Start the VM:
     - from the bash git, run the vagrant up and run the vagrant ssh to log in.
  - Download the database setup: 
        "https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip"
  - Extract compressed file 'P3'.
  - Then cd into the vagrant directory and then cd to 'log analysis project' file 
  - Setup  the Database
    - use the following command 'psql -d news -f newsdata.sql'
  - Make Views by running the queries belwo.
    - Run this command 'python _P3_.py'
    
        *************************************************

-Creat Views :

- I create database views:

  1 -   CREATE VIEW author_info AS
	SELECT authors.name, articles.title, articles.slug
        FROM articles, authors
	WHERE articles.author = authors.id
	ORDER BY authors.name;
  
  2 -   CREATE VIEW path_view AS
	SELECT path, COUNT(*) AS view
	FROM log
	GROUP BY path
	ORDER BY path;

  3-	CREATE VIEW article_view AS
	SELECT author_info.name, author_info.title, path_view.view
	FROM author_info, path_view
	WHERE path_view.path = CONCAT('/article/', author_info.slug)
	ORDER BY author_info.name;

4-	CREATE VIEW total_view AS
	SELECT date(time), COUNT(*) AS views
	FROM log 
	GROUP BY date(time)
	ORDER BY date(time);

5-	CREATE VIEW error_view AS
	SELECT date(time), COUNT(*) AS errors
	FROM log WHERE status = '404 NOT FOUND' 
	GROUP BY date(time) 
	ORDER BY date(time);

6-	CREATE VIEW error_rate AS
	SELECT total_view.date, (100.0*error_view.errors/total_view.views) AS percentage
	FROM total_view, error_view
	WHERE total_view.date = error_view.date
	ORDER BY total_view.date;	
        *****************************************************

- What's included

  - _P3_.py :- This is the main code for the application
                               
  - newsdata.sql :- it is the database that includes three tables:
                    1-The authors table that contain information about the authors of articles.
                    2-The articles table that contain the articles themselves.
                    3-The log table that contain one entry for each time a user has accessed the site.


  

  