# use python 3.9 image 
FROM python:3.9-alpine

# 
WORKDIR /app

COPY . .
# 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN chmod +x start.sh

# 
CMD ["uvicorn", "app.main:app", "--host 0.0.0.0",  "--port=3000"]