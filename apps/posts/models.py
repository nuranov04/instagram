from django.db import models
from django.contrib.auth.models import User
from apps.tags.models import Tag


class Post(models.Model):
    owner = models.ForeignKey(
        User,
        related_name='posts',
        verbose_name='Автор',
        on_delete=models.CASCADE,
    )
    description = models.TextField(
        blank=True, null=True,
        verbose_name='Описание'
    )
    create_at = models.DateTimeField(
        auto_now_add=True
    )
    tag = models.ManyToManyField(
        Tag,
        verbose_name='Тег',
        related_name='tags'
    )

    def __str__(self):
        return f"{self.id}"

    class Meta:
        ordering = ('-id',)



class PostImage(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_image'
    )
    image = models.ImageField(
        upload_to='post',
        verbose_name='Картинки'
    )

    def __str__(self):
        return f"{self.post.id}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes_post')

