FROM python:3.14.3-slim-trixie

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# UPDATE AND INSTALL PYTHON PACKAGES
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# COPY PROJECT TO DOCKER
COPY . .

EXPOSE 8000
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
