from django.db import models



class CmsSlider(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.CharField(max_length=200, verbose_name='Текст')
    img = models.ImageField(upload_to='slider_img/')
    css = models.CharField(max_length=200, null=True, default='-', verbose_name='CSS класс')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'