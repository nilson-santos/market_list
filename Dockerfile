FROM python:3.12-alpine

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install django

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]