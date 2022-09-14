from django import forms
from .models import Customer
from .models import Wallet
from .models import Account
from .models import Transaction
from .models import Card
from .models import ThirdParty
from .models import Notification
from .models import Recipient
from .models import Loan
from .models import Reward
from .models import Currency


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model= Customer
        fields= ('first_name','last_name','address','phone_number','email','gender','age','password','id_number','nationality')
        Widget={
            "first_name":forms.TextInput(attrs={'class':"form-control"}),
            "last_name":forms.TextInput(attrs={'class':"form-control"}),
            "address":forms.TextInput(attrs={'class':"form-control"}),
            "phone_number":forms.TextInput(attrs={'class':"form-control"}),
            "email":forms.TextInput(attrs={'class':"form-control"}),
            "gender":forms.TextInput(attrs={'class':"form-control"}),
            "age":forms.TextInput(attrs={'class':"form-control"}),
            "password":forms.TextInput(attrs={'class':"form-control"}),
            "id_number":forms.TextInput(attrs={'class':"form-control"}),
            "nationality":forms.TextInput(attrs={'class':"form-control"}),
        }

        
class WalletRegistrationForm(forms.ModelForm):
    class Meta:
        model= Wallet
        fields=('balance','customer','amount','time','status','currency','pin')
        Widget={
            "balance":forms.TextInput(attrs={'class':"form-control"}),
            "customer":forms.TextInput(attrs={'class':"form-control"}),
            "amount":forms.TextInput(attrs={'class':"form-control"}),
            "time":forms.TextInput(attrs={'class':"form-control"}),
            "status":forms.TextInput(attrs={'class':"form-control"}),
            "currency":forms.TextInput(attrs={'class':"form-control"}),
            "pin":forms.TextInput(attrs={'class':"form-control"}),
        }


class AccountRegistrationForm(forms.ModelForm):
    class Meta:
        model= Account
        fields=('account_number','account_type','account_balance','account_name','wallet',)
        Widget={
            "account_number":forms.TextInput(attrs={'class':"form-control"}),
            "account_type":forms.TextInput(attrs={'class':"form-control"}),
            "account_balance":forms.TextInput(attrs={'class':"form-control"}),
            "account_name":forms.TextInput(attrs={'class':"form-control"}),
            "wallet":forms.TextInput(attrs={'class':"form-control"}),
        
        }

class TransactionRegistrationForm(forms.ModelForm):
    class Meta:
        model= Transaction
        fields=('transaction_ref','wallet','transaction_amount','transaction_name','transaction_type', 'transaction_charge','date_and_time','original_account','destination_account','receipt')
        Widget={
            "transaction_refr":forms.TextInput(attrs={'class':"form-control"}),
            "wallet":forms.TextInput(attrs={'class':"form-control"}),
            "transaction_amount":forms.TextInput(attrs={'class':"form-control"}),
            "transaction_name":forms.TextInput(attrs={'class':"form-control"}),
            "transaction_type":forms.TextInput(attrs={'class':"form-control"}),
            "transaction_charge":forms.TextInput(attrs={'class':"form-control"}),
            "date_and_time":forms.TextInput(attrs={'class':"form-control"}),
            "original_account":forms.TextInput(attrs={'class':"form-control"}),
            "destination_account":forms.TextInput(attrs={'class':"form-control"}),
            "receipt":forms.TextInput(attrs={'class':"form-control"}),
        
        }

class CardRegistrationForm(forms.ModelForm):
    class Meta:
        model= Card
        fields=('card_number','card_name','date_issued','card_type','expiry_date','security_code','wallet','account','issuer')
        Widget={
            "card_number":forms.TextInput(attrs={'class':"form-control"}),
            "card_name":forms.TextInput(attrs={'class':"form-control"}),
            "date_issued":forms.TextInput(attrs={'class':"form-control"}),
            "card_type":forms.TextInput(attrs={'class':"form-control"}),
            "expiry_date":forms.TextInput(attrs={'class':"form-control"}),
            "security_code":forms.TextInput(attrs={'class':"form-control"}),
            "wallet":forms.TextInput(attrs={'class':"form-control"}),
            "account":forms.TextInput(attrs={'class':"form-control"}),
            "issuer":forms.TextInput(attrs={'class':"form-control"}),
        }

