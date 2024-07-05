from django.contrib import admin
from .models import SafetyFilter, Accommodation,  SearchRecord, SortOption, Post, Comment

# Register your models here.

@admin.register(SafetyFilter)
class SafetyFilterAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)
    list_filter = ('category',)

@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'review_score', 'price', 'image')
    search_fields = ('name', 'location')
    list_filter = ('safety_filters',)
    filter_horizontal = ('safety_filters',)

@admin.register(SearchRecord)
class SearchRecordAdmin(admin.ModelAdmin):
    list_display = ('destination', 'travel_date', 'travel_date2', 'people')
    search_fields = ('destination',)
    list_filter = ('travel_date', 'people', 'safety_filter')
    filter_horizontal = ('safety_filter',)

@admin.register(SortOption)
class SortOptionAdmin(admin.ModelAdmin):
    list_display = ('sort_type',)
    ordering = ('sort_type',)
    list_filter = ('sort_type',)
    search_fields = ('sort_type',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at', 'image') 
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')  
    search_fields = ('post__title', 'author__username') 