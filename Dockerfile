FROM python:3.8

# Create app directory
WORKDIR /app

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

# Set the PYTHONPATH environment variable
ENV PYTHONPATH /app

# Bundle app source
COPY . .

EXPOSE 5010 5050

ENTRYPOINT ["python3"]
CMD ["./api/app.py"]