from django.contrib.auth.models import User, Group
from . models import Post, Category, Tag
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PostSerializer, CategorySerializer, TagSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def post_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        # print(serializer.data, "AAAAAAAAAAAAAAAAAAAAAAAAAA")
        print("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.author == None:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT'])
def category_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        post = Category.objects.all()
        serializer = CategorySerializer(post, many=True)
        # print(serializer.data, "AAAAAAAAAAAAAAAAAAAAAAAAAA")
        print("CCCCCCCCCCCCCCCCCCCCC")
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'PUT':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def tag_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        tag = Tag.objects.all()
        serializer = TagSerializer(tag, many=True)
        # print(serializer.data, "AAAAAAAAAAAAAAAAAAAAAAAAAA")
        print("TTTTTTTTTTTTTTTTTTTTTT")
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)