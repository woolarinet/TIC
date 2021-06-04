from datetime import date

from bot import main


def handler(event, context):
    '''lambda handler function'''
    today = date.today().strftime('%Y-%m-%d')
    main(today)
