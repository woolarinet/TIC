import os
from http import HTTPStatus

import requests


GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
SLACK_HOOK_URL = 'https://hooks.slack.com/services/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'


def send_slack_message(data: dict):
    '''
    send slack message with hook

    :params:
        data: data should contains "text"

    {
        "text": "test mesage"
    }

    success message contains 'ok' with 200
    '''
    if 'text' not in data:
        raise ValueError('Slack data must have "text"')

    res = requests.post(
        url=SLACK_HOOK_URL,
        json=data,
    )
    try:
        assert res.status_code == HTTPStatus.OK
    except AssertionError:
        raise Exception(f'Send slack message faild: {res.status_code} with {res.text}')
