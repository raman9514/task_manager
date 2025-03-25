FROM python:3.12-slim

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1 

RUN pip install --upgrade pip 

COPY requirements.txt  /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]