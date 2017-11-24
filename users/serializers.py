from rest_framework.authtoken.models import Token
from rest_framework import serializers
from .models import (
    CustomerUser,
    CreditCard,
    ShippingAddress
    )


class CustomerUserSerializerDefault(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = '__all__'

        extra_kwargs = {
            'password': {'write_only': True},
        }


class CustomerUserSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ('pk', 'username', 'first_name', 'last_name',
                  'email', 'password', 'cellphone', 'phone_number')

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = CustomerUser(**validated_data)
        password = validated_data['password']
        user.set_password(password)
        user.save()
        token = Token.objects.create(user=user)
        token.save()
        return user


class CreditCardSerializerDefault(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = '__all__'


class CreditCardSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ('pk', 'owner_name', 'card_number', 'security_code',
                  'expire_date', 'provider', 'user')

    def create(self, validated_data):
        credit_card = CreditCard(**validated_data)
        credit_card.save()
        token = Token.objects.create(credit_card=credit_card)
        token.save()
        return credit_card


class ShippingAddressSerializerDefault(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'
