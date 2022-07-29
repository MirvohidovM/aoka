from rest_framework import serializers

from .models import Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['position', 'phone', 'email', 'address', 'transport', 'reception_days']