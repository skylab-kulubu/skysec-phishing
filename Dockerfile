FROM python:latest

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./phishing .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
