import os
from string import Template
from http import HTTPStatus
from datetime import datetime

import requests


GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
GITHUB_GRAPHQL_URL = 'https://api.github.com/graphql'
GRAPHQL_QUERY_TEMPLATE_STRING = '''
{
 user(login: "$username") {
    login,
    contributionsCollection(to:"$date_to", from: "$date_from") {
      commitContributionsByRepository {
        contributions (first:1, orderBy:{field: OCCURRED_AT, direction: DESC}) {
          nodes{
            occurredAt,
            commitCount,
            repository {
              url
            },
          }
        }
      }
    }
  }
}
'''


def call_github_graphql(query: str):
    '''
    call github graphql for query

    :params:
        query: valid graphql query
    '''
    if not GITHUB_TOKEN:
        raise Exception('GITHUB_TOKEN must be set in environment variable')

    res = requests.post(
        url=GITHUB_GRAPHQL_URL,
        headers={'Authorization': f'bearer {GITHUB_TOKEN}'},
        json={'query': query}
    )
    if res.status_code == HTTPStatus.OK:
        return res.json()
    else:
        raise Exception(f'Query failed: {res.status_code}/{res.json()}')


def call_github_commit_query(github_username: str, date_from: datetime, date_to: datetime) -> dict:
    '''
    call github graphql for check last commit between date_from and date_to

    :params:
        github_username
        date_from
        date_to

    Usage
    >>> date_from = datetime(2021, 6, 1)
    >>> date_to = datetime(2021, 6, 2)
    >>> call_github_commit_query('bartkim0426', date_to, date_from)
    True
    '''
    query = Template(GRAPHQL_QUERY_TEMPLATE_STRING).substitute(
        username=github_username,
        date_to=date_to.isoformat(),
        date_from=date_from.isoformat()
    )
    return call_github_graphql(query)


def is_commit_on(graphql_result: dict) -> bool:
    '''
    Check if github user commit on specific date between date_from and date_to
    '''
    try:
        result_list: list = graphql_result['data']['user']['contributionsCollection']['commitContributionsByRepository']
    except (TypeError, KeyError):
        raise ValueError(f'Graphql query invalid: {graphql_result}')
    return True if result_list else False


def get_not_commited_users(usernames: list, date_from: datetime, date_to: datetime):
    not_committed: list = []
    for username in usernames:
        result = call_github_commit_query(username, date_from, date_to)
        if not is_commit_on(result):
            not_committed.append(username)
    return not_committed
