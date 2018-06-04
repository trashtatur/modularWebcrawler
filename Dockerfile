FROM python

MAINTAINER andreas.hoerster@haw-hamburg.de

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app


CMD ["python","-m","web.frontend.py"]