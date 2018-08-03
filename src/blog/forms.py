from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    body = forms.CharField(required=False,
                                widget=forms.Textarea(attrs={
                                    "placeholder": 'Your article body',
                                    "class": "new-class-name two",
                                    "id": "my-id-for-Textarea",
                                    "rows": 20,
                                    "cols": 120,
                                }
    ))
    active = forms.BooleanField()
    class Meta:
        model = Article
        fields = [
            'title',
            'body',
            'active',
        ]
