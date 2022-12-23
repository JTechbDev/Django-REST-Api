from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from book_api.models import Book
from book_api.serializer import BookSerializer
from rest_framework import status

# Create your views here.
@api_view(['Get'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
#    http://127.0.0.1:8000/books/list
   
@api_view(['POST'])
def book_create(request): 
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
      

# http://127.0.0.1:8000/books/

@api_view(['GET', 'PUT', 'DELETE'])
def book(request, pk):
    try: 
        book = Book.objects.get(pk=pk)
    except:
        return Response({
            'error': 'Book does not exist'
        }, status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET':
        
        serializer = BookSerializer(book)
        return Response(serializer.data)


    if request.method == "PUT":
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

    
    if request.method == "DELETE":
        book.delete()
        return Response(status.HTTP_204_NO_CONTENT)



        