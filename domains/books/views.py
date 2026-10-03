from django.shortcuts import render

#để cho biết Book lấy từ models nào
from .models import Book,Author

def book_list(request):
    #lấy tấc cả cac sách lưu vào biến books
    books=Book.objects.all()

    #gửi sang trang HTML
    return render(
        request,
        'books/book_list.html',
        {'books':books}
    )
def book_detail(request,book_id):
    book=Book.objects.get(id=book_id)

    return render(
        request,
        'books/book_detail.html',
        {'book':book}
    )
def author_list(request):
    authors=Author.objects.all()

    return render(
        request,
        'books/author_list.html',
        {'authors':authors}
    )
def author_detail(request,author_id):
    author=Author.objects.get(id=author_id)

    return render(
        request,
        'books/author_detail.html',
        {'author':author}
    )