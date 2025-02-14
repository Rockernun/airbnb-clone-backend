from django.contrib import admin
from .models import Review

class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, queryset):  # reviews -> queryset (일관성 유지)
        print("Score Filter Value:", self.value())
        score = self.value()  # 선택된 필터 값 가져오기
        
        if score == "bad":
            return queryset.filter(rating__lte=3)
        elif score == "good":
            return queryset.filter(rating__gte=4)
        return queryset  # None일 경우 전체 결과 반환

class ScoreFilter(admin.SimpleListFilter):
    title = "Filter by score!"
    parameter_name="score"

    def lookups(self, request, model_admin):
        return [
            ("bad", "Bad"),
            ("good", "Good"),
        ]
    
    def queryset(self, request, reviews):
        score = self.value()
        if score == "bad":
            return reviews.filter(rating__lte=3)
        else:
            return reviews.filter(rating__gte=4)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    
    list_display = (
        "__str__",
        "payload",
    )

    list_filter = (
        WordFilter,
        ScoreFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
