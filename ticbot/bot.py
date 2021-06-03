import sys
import argparse
from datetime import datetime, timedelta, date
from typing import Optional

from pytz import timezone

from utils import send_slack_message
from github_graphql import get_not_commited_users


MEMBERS = [
    'bartkim0426',
    'yoonbr',
    'maintainker',
    'hoartist',
    'woolarinet',
    'che-ri',
    'DDAMDOO',
    'jeunbi95',
    'JuHyun419',
    'startFromBottom',
    'Jo-Yewon',
    'JadeyJ',
    'yoonbr',
    'ch200203',
    'Cenibee',
]


def run_tic_bot_per_today(usernames: list, date_str: str):
    '''
    run tic check for specific date and send message to slack channel

    :param:
        date_str: format should be yyyy-mm-dd
    '''
    date_from = datetime.strptime(date_str, '%Y-%m-%d').astimezone(tz=timezone('Asia/Seoul')).replace(hour=0, minute=0, second=0)
    date_to = date_from + timedelta(days=1)

    not_committed: list = get_not_commited_users(usernames, date_from=date_from, date_to=date_to)

    not_committed_msg: str = '\n'.join(not_committed)
    msg = f'''
{date_from.strftime("%Y-%m-%d")}
아직 커밋안하신 분~
(프라이빗 레포에 커밋하신분 제외)
===================
{not_committed_msg}
===================
'''
    send_slack_message({'text': msg})


def main(date_str):
    run_tic_bot_per_today(MEMBERS, date_str)
    print(f'Check TIC for {date_str} completed!')


if __name__ == '__main__':
    today = date.today().strftime('%Y-%m-%d')

    parser = argparse.ArgumentParser(description='TIC-bot')
    parser.add_argument('-d', '--date', type=str, help='date to check TIC in "yyyy-mm-dd" format', default=today)
    args = parser.parse_args(sys.argv[1:])
    main(args.date)
