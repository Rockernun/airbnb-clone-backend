from django.db import models

# 모델이므로 models.Model을 상속 받음
class House(models.Model):

    """ Model Definition for Houses """

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True)

    # admin 패널에서 house의 이름으로 보이도록 설정
    def __str__(self):
        return self.name