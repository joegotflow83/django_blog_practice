from django import forms
from bloggy.models import Posts


class PostForm(forms.ModelForm):


	class Meta:


		model = Posts
		fields = ['title', 'post']