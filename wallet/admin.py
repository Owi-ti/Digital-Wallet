
from django.contrib import admin

# Register your models here.
from .models import Customer, Wallet, Transaction, Account, Card, ThirdParty, Notification, Recipient, Loan, Reward


class CustomerAdmin(admin.ModelAdmin):
    list_display= ('first_name','last_name','age','email',)
    search_fields=('first_name','last_name',)

class WalletAdmin(admin.ModelAdmin):
    list_display= ('customer','balance','amount',)
    search_fields=('customer','balance',)

# class AccountAdmin(admin.ModelAdmin):
#     list_display= ('acount_name','wallet','account_balance',)
#     search_fields=('account_name','wallet',)

# class TransactionAdmin(admin.ModelAdmin):
#     list_display= ('transaction_name ','transaction_type','destination_account','transaction_amount',)
#     search_fields=('transaction_name ','transaction_amount','destination_account')

# class CardAdmin(admin.ModelAdmin):
#     list_display= ('card_name','card_type','amount','wallet',)
#     search_fields=('card_name','amount',)
        
class ThirdPartyAdmin(admin.ModelAdmin):
    list_display= ('name','account','type','amount',)
    search_fields=('name','account',)
                  
# class NotificationAdmin(admin.ModelAdmin):
#     list_display= (' message ','title','recipient','status',)
#     search_fields=('message','recipient',)
        
# class RecipientAdmin(admin.ModelAdmin):
#     list_display= ('amount','recipient','bill_number','date_time',)
#     search_fields=('amount','recipient',)

class LoanAdmin(admin.ModelAdmin):
    list_display= ('amount','wallet','loan_balance',)
    search_fields=('loan_balance','amount',)

class RewardAdmin(admin.ModelAdmin):
    list_display= ('name','message','customer_id ','date_time',)
    search_fields=('name','message', 'date_time',)    



admin.site.register(Customer,CustomerAdmin)
admin.site.register(Wallet,WalletAdmin)
admin.site.register(Transaction)
admin.site.register(Account)
admin.site.register(Card)
admin.site.register(ThirdParty,ThirdPartyAdmin)
admin.site.register(Notification)
admin.site.register(Recipient)
admin.site.register(Loan,LoanAdmin)
admin.site.register(Reward)










