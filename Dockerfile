FROM python:3.8-alpine

WORKDIR app

COPY . ./

RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 5008

CMD [ "python", "basicBot.py" ]

