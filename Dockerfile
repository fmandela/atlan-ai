# use python 3.9 image 
FROM python:3.9-alpine

# 
WORKDIR /src

# 
COPY ./requirements.txt /src/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

# 
COPY ./src /src

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]

EXPOSE 3000