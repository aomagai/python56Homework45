from django.db import models

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]


class ToDo(models.Model):
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='new', null=False, blank=False, verbose_name='Статус')
    date = models.DateField(null=True, blank=True, verbose_name='Дата')

    def __str__(self):
        return "{0}. {2} ({1})".format(self.pk, self.status, self.description)