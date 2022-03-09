FROM python:3.8-slim-buster

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY notes_mysql.py my.conf ./
ENV FLASK_APP=notes_mysql.py
EXPOSE 5000/tcp
ENTRYPOINT [ "flask", "run"]
