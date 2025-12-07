
FROM nikolaik/python-nodejs:python3.10-nodejs18

RUN apt-get update && apt-get install -y \
    git ffmpeg gcc g++ wget curl build-essential \
    libgl1 libglib2.0-0 libssl-dev \
    && rm -rf /var/lib/apt/lists/*


RUN git clone -b Yxzn-Userbot https://github.com/yusniii/Yxzn-Userbot /app
WORKDIR /app


RUN pip install --upgrade pip setuptools wheel

COPY requirements.txt /app/
RUN pip install -r requirements.txt --default-timeout=200

CMD ["bash", "start"]
