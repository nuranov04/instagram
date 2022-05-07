from django.db import models


class Tag(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Тег',
        blank=True, null=True
    )

    def __str__(self):
        return f"{self.title}"
