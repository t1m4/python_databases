FROM python:latest
WORKDIR /home
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
#CMD ["python", "-u", "postgresql.py"]