from django import forms
from apps.posts.models import Post, PostImage


class PostForm(forms.ModelForm):
    tag = forms.CharField(max_length=255, required=False)

    class Meta:
        model = Post
        fields = ['description', 'tag']


class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image', ]
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
