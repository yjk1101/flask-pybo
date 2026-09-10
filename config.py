import os

BASE_URL = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_URL, 'pybo.db')}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

