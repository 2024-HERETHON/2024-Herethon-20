from django.db import models

# Create your models here.

class SafetyFilter(models.Model):
    CATEGORY_CHOICES = [
        ('female', '여성 전용 숙소'),
        ('mole_care', '몰카 안심 숙소'),
        ('restroom_separated', '화장실 남녀 분리'),
        ('cctv', 'CCTV 설치 유무'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='female')

    def __str__(self):
        return self.name

class SearchRecord(models.Model):
    DESTINATION_MAX_LENGTH = 200
    
    destination = models.CharField(max_length=DESTINATION_MAX_LENGTH)
    travel_date = models.DateField()
    travel_date2 = models.DateField(null=True, blank=True)
    people = models.PositiveIntegerField()
    safety_filter = models.ManyToManyField('SafetyFilter')

    def __str__(self):
        return f"{self.destination} - {self.travel_date} ~ {self.travel_date2} - {self.people}명"

class Accommodation(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    review_score = models.FloatField(max_length=200)
    price = models.PositiveIntegerField()
    safety_filters = models.ManyToManyField('SafetyFilter')

    def __str__(self):
        return self.name

class SortOption(models.Model):
    SORT_CHOICES = [
        ('price_asc', '가격 낮은 순서'),
        ('price_desc', '가격 높은 순서'),
        ('rating_asc', '별점 낮은 순서'),
        ('rating_desc', '별점 높은 순서'),
    ]

    sort_type = models.CharField(max_length=20, choices=SORT_CHOICES, unique=True)
    
    def __str__(self):
        return dict(self.SORT_CHOICES).get(self.sort_type, self.sort_type)