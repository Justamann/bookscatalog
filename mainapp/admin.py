from django.apps import AppConfig
from django.contrib import admin
from .models import Author, Tags, Book

# admin.site.register(Author)
admin.site.register(Tags)


class MainappConfig(AppConfig):
    name = 'mainapp'


class BookInline(admin.TabularInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')
    fields = ['name', 'surname', 'patronymic', ('email', 'phone')]
    inlines = [BookInline]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'date')

# @admin.register(BookInstance)
# class BookInstanceAdmin(admin.ModelAdmin):
#     list_filter = ('status', 'due_back')
