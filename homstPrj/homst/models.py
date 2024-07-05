from django.db import models
from django.contrib.auth.models import User
from django import forms
import os
from uuid import uuid4
from django.utils import timezone

def upload_filepath(instance, filename):
    today_str = timezone.now().strftime("%Y%m%d")
    file_basename = os.path.basename(filename)
    return f'{instance._meta.model_name}/{today_str}/{str(uuid4())}_{file_basename}'

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
    image = models.ImageField(upload_to='accommodations/', blank=True, null=True)

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
    
class Post(models.Model):
    CATEGORY_CHOICES = [
        ('review', '여행 후기'),
        ('accommodation', '숙소 추천'),
        ('free', '자유'),
    ]
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='free')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    image = models.ImageField(upload_to='post/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_likes_count(self):
        return self.likes.count()
    
class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:20]
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')