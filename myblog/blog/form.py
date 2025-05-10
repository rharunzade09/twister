from django import forms
from .models import Comments

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'email', 'text_comments')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваше имя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш email'}),
            'text_comments': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите ваш комментарий...', 'rows': 5})
        }