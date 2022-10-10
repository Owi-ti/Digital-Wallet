from rest_framework import serializers
from wallet.models import Customer, Wallet, Account, Card, Transaction, Loan, Recipient, Notification


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Customer
        fields= ("first_name","email","age","address")

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ("balance", "customer", "status", "amount", "time", "currency")

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("account_number", "account_type","account_name", "account_balance","wallet")        

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ("card_number", "card_name","date_issued", "card_type","expiry_date","security_code")        

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("transaction_ref", "wallet","transaction_amount", "transaction_name","transaction_type","transaction_charge","date_and_time","original_account","destination_account","receipt")        


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ("loan_type", "amount","transaction", "interest_rate","wallet","loan_balance","loan_term","guarantor","status","payment_due_date") 


class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipient
        fields = ("receipt", "date_time","bill_number", "amount","receipt_file") 

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ("message", "title","recipient", "date_time","status")         