# Today I Commit Challenge
1일1커밋 챌린지를 위한 알림 봇

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


### References
+ https://docs.github.com/en/github/searching-for-information-on-github/searching-on-github/searching-commits
+ https://docs.github.com/en/rest/reference/activity

#### TODO

- [ ] move GITHUB_TOKEN into lambda function
- [ ] edit slack message

