# FROM debian

# RUN apt-get update && apt-get install python3 -y

# WORKDIR /app

# COPY app.py .
# RUN chmod +x app.py

# CMD ["python3", "app.py"]


FROM python:3.9

WORKDIR /application

COPY ./requirements.txt .
COPY ./src .

RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"]