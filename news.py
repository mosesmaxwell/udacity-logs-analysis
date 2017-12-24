#!/usr/bin/env python

"""Log analysis of the news articles"""

from newsdb import *


def most_popular_three_articles():

    """
    What are the most popular three articles of all time
    """

    logs = get_most_popular_article()
    print('*******************')
    print('Top three articles!')
    print('*******************')
    row = 1
    for i in logs:
        print(str(row) + '. ' + i[0] + ' - ' + str(i[1]) + ' views')
        row += 1
    print('\n\n')


def most_popular_article_autors():

    """
    Who are the most popular article authors of all time
    """

    logs = get_most_popular_article_autors()
    print('*******************')
    print('Popular article authors!')
    print('*******************')
    row = 1
    for i in logs:
        print(str(row) + '. ' + i[0] + ' - ' + str(i[1]) + ' views')
        row += 1
    print('\n\n')


def popular_erros():

    """
    On which days did more than 1% of requests lead to errors
    """

    logs = get_popular_erros()
    print('*******************')
    print('Days with more than 1% of errors!')
    print('*******************')
    row = 1
    for i in logs:
        day = i[0].strftime('%B %d, %Y')
        err = str(round(i[1]*100, 1))
        print(day + ' - ' + err + ' % errors')
        row += 1
    print('\n\n')

if __name__ == '__main__':
    most_popular_three_articles()
    most_popular_article_autors()
    popular_erros()
