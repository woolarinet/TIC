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

# 레포지토리 목록을 보고 각 레포지토리의 커밋기록을 살핌
def commit_check(token, user, today):
  check = False
  response = requests.get("https://api.github.com/users/%s/repos?per_page=100" % (user),
      headers={
          "Accept": "application/vnd.github.cloak-preview+json",
          "Authorization": "Bearer " + token,
      }
  )
  repos = json.loads(response.text)
  for i in repos:
      # 각 레포지토리의 커밋 기록을 요청
      response = requests.get("https://api.github.com/repos/%s/%s/commits" % (user, i["name"]),
          headers={
              "Accept": "application/vnd.github.cloak-preview+json",
              "Authorization": "Bearer " + token,
          }
      )
      commits = json.loads(response.text)
      # 빈 레포지토리는 dict를 응답
      if type(commits) is not dict:
          date = commits[0]['commit']['author']['date']
          # 가장 최근 커밋기록의 날짜의 형태를 바꾸어 오늘 날짜와 비교
          dt = date.split('T')
          comp1 = dt[0]
          comp2 = dt[1].split('Z')[0]
          temp = datetime.datetime.strptime(comp1 + ' ' + comp2, "%Y-%m-%d %H:%M:%S")
          # UTC 시간에 맞춰줌
          temp += datetime.timedelta(hours=9)
          print("[%s] -> <%s>: %s" % (user, i["name"], str(temp)))
          if str(temp).split(' ')[0] == today:
              check = True
              print("\n\n[%s] OK\n\n" % (user))
              break
  return check

now = datetime.datetime.now()
today = str(now.date())
not_commit = ''

for i in member_list:
    is_commit = commit_check(github_token, i, today)
    if is_commit is False:
        not_commit += i + '\n'

# print(not_commit)
msg = "아직 커밋안하신 분~\n===============\n" + not_commit + "===============\n"
post_message(slack_token, channel, msg)


