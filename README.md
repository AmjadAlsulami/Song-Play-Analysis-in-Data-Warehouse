# Song Play Analysis in  Data Warehouse
## Problem Statment
A music streaming startup, Sparkify wants to build an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to.  

## Project Steps
Load data from S3 to staging tables on Redshift and execute SQL statements that create the analytics tables from these staging tables.
# Schema 
1. The fact table \*songplay
* songplay table  which contains (songplay_id, start_time, user_id,level,song_id, artist_id, session_id     ,location, user_agent)
2. The dimention Table
* users table which contains(user_id,first_name,last_name,gender,level)
* songs table (song_id ,title,artist_id,year,duration)
* artists table (artist_id,name,location,latitude,longitude) 
* time table (start_time ,hour,day,week,month,year,weekday)     


## ETL process

In this project most of ETL is done with SQL (Python used just as bridge), transformation and data normalization is done by Query, check out the sql_queries python module

## How to run

Although the data-sources are provided by two S3 buckets the only thing you need for running the example is an AWS Redshift Cluster up and running And Python.
1. The etl.py will load data from S3 to staging tables on Redshift.
2. After that, etl.py will load data from staging tables to analytics tables on Redshift.
3. You can test by running etl.py after running create_tables.py and running the analytic queries on the Redshift database .
Delete your redshift cluster when finished.

