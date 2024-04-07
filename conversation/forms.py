from django import forms

from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content', )
        widgets = {
            'content': forms.Textarea(attrs={
                'style': 'width: 100%; height: 200px'
            })
        }