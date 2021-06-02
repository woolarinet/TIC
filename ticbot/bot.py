from datetime import datetime, timedelta

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


def run_tic_bot_per_today(usernames: list) -> list:
    '''
    run daily tic check and send message to slack channel
    '''
    today = datetime.now().astimezone(tz=timezone('Asia/Seoul')).replace(hour=0, minute=0, second=0)
    yesterday = today - timedelta(days=1)

    not_committed: list = get_not_commited_users(usernames, date_from=yesterday, date_to=today)

    not_committed_msg: str = '\n'.join(not_committed)
    msg = f'''
{yesterday.strftime("%Y-%m-%d")}
아직 커밋안하신 분~
===================
{not_committed_msg}
===================
'''
    send_slack_message({'text': msg})


if __name__ == '__main__':
    run_tic_bot_per_today(MEMBERS)
