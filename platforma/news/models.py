from django.db import models


class Items(models.Model):
    """Страница поста как на сайте"""
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to="images/categories/%Y/%m/%d/")
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        """Вывод заголовка текущей записи"""
        return self.title
