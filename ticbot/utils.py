import os
from http import HTTPStatus

import requests


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
