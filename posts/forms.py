"""forms.py"""
from django import forms

from posts.models import POST_TYPE_CHOICES


class PostForms(forms.Form):
    title = forms.CharField(

        label='title',
        max_length=100,
        min_length=8,
    )
    description = forms.CharField(
        widget=forms.Textarea()
    )
    stars = forms.IntegerField(max_value=5, min_value=0)
    type = forms.ChoiceField(choices=POST_TYPE_CHOICES)


class CommentForms(forms.Form):
    author = forms.CharField(label='Автор', max_length=100, min_length=2)
    text = forms.CharField(
        widget=forms.Textarea(),
        label='ты знаешь что сюда писать'
    )