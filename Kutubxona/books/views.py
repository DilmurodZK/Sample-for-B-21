from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

# Create your views here.
@api_view(['GET'])
def get_data(request):
    books = Book.objects.all()
    ser = BookSerializer(books, many=True)
    return Response(ser.data)