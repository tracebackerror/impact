from django import forms    
from .models import ContactModel, CommentModel, BlogModel

class ContactForm(forms.ModelForm):
    class Meta:
        model= ContactModel
        fields= ["your_name", "email", "phone", "subject", "comment"]
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model= CommentModel
        fields= ["id", "name", "email", "phone", "subject", "message", ]