FROM python:3.12.8

RUN apt-get update && apt-get install -y \
    wget gnupg curl unzip \
    && wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | apt-key add - \
    && echo "deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main" > /etc/apt/sources.list.d/microsoft-edge.list \
    && apt-get update && apt-get install -y microsoft-edge-stable \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m test_user
WORKDIR /app

COPY ./requirements.txt /app



RUN pip3 install -r requirements.txt


USER test_user


