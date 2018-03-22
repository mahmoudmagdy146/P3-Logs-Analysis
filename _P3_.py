#!/usr/bin/env python

import psycopg2


def Ex_Query(query):
    """Connect to the database, runs the Query passed to it,
    and it will return the results"""
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    db.close()
    return result


# Question 1
def Most_Articles():
    """Return top 3 most read articles"""
    query1 = """
        SELECT article_view.title, article_view.view
        FROM article_view
        ORDER BY article_view.view DESC
        LIMIT 3;
    """
    result = Ex_Query(query1)
    print("TOP THREE ARTICLES BY PAGE VIEWS:")
    for (title, view) in result:
        print("    {} - {} views".format(title, view))
    print("=" * 60)


# Question 2
def Most_Article_Authors():
    """Return top 3 most popular authors"""
    query2 = """
        SELECT article_view.name, SUM(article_view.view) AS author_view
        FROM article_view
        GROUP BY article_view.name
        ORDER BY author_view DESC;
    """
    result = Ex_Query(query2)
    print("TOP THREE AUTHORS BY VIEWS:")
    for (name, view) in result:
        print("    {} - {} views".format(name, view))
    print("=" * 60)


# Question 3
def Days_Errors():
    """Return Days with more than 1% Errors"""
    query3 = """
        SELECT *
        FROM error_rate
        WHERE error_rate.percentage > 1
        ORDER BY error_rate.percentage DESC;
    """
    result = Ex_Query(query3)
    print("Days with more than 1% errors:")
    for (date, percentage) in result:
        print('    {0:%B %d, %Y} - {1:.1f}% errors'.format(date, percentage))
    print("=" * 60)


def main():
    """Generate report."""
    print('Calculating Results...\n')
    Most_Articles()
    Most_Article_Authors()
    Days_Errors()


if __name__ == '__main__':
    main()
