from django import forms
from .models import Comment
from django.forms import ValidationError

class CommentForm(forms.ModelForm):
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput)

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise ValidationError("A Bot has entered page, We have had a problem houston")
        return botcatcher
    class Meta:
        model = Comment
        fields = ('post','author','text','created_date')