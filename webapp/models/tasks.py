from django.db import models
from django.utils import timezone


class Task(models.Model):

    title = models.CharField(verbose_name='Title', max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name='Description', max_length=3000, null=False, blank=False)
    is_deleted = models.BooleanField(verbose_name='Deleted', null=False, default=False)
    created_at = models.DateTimeField(verbose_name='Date created', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Date updated', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Date deleted', null=True, default=None)
    types = models.ManyToManyField(to='webapp.Type', verbose_name='Type',
                                   related_name='types', blank=True)
    statuses = models.ManyToManyField(to='webapp.Status', verbose_name='Status',
                                      related_name='statuses', blank=True)

    def __str__(self):
        return f'{self.title} - {self.description}'


    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()
