from rest_framework.serializers import ModelSerializer
from contacts.models import Contact


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ('country_code', 'firstname', 'lastname',
                  'phone_number', 'contact_picture', 'is_favorite')
