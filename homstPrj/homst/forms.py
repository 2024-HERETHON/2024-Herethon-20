from django import forms
from .models import SearchRecord, SafetyFilter, Post, Comment, Accommodation

class SearchRecordForm(forms.ModelForm):
    safety_filter = forms.ModelMultipleChoiceField(
        queryset=SafetyFilter.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="안심필터"
    )

    class Meta:
        model = SearchRecord
        fields = ['destination', 'travel_date', 'travel_date2', 'people', 'safety_filter']
        widgets = {
            'destination': forms.TextInput(attrs={'placeholder': '여행지를 입력하세요'}),
            'travel_date': forms.DateInput(attrs={'type': 'date', 'placeholder': '여행 시작일'}),
            'travel_date2': forms.DateInput(attrs={'type': 'date', 'placeholder': '여행 종료일'}),
            'people': forms.NumberInput(attrs={'min': 1, 'placeholder': '인원 수'}),
        }
        labels = {
            'destination': '여행지',
            'travel_date': '여행 시작일',
            'travel_date2' : '여행 종료일',
            'people': '인원수',
            'safety_filter': '안심필터',
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '제목을 입력하세요'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '내용을 입력하세요'}),
            'category': forms.Select(choices=Post.CATEGORY_CHOICES),
            'image': forms.FileInput(attrs={'class':'form-control-file'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': '댓글을 입력하세요.'}),
        }

class AccommodationForm(forms.ModelForm):
    class Meta:
        model = Accommodation
        fields = ['name', 'location', 'review_score', 'price', 'safety_filters', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '숙소 이름'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '숙소 위치'}),
            'review_score': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '별점'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '가격'}),
            'safety_filters': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        }

