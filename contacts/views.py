from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ContactSerializer
from .models import Contact
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ContactList(ListCreateAPIView):

    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)

    def perfom_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)

class ContactDetail(RetrieveUpdateDestroyAPIView):
    
        serializer_class = ContactSerializer
        permission_classes = (IsAuthenticated,)
        lookup_field = 'id'
    
        def get_queryset(self):
            return Contact.objects.filter(owner=self.request.user)