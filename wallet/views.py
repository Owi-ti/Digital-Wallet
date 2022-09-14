
from django.shortcuts import render
from wallet.models import Customer
from .forms import CustomerRegistrationForm
from .forms import WalletRegistrationForm
from .forms import AccountRegistrationForm
from .forms import TransactionRegistrationForm
from .forms import CardRegistrationForm
from .forms import ThirdPartyRegistrationForm
from .forms import NotificationRegistrationForm 
from .forms import RecipientRegistrationForm
from .forms import LoanRegistrationForm 
from .forms import RewardRegistrationForm
from .forms import CurrencyRegistarationForm
from .models import Currency, Customer, Loan, Notification, Recipient, Reward, ThirdParty
from . models import Account
from . models import Transaction
from .models import Wallet
from .models import Card


# from . import forms
#
# Create your views here.
def register_customer(request):
    if request.method =="POST":     
       form = CustomerRegistrationForm(request.POST)
       if form.is_valid():
        form.save()
    else:
        form= CustomerRegistrationForm()  
    return render(request,"wallet/register_customer.html",
    {"form":form})

def list_customers(request):
    customers=Customer.objects.all()
    return render(request, "wallet/customers_list.html",
    {"customers":customers})



def register_wallet(request):
    if request.method =="POST":     
       form = WalletRegistrationForm(request.POST)
       if form.is_valid():
        form.save()
    else:
        form= WalletRegistrationForm()  
    return render(request,"wallet/register_wallet.html",
    {"form":form}) 

def list_wallets(request):
    wallets=Wallet.objects.all()
    return render(request, "wallet/wallets_list.html",
    {"wallets":wallets})
      



def register_account(request):
     if request.method =="POST":   
       form = AccountRegistrationForm(request.POST)
       if form.is_valid():
        form.save()
     else:
        form= AccountRegistrationForm()  
     return render(request,"wallet/register_account.html",
        {"form":form})
         
def list_accounts(request):
    accounts= Account.objects.all()
    return render(request, "wallet/accounts_list.html",
    {"accounts":accounts})



def register_transaction(request):
    if request.method =="POST":  
        form = TransactionRegistrationForm(request.POST)
        if form.is_valid():
         form.save()
    else:
         form = TransactionRegistrationForm()
    return render(request,"wallet/register_transaction.html",
         {"form":form})

def list_transactions(request):
    transactions=Transaction.objects.all()
    return render(request, "wallet/transactions_list.html",
    {"transactions":transactions})
      



def register_card(request):
    if request.method =="POST": 
        form = CardRegistrationForm(request.POST)
        if form.is_valid():
          form.save()
    else:
        form= CardRegistrationForm()  
    return render(request,"wallet/register_card.html",
        {"form":form})
    
def   list_cards(request):
      cards=Card.objects.all()
      return render(request, "wallet/cards_list.html",
       {"cards":cards})   



def register_thirdparty(request):
    if request.method =="POST":
     form = ThirdPartyRegistrationForm(request.POST)
     if form.is_valid():
        form.save

    else:
        form=ThirdPartyRegistrationForm()    
    return render(request,"wallet/register_thirdparty.html",
    {"form":form})   

def list_thirdparties(request):
    thirdparties=ThirdParty.objects.all()
    return render(request, "wallet/thirdparties_list.html",
    {"thirdparties":thirdparties})




def register_notification(request):
    if request.method =="POST": 
      form = NotificationRegistrationForm(request.POST)
      if form.is_valid():
         form.save()
    else:
         form= NotificationRegistrationForm()  
    return render(request,"wallet/register_natification.html",
         {"form":form})   

def list_notifications(request):
    notifications=Notification.objects.all()
    return render(request, "wallet/notifications_list.html",
    {"notifications":notifications})



def register_recipient(request):
    if request.method == "POST":
        form = RecipientRegistrationForm(request.POST)
        if form.is_valid():
           form.save()
    else:
         form= RecipientRegistrationForm()  
    return render(request,"wallet/register_recipient.html",
    {"form":form})

def list_recipients(request):
    recipients=Recipient.objects.all()
    return render(request, "wallet/recipients_list.html",
    {"recipients":recipients})





def register_loan(request):
    if request.method =="POST":     
       form = LoanRegistrationForm(request.POST)
       if form.is_valid():
        form.save()
    else:
        form= LoanRegistrationForm()  
    return render(request,"wallet/register_loan.html",
    {"form":form})

def list_loans(request):
    loans= Loan.objects.all()
    return render(request, "wallet/loans_list.html",
    {"loans":loans})


def register_reward(request):
    if request.method =="POST":     
       form = RewardRegistrationForm(request.POST)
       if form.is_valid():
        form.save()
    else:
        form= RewardRegistrationForm()  
    return render(request,"wallet/register_reward.html",
    {"form":form})

def list_rewards(request):
    rewards= Reward.objects.all()
    return render(request, "wallet/rewards_list.html",
    {"rewards":rewards})  


def register_currency(request):
    if request.method =="POST":     
       form = CurrencyRegistarationForm(request.POST)
       if form.is_valid():
        form.save()
    else:
        form= CurrencyRegistarationForm()  
    return render(request,"wallet/register_currency.html",
    {"form":form})

def list_currencies(request):
    currencies= Currency.objects.all()
    return render(request, "wallet/currencies_list.html",
    {"currencies":currencies})

    
                     

# def list_customers(request):
#     customer= Customer.objects.all()
#     return render(request,"wallet/customer_list.html",  {"customer":customer})


