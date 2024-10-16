from django.db import models


class Blog(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="заголовок",
    )
    slug = models.CharField(
        max_length=100,
        verbose_name="slug",
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name="содержимое",
    )
    photo = models.ImageField(
        upload_to="blog/photo",
        blank=True,
        null=True,
        verbose_name="изображение",
    )
    created_at = models.DateField(
        auto_now=True,
        blank=True,
        null=True,
    )
    views_counter = models.IntegerField(
        verbose_name="количество просмотров",
        default=0,
    )
    is_published = models.BooleanField(
        verbose_name="признак публикации",
        default=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"