class ThirdPartyRegistrationForm(forms.ModelForm):
    class Meta:
        model= ThirdParty
        fields=('name','account','location','type','amount',)
        Widget={
            "name":forms.TextInput(attrs={'class':"form-control"}),
            "account":forms.TextInput(attrs={'class':"form-control"}),
            "location":forms.TextInput(attrs={'class':"form-control"}),
            "type":forms.TextInput(attrs={'class':"form-control"}),
            "amount":forms.TextInput(attrs={'class':"form-control"}),
           
           
        }

class NotificationRegistrationForm(forms.ModelForm):
    class Meta:
        model= Notification
        fields=('message','title','recipient','date_time','status',)
        Widget={
            "message":forms.TextInput(attrs={'class':"form-control"}),
            "title":forms.TextInput(attrs={'class':"form-control"}),
            "recipient":forms.TextInput(attrs={'class':"form-control"}),
            "date_time":forms.TextInput(attrs={'class':"form-control"}),
            "status":forms.TextInput(attrs={'class':"form-control"}),
        }




class RecipientRegistrationForm(forms.ModelForm):
    class Meta:
        model= Recipient
        fields=('receipt','date_time','bill_number','amount','receipt_file',)
        Widget={
            "receipt":forms.TextInput(attrs={'class':"form-control"}),
            "date_time":forms.TextInput(attrs={'class':"form-control"}),
            "bill_number":forms.TextInput(attrs={'class':"form-control"}),
            "amount":forms.TextInput(attrs={'class':"form-control"}),
            "receipt_file":forms.TextInput(attrs={'class':"form-control"}),
        }


class LoanRegistrationForm(forms.ModelForm):
    class Meta:
        model= Loan
        fields=('loan_type','amount','transaction','interest_rate','wallet','loan_balance','loan_term','guarantor','status','payment_due_date')
        Widget={
            "loan_type":forms.TextInput(attrs={'class':"form-control"}),
            "amount":forms.TextInput(attrs={'class':"form-control"}),
            "transaction":forms.TextInput(attrs={'class':"form-control"}),
            "wallet":forms.TextInput(attrs={'class':"form-control"}),
            "loan_balance":forms.TextInput(attrs={'class':"form-control"}),
            "loan_term":forms.TextInput(attrs={'class':"form-control"}),
            "guarantor":forms.TextInput(attrs={'class':"form-control"}),
            "status":forms.TextInput(attrs={'class':"form-control"}),
            "payment_due_date":forms.TextInput(attrs={'class':"form-control"}),
        }    


class RewardRegistrationForm(forms.ModelForm):
    class Meta:
        model= Reward
        fields=('name','customer_id','gender','message','date_time','points',)
        Widget={
            "name":forms.TextInput(attrs={'class':"form-control"}),
            "customer_id":forms.TextInput(attrs={'class':"form-control"}),
            "gender":forms.TextInput(attrs={'class':"form-control"}),
            "message":forms.TextInput(attrs={'class':"form-control"}),
            "date_time":forms.TextInput(attrs={'class':"form-control"}),
            "points":forms.TextInput(attrs={'class':"form-control"}),
        
        }      
class CurrencyRegistarationForm(forms.ModelForm):
     class Meta:
        model = Currency
        fields=('country','symbol','amount',)
        Widget={
            "country":forms.TextInput(attrs={'class':"form-control"}),
            "symbol":forms.TextInput(attrs={'class':"form-control"}),
            "amount":forms.TextInput(attrs={'class':"form-control"}),  
        }      