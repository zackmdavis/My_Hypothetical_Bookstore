from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=60)
    authors = models.ManyToManyField('Author', null=True)
    publisher = models.ForeignKey('Publisher', null=True)
    publication_date = models.DateField(null=True)
    isbn = models.CharField(max_length=13, null=True)
    price = models.DecimalField(max_digits=16, decimal_places=2)

class Author(models.Model):
    name = models.CharField(max_length=60)

class Publisher(models.Model):
    name = models.CharField(max_length=60)
    website = models.URLField()


