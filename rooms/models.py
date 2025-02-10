from django.db import models
from common.models import CommonModel

class Room(CommonModel):

    """ Room Model Definition """

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = ("shared_room", "Shared Room")

    name = models.CharField(max_length=180, default="")
    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")
    price = models.PositiveIntegerField(default=0)  # 기본값 0원
    rooms = models.PositiveIntegerField(default=1)  # 기본값 1개
    toilets = models.PositiveIntegerField(default=1)  # 기본값 1개
    description = models.TextField(default="설명을 입력해주세요.")  # 기본 설명
    address = models.CharField(max_length=250, default="주소를 입력해주세요.")  # 기본 주소
    pet_friendly = models.BooleanField(default=True)
    kind = models.CharField(
        max_length=20, 
        choices=RoomKindChoices.choices, 
        default=RoomKindChoices.ENTIRE_PLACE  # 기본값을 'Entire Place'로 설정
    )
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
    amenities = models.ManyToManyField("rooms.Amenity")
    category = models.ForeignKey("categories.Category", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.name

class Amenity(CommonModel):

    """ Amenity Definition """

    name = models.CharField(max_length=150, default="기본 어메니티")  # 기본 어메니티 이름 설정
    description = models.CharField(max_length=150, null=True, blank=True, default="")  # 기본값 빈 문자열

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"