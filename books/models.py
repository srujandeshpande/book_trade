import datetime
from django.db import models
from django.utils import timezone

class Books(models.Model):
    book_name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    published_date = models.DateTimeField('date published')
    def __str__(self):
        return self.book_name
    def was_published_recently(self):
        return self.pub_data >= timezone.now() - datetime.timedelta(days=1)

class Owners(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=200)
    buy_date = models.DateTimeField('date bought')
    def __str__(self):
        return self.owner_name
