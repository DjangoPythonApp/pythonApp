import os

from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Category
from .serializers import CategorySerializer
from django.db.models.query import QuerySet

# Create a view to handle data & image upload
# @api_view is a decorator. This decorator is used to define a function-based view.
# It has a List as parameter, where we are defining the allowed HTTP methods
@api_view(['POST'])
def api_add_category(request: Request):
    print(f"Request Context: {request}")
    print(f"Request Data: {request.data}")
    
    # CategorySerializer is a constructor.
    # Its takes two parameters:
    #       a. The data given by user as QueryDict
    #       b. context(REST API endpoint) where from the request is coming.
    serializer: CategorySerializer = CategorySerializer(data=request.data, context={'request': request})

    if serializer.is_valid():
        category = serializer.save()

        return Response(
            CategorySerializer(category).data, status=200
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['GET'])
def api_list_categories(request):
    
    categories: QuerySet = Category.objects.all()
    all_categories = CategorySerializer(categories, many=True, context={'request': request}).data

    if not all_categories:
        return Response({"message": "No category found."}, status=status.HTTP_404_NOT_FOUND)
    
    return Response({
        "message": "List of all categories",
        "categories": all_categories
    }, status=status.HTTP_200_OK)


@api_view(['PUT', 'PATCH'])
def api_update_category(request, pk):
    try:
        category_found = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({
                "message": "Category not found."
            },
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = CategorySerializer(instance=category_found, data=request.data, partial=request.method == 'PATCH')

    if serializer.is_valid():
        serializer.save()

        return Response({
                "message": "Category updated successfully!",
                "category": serializer.data
            },
            status=status.HTTP_200_OK
        )

    return Response({
            "message": "Category update failed!",
            "errors": serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['DELETE'])
def api_delete_category(request, pk):
    try:
        category_found = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({
                "message": "Category not found."
            },
            status=status.HTTP_404_NOT_FOUND
        )

    category_found.delete()

    return Response({
            "message": "Category deleted successfully!"
        },
        status=status.HTTP_200_OK
    )