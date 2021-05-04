FROM tiangolo/uwsgi-nginx-flask


WORKDIR /opt/demo/
COPY /app .

RUN pip install -r requirements.txt

ENTRYPOINT python app.py