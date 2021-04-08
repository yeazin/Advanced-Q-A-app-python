from django.db import models

# Create your models here.

class ToDo(models.Model):
    list_name   = models.CharField(max_length=300, blank=False, null=True, verbose_name='List Name')
    finish_yet  = models.BooleanField(default=False)

    def __str__(self):
        return self.list_name

    class Meta:
        verbose_name = " To Do List"
        verbose_name_plural = 'To Do List'
    