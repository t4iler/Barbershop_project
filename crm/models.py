from django.db import models


class Order(models.Model):
    ordered_at = models.DateTimeField(auto_now_add=True)
    order_name = models.CharField(max_length=100, verbose_name='Name')
    order_phone = models.CharField(max_length=50, verbose_name='Phone')
    order_status = models.ForeignKey('StatusCrm', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    

class StatusCrm(models.Model):
    Status_name = models.CharField(max_length=200, verbose_name='Название статуса')

    def __str__(self):
        return self.Status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class CommentCrm(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
    comment_text = models.TextField(verbose_name='Текст комментария')
    commented_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата комментария')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'