from django.urls import path 
from .views import register_customer
from .views import register_wallet
from .views import register_account
from .views import register_transaction
from .views import register_card
from .views import register_thirdparty
from .views import register_notification
from .views import register_recipient
from .views import register_loan
from .views import register_reward
from .views import register_currency



urlpatterns =[
    path("register/",register_customer,name="registration"),
    path("wallet/",register_wallet,name="registration"),
    path("account/",register_account,name="registration"),
    path("transaction/",register_transaction,name="registration"),
    path("card/",register_card,name="registration"),
    path("thirdparty/",register_thirdparty,name="registration"),
    path("notification/",register_notification,name="registration"),
    path("recipient/",register_recipient,name="registration"),
    path("loan/",register_loan,name="registration"),
    path("reward/",register_reward,name="registration"),
    path("currency/",register_currency,name="registration"),
]
