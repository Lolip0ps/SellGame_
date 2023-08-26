from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from drf.permissions import IsAdminOrReadOnly
from drf.serializers import NewsSerializer, CatalogSerializer
from news.models import News
from catalog.models import Product


# from women.permissions import IsAdminOrReadOnly


class NewsAPIList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class NewsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication, )


class NewsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CatalogAPIList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CatalogSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CatalogAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = CatalogSerializer
    permission_classes = (IsAuthenticated,)


class CatalogAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = CatalogSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
