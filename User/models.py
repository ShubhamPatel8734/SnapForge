from django.db import models
from db_connection import db

# Create your models here.

user_collection = db['user']
images_collection = db['images']
