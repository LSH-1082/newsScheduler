FROM python:3.9.6-slim

ENV TZ=Asia/Seoul

RUN apt-get update && apt-get install -y tzdata && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    apt-get clean

WORKDIR /app

COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

ENV PYTHONUNBUFFERED=1

CMD ["python", "-u", "main.py"]