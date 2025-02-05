from django.db import models

# 모델이므로 models.Model을 상속 받음
class House(models.Model):

    """ Model Definition for Houses """

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(verbose_name="Price", help_text="Positive Numbers Only")
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(verbose_name="Pets Allowed?", default=True, help_text="Does this house allow pets?")

    # admin 패널에서 house의 이름으로 보이도록 설정
    def __str__(self):
        return self.name