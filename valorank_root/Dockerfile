FROM python:3.10

WORKDIR app/

ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update
RUN apt-get install netcat -y
RUN apt-get upgrade -y
RUN apt-get install -y postgresql gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


COPY . .

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["sh", "/app/entrypoint.sh"]