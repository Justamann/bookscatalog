from django.db import models
from django.urls import reverse
from django import forms


class Author(models.Model):
    name = models.CharField(verbose_name='имя автора', max_length=60)
    surname = models.CharField(verbose_name='фамилия автора', max_length=60)
    patronymic = models.CharField(verbose_name='отчество автора', max_length=60, blank=True)
    email = models.EmailField(verbose_name='электронная почта автора', max_length=50, blank=True)
    phone = models.CharField(verbose_name='телефон автора', max_length=20, blank=True)

    class Meta:
        ordering = ["surname", "name"]

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('mainapp:author', args=[str(self.id)])

    def __str__(self):
        return '{0} {1}'.format(self.surname, self.name)


class Tags(models.Model):
    name = models.CharField(verbose_name='имя тега', max_length=200)
    description = models.TextField(verbose_name='описание тега', blank=True)
    active_flag = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name


GET_SHORT_LEN = 250


class Book(models.Model):
    name = models.CharField(verbose_name='имя книги', max_length=150)
    date = models.DateField('Дата публикации', auto_now=True)
    short_desc = models.TextField(verbose_name='краткое описание', max_length=3000, blank=True)
    preview = models.ImageField(verbose_name='обложка книги', blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tags, help_text='Укажите тег для этой книги')

    class Meta:
        ordering = ["name", "-date"]

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('mainapp:book', args=[str(self.id)])

    def get_short_text(self):
        if len(self.short_desc) > GET_SHORT_LEN:
            return self.short_desc[:GET_SHORT_LEN]
        else:
            return self.short_desc

    def __str__(self):
        return self.name


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

    def __str__(self):
        return self.your_name
