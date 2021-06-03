$(aws ecr get-login --no-include-email --region ap-northeast-2)
docker build --build-arg GITHUB_TOKEN=$GITHUB_TOKEN -t ticbot .
docker tag ticbot:latest 622385363639.dkr.ecr.ap-northeast-2.amazonaws.com/ticbot:latest
docker push 622385363639.dkr.ecr.ap-northeast-2.amazonaws.com/ticbot:latest
