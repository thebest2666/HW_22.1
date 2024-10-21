from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Категория продукта",
        help_text="Введите категорию продукта",
    )
    description = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="описание продукта",
        help_text="Введите описание продукта",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    description = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="описание продукта",
        help_text="Введите описание продукта",
    )
    photo = models.ImageField(
        upload_to="products/photo",
        blank=True,
        null=True,
        verbose_name="изображение продукта",
        help_text="Вставьте изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="категория продукта",
        help_text="Введите категорию продукта",
        related_name="products",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена за покупку",
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания продукта",
        help_text="Введите дату создания продукта",
    )
    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения",
        help_text="Введите дату последнего изменения",
    )
    views_counter = models.IntegerField(
        verbose_name="количество просмотров",
        default=0,
    )
    is_published = models.BooleanField(
        verbose_name="признак публикации",
        default=True,
    )
    creator = models.ForeignKey(
        User,
        verbose_name="Создатель",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "created_at"]
        permissions = [
            ('set_published', 'Can publish product'),
            ('edit_description', 'Can edit description'),
            ('change_category_product', 'Can change category of product')
        ]

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_query_name="version",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Версия",
    )
    version_number = models.PositiveIntegerField(
        verbose_name="Номер версии", help_text="Введите номер версии", default=0
    )
    version_name = models.CharField(
        max_length=50,
        verbose_name="Название версии",
        help_text="Введите название версии",
    )
    current_version_indicator = models.BooleanField(
        verbose_name="признак публикации",
        default=True,
    )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["version_name", "version_number"]

    def __str__(self):
        return f"Версия №{self.version_number}: {self.version_name}"
