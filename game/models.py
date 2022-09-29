from platform import platform
from django.db import models
from django.contrib.auth.models import User


class GameImages(models.Model):
    gameTitle = models.CharField(max_length=50, null=True, blank=True)
    imageOne = models.ImageField(
        null=True, blank=True, default='images/placeholder.png', upload_to='images/games')
    imageTwo = models.ImageField(
        null=True, blank=True, default='images/placeholder.png', upload_to='images/games')
    imageThree = models.ImageField(
        null=True, blank=True, default='images/placeholder.png', upload_to='images/games')
    imageFour = models.ImageField(
        null=True, blank=True, default='images/placeholder.png', upload_to='images/games')
    imageFive = models.ImageField(
        null=True, blank=True, default='images/placeholder.png', upload_to='images/games')
    _id = models.AutoField(primary_key=True, editable=False)
    fields = ['_id', 'imageOne', 'imageTwo',
              'imageThree', 'imageFour', 'imageFive']

    def __str__(self):
        return self.gameTitle


class GameSpecifications(models.Model):
    gameTitle = models.CharField(max_length=50, null=True, blank=True)
    osVersion = models.CharField(max_length=50, null=True, blank=True)
    cpu = models.CharField(max_length=50, null=True, blank=True)
    memory = models.CharField(max_length=50, null=True, blank=True)
    gpu = models.CharField(max_length=50, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)
    fields = ['_id', 'osVersion', 'cpu', 'memory', 'gpu']

    def __str__(self):
        return self.gameTitle


class Game(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=512, null=True, blank=True)
    publisher = models.CharField(max_length=50, null=True, blank=True)
    developer = models.CharField(max_length=50, null=True, blank=True)
    platform = models.CharField(max_length=50, null=True, blank=True)
    image = models.ForeignKey(GameImages, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    createdTime = models.DateTimeField(auto_now_add=True)
    specifications = models.ForeignKey(
        GameSpecifications, on_delete=models.CASCADE, null=True)
    key = models.URLField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)
    fields = ['_id', 'description', 'price', 'title']

    def __str__(self):
        return self.title
