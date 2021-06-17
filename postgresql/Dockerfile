FROM python:latest
WORKDIR /home
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5432
COPY . .
CMD ["python", "postgresql.py"]