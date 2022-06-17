# use python 3.9 image 
FROM python:3.9-alpine

# 
WORKDIR /app/atlan-ai

COPY . .
# 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN chmod +x start.sh

# 
CMD ["./start.sh"]