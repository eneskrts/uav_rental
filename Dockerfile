
FROM python:3.11.7
ENV PYTHONUNBUFFERED 1
ADD requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
RUN chmod a+x entrypoints/django.sh

