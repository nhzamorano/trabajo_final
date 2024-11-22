FROM python:3.12.0 


WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt 
RUN apt-get update && apt-get install -y net-tools
COPY . .

EXPOSE 8000

CMD ["python", "app.py"]