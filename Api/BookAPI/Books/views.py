from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
# from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


from .models import Book
from .serializers import BookSerializer


# Create your views here.

class WomenAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10


class BookAPIList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = WomenAPIListPagination
    permission_classes = (IsAuthenticated,)


class BookAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)


class BookAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)


class MyLogoutView(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request, format=None):
        request.user.auth_token.delete()

        return Response({"detail": "Logged out successfully."})
