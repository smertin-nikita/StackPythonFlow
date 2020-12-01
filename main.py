import requests
from pprint import pprint
from datetime import datetime, timedelta


def get_questions(date):
    """Returns all questions with tag 'python' since date"""

    response = requests.get(
        url='https://api.stackexchange.com/2.2/questions',
        params={
            'fromdate': date,
            'order': 'desc',
            'tagged': 'python',
            'filter': 'default',
            'site': 'stackoverflow'
        })
    response.raise_for_status()
    return response.json()


if __name__ == '__main__':
    delta = datetime.today() - timedelta(2)
    fromdate = delta.strftime('%Y-%m-%d')

    pprint(get_questions(fromdate))
