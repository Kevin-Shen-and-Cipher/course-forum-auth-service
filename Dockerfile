FROM python:3.10-slim-bullseye

WORKDIR /app
COPY . .

RUN apt-get update \
  && apt-get install -y --no-install-recommends --no-install-suggests \
  build-essential && pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir --requirement requirements.txt


EXPOSE 5000

CMD ["python3", "-u", "server.py"]