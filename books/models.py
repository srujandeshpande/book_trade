from django.db import models

class Books(model.Model):
    book_name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    published_date = models.DateTimeField('date published')

class Owners(model.Model):
    book = models.ForiegnKey(Books, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=200)
    buy_date = models.DateTimeField('date bought')
