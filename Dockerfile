FROM python:3
ENV PYTHONUNBUFFERED 1
COPY test_task/ /test_task/
COPY requirements.txt /test_task/
WORKDIR /test_task
RUN pip install --upgrade pip && pip install -r requirements.txt
