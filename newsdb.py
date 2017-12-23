#!/usr/bin/env python

"""This file implements the requested db quries and return results"""

import psycopg2

DBNAME = "news"

def execute_query(query):
    """Run the query and return results"""

    conn = psycopg2.connect(database=DBNAME)
    cur = conn.cursor()
    cur.execute(query)
    records = cur.fetchall()
    conn.close()
    return records

def get_most_popular_article():
    """
    1. What are the most popular three articles of all time?
    Which articles have been accessed the most?
    Present this information as a sorted list with the most popular article at the top.
    """

    query = """
      SELECT a.title, count(*) as num
      FROM articles a 
      JOIN log l 
      ON l.path LIKE '%' || a.slug
      GROUP BY a.title 
      ORDER BY num DESC 
      LIMIT 3"""
    results = execute_query(query)
    return results

def get_most_popular_article_autors():
    """
    2. Who are the most popular article authors of all time?
    That is, when you sum up all of the articles each author has written,
    which authors get the most page views?
    Present this as a sorted list with the most popular author at the top.
    """

    query = """
      SELECT a.name, count(*) AS num
      FROM authors a 
      JOIN articles ar  
      ON a.id = ar.author
      JOIN log l
      ON l.path LIKE '%' || ar.slug
      GROUP BY a.name 
      ORDER BY num DESC
      """
    results = execute_query(query)
    return results

def get_popular_erros():
    """
    3. On which days did more than 1% of requests lead to errors?
    The log table includes a column status that indicates the HTTP status code
    that the news site sent to the user's browser.
    """

    query = """
      SELECT t.day, ROUND(((e.err*1.0) / t.reqs) , 3) AS percent
      FROM (SELECT date_trunc('day', time) "day", count(*) AS err FROM log WHERE status LIKE '404%' GROUP BY day) AS e 
      JOIN (SELECT date_trunc('day', time) "day", count(*) AS reqs FROM log GROUP BY day) AS t 
      ON e.day = t.day 
      WHERE (ROUND(((e.err*1.0) / t.reqs) , 3) > 0.01)
      ORDER BY percent DESC
      """
    results = execute_query(query)
    return results
