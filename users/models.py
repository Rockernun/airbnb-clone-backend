from django.db import models
from django.contrib.auth.models import AbstractUser

# AbstractUser의 모든 걸 사용하지만 내가 조작할 수 있는 class가 있는 것
class User(AbstractUser):
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    name = models.CharField(max_length=150, default="")
    is_host = models.BooleanField(default=False)  # 이전에 생성된 모든 사용자는 is_host 값을 default인 False로 받게 된다.