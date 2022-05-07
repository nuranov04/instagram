from django.db import models
from django.contrib.auth.models import User
from apps.posts.models import Post


class Comment(models.Model):
    text = models.TextField(
        verbose_name='Комментарий'
    )
    user = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        related_name='comment_post',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.post.id} -- {self.user.id}"



