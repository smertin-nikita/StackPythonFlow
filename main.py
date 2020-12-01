import requests
from pprint import pprint

if __name__ == '__main__':
    response = requests.get(
        url='https://api.stackexchange.com/2.2/questions',
        params={
            'fromdate': '2020-11-28',
            'order': 'desc',
            'tagged': 'python',
            'filter': 'default',
            'site': 'stackoverflow'
        })
    response.raise_for_status()
    pprint(response.json())
