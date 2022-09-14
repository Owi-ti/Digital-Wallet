
from django.db import models
# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    phone_number=models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    age = models.PositiveSmallIntegerField()
    password= models.CharField(max_length=20,null=True)
    id_number=models.IntegerField(null=True)
    nationality=models.CharField(max_length=30,null=True)
    # def __str__(self):
    #     return str(self.form)


class Wallet(models.Model):
    balance = models.IntegerField()
    customer = models.ForeignKey(Customer,on_delete= models.CASCADE,related_name='Wallet_customer')
    amount = models.IntegerField()
    time = models.DateTimeField()
    status = models.CharField(max_length=20,null=True)
    currency= models.ForeignKey('Currency', on_delete= models.CASCADE,related_name='wallet_currency',null=True)
    pin= models.IntegerField(null=True)
    


class Account(models.Model):
    account_number = models.IntegerField()
    account_type = models.CharField(max_length=20)
    account_balance = models.IntegerField()
    account_name = models.CharField(max_length=20)
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='Account_wallet')


class Transaction(models.Model):
    transaction_ref = models.CharField(max_length=20)
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='Transaction_wallet')
    transaction_amount = models.IntegerField()
    transaction_name = models.CharField(max_length=20)
    transaction_type = models.CharField(max_length=20)
    transaction_charge = models.IntegerField()
    date_and_time = models.DateTimeField()
    original_account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name='Transaction_original_account',null="true")
    destination_account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='Transaction_destination_account')
    receipt = models.CharField(max_length=20)





class Card(models.Model):
    card_number = models.IntegerField()
    card_name = models.CharField(max_length=20)
    date_issued = models.DateTimeField()
    card_type = models.CharField(max_length=20)
    expiry_date = models.IntegerField()
    security_code = models.IntegerField()
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='Card_wallet')
    account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='Card_account')
    issuer = models.CharField(max_length=20)


class ThirdParty(models.Model):
    name = models.CharField(max_length=20)
    account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='ThirdParty_account')
    location = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    amount = models.IntegerField()


class Notification(models.Model):
    message = models.CharField(max_length=100)
    title = models.CharField(max_length=20)
    recipient = models.OneToOneField(Customer,on_delete=models.CASCADE,related_name='Notification_recipient')
    date_time = models.DateTimeField()
    status = models.CharField(max_length=20)


class Recipient(models.Model):
    receipt = models.CharField(max_length=20)
    date_time = models.DateTimeField()
    bill_number = models.CharField(max_length=20)
    amount = models.IntegerField()
    receipt_file = models.FileField()


class Loan(models.Model):
    loan_type = models.CharField(max_length=20)
    amount = models.IntegerField()
    transaction = models.ForeignKey(Transaction,on_delete=models.CASCADE,related_name='Loan_transaction')
    interest_rate = models.IntegerField()
    wallet = models.IntegerField()
    loan_balance = models.IntegerField()
    loan_term = models.CharField(max_length=20)
    guarantor = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    payment_due_date = models.IntegerField()


class Reward(models.Model):
    name = models.CharField(max_length=20)
    customer_id = models.IntegerField()
    gender = models.CharField(max_length=20)
    message = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    points = models.IntegerField()


class Currency(models.Model):
    country = models.CharField(max_length=30,null=True)
    symbol = models.CharField(max_length=5,null=True)
    amount = models.IntegerField()



  

































    














    
















     







 




    
