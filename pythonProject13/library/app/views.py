from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Reader
from .forms import BookForm, ReaderForm
from django.contrib.auth.decorators import login_required, user_passes_test


def is_librarian(user):
    return user.groups.filter(name='Librarians').exists()


@login_required
@user_passes_test(is_librarian)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})


@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})


@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})


@login_required
@user_passes_test(is_librarian)
def reader_list(request):
    readers = Reader.objects.all()
    return render(request, 'readers/reader_list.html', {'readers': readers})


@login_required
def reader_create(request):
    # Аналогично созданию книги
    if request.method == 'POST':
        form = ReaderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reader_list')
    else:
        form = ReaderForm()
    return render(request, 'readers/reader_form.html', {'form': form})


@login_required
def reader_update(request, pk):
    # Аналогично редактированию книги
    reader = get_object_or_404(Reader, pk=pk)
    if request.method == 'POST':
        form = ReaderForm(request.POST, instance=reader)
        if form.is_valid():
            form.save()
            return redirect('reader_list')
    else:
        form = ReaderForm(instance=reader)
    return render(request, 'readers/reader_form.html', {'form': form})


@login_required
def reader_delete(request, pk):
    # Аналогично удалению книги
    reader = get_object_or_404(Reader, pk=pk)
    if request.method == 'POST':
        reader.delete()
        return redirect('reader_list')
    return render(request, 'readers/reader_confirm_delete.html', {'reader': reader})