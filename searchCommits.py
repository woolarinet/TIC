import requests
import json
import datetime
import time
import config

github_token = config.github_token
slack_token = config.slack_token
channel = config.channel
member_list = config.member_list

# 슬랙 메시지 전송
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer " + token},
        data={"channel": channel,"text": text}
    )

# 특정 날짜 (committer-date) 이후의 커밋 기록을 요청
def commit_check(token, user, today):
  response = requests.get("https://api.github.com/search/commits?q=author:%s+committer-date:>%s" % (user, today),
      headers={
          "Accept": "application/vnd.github.cloak-preview+json",
          "Authorization": "Bearer " + token,
      }
  )
  result = json.loads(response.text)
  print("[%s]: %d" %(user, result["total_count"]))
  # 특정 날짜 (오늘 00시) 이후의 커밋 개수로 확인
  commit_count = result["total_count"]
  if commit_count !=0:
      print("\n\n[%s] OK\n\n" % (user))
      return True
  else:
      return False

not_commit = ''
# today = datetime.datetime.now()
yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
for i in member_list:
    # UTC 시간에 맞춰줌
    is_commit = commit_check(github_token, i, str(yesterday.date()) + "T15:00:00Z")
    if is_commit is False:
        not_commit += i + '\n'
# print(not_commit)

msg = "아직 커밋안하신 분~\n===============\n" + not_commit + "===============\n"
post_message(slack_token, channel, msg)
