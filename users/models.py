from django.db import models
from django.contrib.auth.models import AbstractUser

# AbstractUser의 모든 걸 사용하지만 내가 조작할 수 있는 class가 있는 것
class User(AbstractUser):
    pass
