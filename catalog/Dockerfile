FROM python:3.13-bullseye

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "python", "-m", "manage.py", "runserver", "0.0.0.0:8000" ]