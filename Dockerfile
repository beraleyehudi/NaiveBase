FROM python:3

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt



WORKDIR /app

COPY . .


EXPOSE 8000

CMD ["fastapi", "run", "classifier_server.py", "--port", "8000"]