# Today I Commit Challenge
1일1커밋 챌린지를 위한 알림 봇
### config.py
``` python
github_token = "github private access key"
slack_token = "slack authorization token"
channel = "slack channel"
member_list = ["TIC member's github name list"]
```
### searchWithRepo.py
각 멤버별 레포지토리 목록을 가져오고 각 레포지토리 별 커밋 기록 확인.
레포지토리가 100개가 넘어가는 멤버가 있다면 따로 로직을 추가해야합니다.
* 레포지토리 목록에 없는 레포지토리 같은 경우는 contribution에 올라와도 가져오지 못합니다..

### searchCommits.py
/search/commits 로 요청을 보내 특정 날짜 이후의 커밋 기록을 확인.
* 이유는 모르겠지만 commit을 했음에도 불구하고 total_count가 0이 찍히는 경우가 있습니다..

### References
+ https://docs.github.com/en/github/searching-for-information-on-github/searching-on-github/searching-commits
+ https://docs.github.com/en/rest/reference/activity


### update

- working based on python version: 3.9.0, OS X
- will be send message to slack channel: [#tic-bot-noti](https://tic-challenge.slack.com/archives/C023T4H7ECA)
#### Prerequisite
- Can generate token [here](https://github.com/settings/tokens)
- Add token in `env` file and `GITHUB_TOKEN` in environment variable

```
source env
```

#### Execute

```
# (Optinoal) create venv

# install dependencies
pip install -r requirements.txt

# run bot
cd ticbot
python bot.py
```

### Deployment

deploy with AWS Lambda

```
# set GITHUB_TOKEN to environment variable from .env
source .env

# build and push docker image to ECR
./build.sh

# Deploy new image to lambda in console
```

- lambda function si triggerd by cloudwatch schedule with `cron(0 14 * * ? *)` (UTC)

#### TODO

- [ ] move GITHUB_TOKEN into lambda function
- [ ] edit slack message
