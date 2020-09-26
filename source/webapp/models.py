from django.contrib.auth import get_user_model
from django.db import models

DEFAULT_CATEGORY = 'other'
CATEGORY_CHOICES = {
    (DEFAULT_CATEGORY, 'Разное'),
    ('food', "Еда"),
    ('toys', 'Игрушки'),
    ('tech', 'Бытовая техника'),
    ('tools', 'Инструменты')
}

RATING_CHOICES = {
    ('1', 'Очень плохой товар'),
    ('2', 'Плохой товар'),
    ('3', 'Хороший товар'),
    ('4', 'Очень хороший товар'),
    ('5', 'Отличный товар'),
}


class Product(models.Model):
    name = models.TextField(max_length=40, null=False, blank=False, verbose_name='Название')
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, default=DEFAULT_CATEGORY, verbose_name='Категория')
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(null=True, blank=True, upload_to='product_pics', verbose_name='Картинка')

    def __str__(self):
        return "{}. {}".format(self.pk, self.name)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Review(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1,
                               related_name='reviews', verbose_name='Автор')
    product = models.ForeignKey('webapp.Product', related_name='reviews',
                                on_delete=models.CASCADE, verbose_name='Товар')
    review = models.TextField(max_length=4000, null=False, blank=False, verbose_name='Отзыв')
    rate = models.CharField(max_length=2, choices=RATING_CHOICES, null=False, blank=False, verbose_name='Оценка')

    def __str__(self):
        return self.review[:20]

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'