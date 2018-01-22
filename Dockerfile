FROM python:3

WORKDIR /app

ADD . /app

RUN pip3 install -r requirements.txt

CMD ["source", "conf.sh"]

CMD ["python", "search.py"]
