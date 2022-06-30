FROM python:3.9-alpine

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 
WORKDIR /app/atlan-ai

COPY . .

COPY .env .
RUN apk update && apk add python3-dev \ 
    gcc \ 
    libc-dev \
    libffi-dev
RUN echo python --version

RUN pip install --upgrade pip wheel setuptools 
# 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN chmod +x start.sh

# 
CMD ["./start.sh"]
