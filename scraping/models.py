from django.db import models

from scraping.utils import from_cyrillic_to_eng


class City(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Назва населеного пункту',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Назва населеного пункту'
        verbose_name_plural = 'Назва населеного пункту'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(self.name)
        super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Мова програмування',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Мови програмування'
        verbose_name_plural = 'Мови програмування'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(self.name)
        super().save(*args, **kwargs)


class Vakancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Назва вакансії')
    company = models.CharField(max_length=250, verbose_name='Компанія')
    description = models.TextField(verbose_name='Опис вакансії')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Місто')
    language = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name='Язик програмування')
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансія'
        verbose_name_plural = 'Вакансії'

    def __str__(self):
        return self.title
