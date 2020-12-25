from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta():
        model = Post   #Connects The Post Form To the Model Post under the models.py file
        fields = ('author','title','text')

    #FORM WIDGETS are used to connect Form Fields to different CSS stylings under the css file of the project
    widgets = {
        'title':forms.TextInput(attrs={'class':'textinputclass'}),  #User created CSS Class
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
    }
class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment  #Connects the Comment Form to the Comment model
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text' :forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
        }
