from django.db import models
from django.db.models import Model, ImageField, CharField, TextField, DecimalField, DateTimeField



class Category(Model):
    image = ImageField(upload_to='categories/')
    name = CharField(max_length=255)


class Product(Model):
    title = ImageField(upload_to='category/')
    description = TextField()
    price = DecimalField(max_digits=9,decimal_places=2)
    image = ImageField(upload_to="products/")
    created_at = DateTimeField(auto_now_add=True)
