from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of main objects
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # Count authors
    num_authors = Author.objects.count()

    # Count books containing a specific word (case insensitive)
    keyword = "potter"  # Change this keyword as needed
    num_books_with_keyword = Book.objects.filter(title__icontains=keyword).count()

    # Count genres containing a specific word (case insensitive)
    num_genres_with_keyword = Genre.objects.filter(name__icontains=keyword).count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits

    # Context to pass to the template
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_books_with_keyword': num_books_with_keyword,
        'num_genres_with_keyword': num_genres_with_keyword,
        'search_keyword': keyword,  # Pass keyword for display

        'num_visits': num_visits,

    }

    # Render the HTML template index.html with the context data
    return render(request, 'index.html', context=context)


from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10



class BookDetailView(generic.DetailView):
    model = Book


from .models import Author
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10  # Paginate the list to show 10 authors per page

class AuthorDetailView(generic.DetailView):
    model = Author