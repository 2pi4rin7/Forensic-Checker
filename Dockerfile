FROM python:3.10.11-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV TERM=xterm

# Install socat in one layer and clean apt cache
RUN apt-get update \
 && apt-get install -y --no-install-recommends socat curl ca-certificates \
 && rm -rf /var/lib/apt/lists/*

RUN mkdir /chall
WORKDIR /chall

COPY . /chall

RUN python3 -m pip install --no-cache-dir -r requirements.txt

RUN chmod +x server.py || true
RUN chmod +x flag.py || true

EXPOSE 1279/tcp

CMD ["socat", "-d", "TCP-LISTEN:1279,reuseaddr,fork", "EXEC:python3 ./server.py,stderr"]
