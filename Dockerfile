FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt ticbot $LAMBDA_TASK_ROOT

WORKDIR $LAMBDA_TASK_ROOT
RUN pip install -r requirements.txt

ARG GITHUB_TOKEN
ENV GITHUB_TOKEN=$GITHUB_TOKEN

CMD ["lambda_app.handler"]
