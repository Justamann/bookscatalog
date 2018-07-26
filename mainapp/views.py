from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from mainapp.models import Book, Author, Tags
from mainapp.models import NameForm


def view_index(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.count()  # The 'all()' is implied by default.
    word_in_books = Book.objects.filter(short_desc__icontains='роман')
    word_in_books = ', '.join([book.name for book in word_in_books])

    # def show_all_books(request):
    #     name_book = Book.name
    #     view_books = Book.objects.all()
    #     content = {'name_book': name_book, 'view_books': view_books}
    #     return render(request, 'mainapp/index.html', content)

    # Render the HTML template index.html with the data in the context variable
    return render(
        request, 'mainapp/index.html',
        context={'num_books': num_books,
                 'num_authors': num_authors,
                 'word_in_books': word_in_books,
                 },
    )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    context_object_name = 'book_list'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context


class BookDetailView(generic.DetailView):
    # context_object_name = 'book'
    template_name = 'mainapp/book.html'
    model = Book


class AuthorsListView(generic.ListView):
    model = Author
    paginate_by = 10
    context_object_name = 'list_authors'

    def get_context_data(self, **kwargs):
        context = super(AuthorsListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context


class AuthorDetailView(generic.DetailView):
    template_name = 'mainapp/author.html'
    model = Author


class TagsListView(generic.ListView):
    model = Tags
    context_object_name = 'listtags'
    template_name = 'mainapp/index.html'

    # def view_all_tags(self):


class RegistrUserView(generic.DetailView):
    template_name = 'mainapp/registration.html'


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/registration/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'registration.html', {'form': form})
