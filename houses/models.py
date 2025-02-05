from django.db import models

# 모델이므로 models.Model을 상속 받음
class House(models.Model):

    """ Model Definition for Houses """

    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
