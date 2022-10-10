from django.shortcuts import render
from rest_framework import viewsets
from wallet.models import Customer, Wallet, Account, Card, Transaction, Loan, Recipient,Notification
from .serializers import CustomerSerializer, WalletSerializer, AccountSerializer, CardSerializer, TransactionSerializer, LoanSerializer, RecipientSerializer, NotificationSerializer
# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset= Customer.objects.all()
    serializer_class = CustomerSerializer

class WalletViewSet(viewsets.ModelViewSet):
    queryset =  Wallet.objects.all()
    serializer_class = WalletSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset= Account.objects.all()
    serializer_class = AccountSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset= Card.objects.all()
    serializer_class = CardSerializer    

class TransactionViewSet(viewsets.ModelViewSet):
    queryset= Transaction.objects.all()
    serializer_class = TransactionSerializer    


class LoanViewSet(viewsets.ModelViewSet):
    queryset= Loan.objects.all()
    serializer_class = LoanSerializer    


class RecipientViewSet(viewsets.ModelViewSet):
    queryset= Recipient.objects.all()
    serializer_class = RecipientSerializer      


class NotificationViewSet(viewsets.ModelViewSet):
    queryset= Notification.objects.all()
    serializer_class = NotificationSerializer   