from datetime import date

from django import forms
from django.db import models

from .models import SearchRecord, SafetyFilter, Post

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

