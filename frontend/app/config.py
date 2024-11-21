import os

class Config:
    DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://admin:sistemas@172.18.195.238/citasmedicas?charset=utf8mb4')
