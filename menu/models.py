from django.db import models
from django.urls import reverse


class BaseAbstractModel(models.Model):
    """
    Base abstract model.
    Provides visibility settings, ordering, and created/updated field.
    """
    is_visible = models.BooleanField(default=True, verbose_name='Visibility')
    date_created = models.DateTimeField(verbose_name='Created', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='Updated', auto_now=True)

    class Meta:
        abstract = True


class Menu(BaseAbstractModel):
    title = models.CharField(max_length=20, verbose_name='Title')
    named_url = models.CharField(
        verbose_name='Named URL', max_length=255,
    )

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menu'

    def __str__(self):
        return f'Title: {self.title}'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'named_url': self.named_url})


class MenuItem(BaseAbstractModel):
    menu = models.ForeignKey('Menu', related_name='menu_item',
                             verbose_name='menu', blank=True, null=True,
                             on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='child_field',
                               verbose_name='Parent',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Item title')
    named_url = models.CharField(max_length=255, verbose_name='Named URL', unique=True)

    class Meta:
        verbose_name = 'menu_item'
        verbose_name_plural = 'menu_items'
        ordering = ['id', ]
        unique_together = ('parent', 'named_url')

    def get_absolute_url(self):
        return reverse('detail', kwargs={'named_url': self.named_url})

    def __str__(self):
        return f"""Title:{self.title}"""
