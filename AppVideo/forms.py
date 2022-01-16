from django import forms
from AppVideo.models import comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = comments
        fields = ('comment',)
