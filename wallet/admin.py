
from django.contrib import admin

from .models import Customer, Wallet, Transaction, Account, Card, ThirdParty, Notification, Recipient, Loan, Reward, Currency


class CustomerAdmin(admin.ModelAdmin):
    list_display= ('first_name','last_name','age','email',)
    search_fields=('first_name','last_name',)
admin.site.register(Customer,CustomerAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display= ('account_number','account_type','account_balance','account_name')
    search_fields=('account_number','account_type','account_balance','account_name',)
admin.site.register(Account,AccountAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display= ('transaction_name','transaction_type','destination_account','transaction_amount',)
    search_fields=('transaction_name','transaction_amount','destination_account',)
admin.site.register(Transaction,TransactionAdmin)


class CardAdmin(admin.ModelAdmin):
     list_display= ('card_number','card_name','date_issued','card_type','expiry_date',)
     search_fields=('card_number','card_name','date_issued','card_type',)
admin.site.register(Card,CardAdmin)  


class ThirdPartyAdmin(admin.ModelAdmin):
    list_display= ('name','account','type','amount',)
    search_fields=('name','account',)
admin.site.register(ThirdParty,ThirdPartyAdmin)

                  
class NotificationAdmin(admin.ModelAdmin):
    list_display= ('message','title','recipient','status',)
    search_fields=('message','recipient',)
admin.site.register(Notification,NotificationAdmin)    
        
class RecipientAdmin(admin.ModelAdmin):
    list_display= ('receipt','date_time','bill_number','amount','receipt_file',)
    search_fields=('receipt','date_time','bill_number','amount',)


class LoanAdmin(admin.ModelAdmin):
    list_display= ('amount','wallet','loan_balance',)
    search_fields=('loan_balance','amount','wallet',)
admin.site.register(Loan,LoanAdmin)


class RewardAdmin(admin.ModelAdmin):
    list_display= ('name','message','customer_id','date_time',)
    search_fields=('name','message','date_time',)    
admin.site.register(Reward,RewardAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display= ('customer','balance','amount','time')
    search_fields=('customer','balance',)
admin.site.register(Wallet,WalletAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display= ('country','symbol','amount')
    search_fields= ('country','symbol','amount')
admin.site.register(Currency,CurrencyAdmin)
