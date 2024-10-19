from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

# Create your views here.
@api_view(['GET'])
def get_data(request):
    books = Book.objects.all()
    ser = BookSerializer(books, many=True)
    return Response(ser.data)


@api_view(['POST'])
def create_book(request):
    title = request.POST.get('title')
    info = request.POST.get('info')
    pages = request.POST.get('pages')
    author = request.POST.get('author')
    Book.objects.create(title=title, info=info, pages=pages, author=author)
    return Response({"message": "Muvaffaqiyatli"})

@api_view(['PUT'])
def update_book(request, pk):
    title = request.POST.get('title')
    info = request.POST.get('info')
    pages = request.POST.get('pages')
    author = request.POST.get('author')
    b = Book.objects.get(id=pk)
    b.title = title
    b.info = info
    b.pages = pages
    b.author = author
    b.save()
    ser = BookSerializer(b)
    return Response(ser.data)

@api_view(['GET'])
def get_book(request, pk):
    b = Book.objects.get(id=pk)
    ser = BookSerializer(b)
    return Response(ser.data)

@api_view(['GET'])
def search_book(request):
    title = request.GET.get('q')
    b = Book.objects.filter(title__icontains=title)
    ser = BookSerializer(b, many=True)
    return Response(ser.data)