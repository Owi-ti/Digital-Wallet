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
from .import views



urlpatterns =[
    path("register/",register_customer,name="registration"),
    path("customers/", views.list_customers, name="customers_list"),

    path("wallet/",register_wallet,name="registration"),
    path("wallets/", views.list_wallets,name="wallets_list"),

    path("account/",register_account,name="registration"),
    path("accounts/",views.list_accounts,name="accounts_list"),

    path("transaction/",register_transaction,name="registration"),
    path("transactions/", views.list_transactions,name="transactions_list"),

    path("card/",register_card,name="registration"),
    path("cards/", views.list_cards,name="cards_list"),

    path("thirdparty/",register_thirdparty,name="registration"),
    path("thirdparties/", views.list_thirdparties,name="thirdparties_list"),

    path("notification/",register_notification,name="registration"),
    path("notifications/", views.list_notifications,name="notifications_list"),

    path("recipient/",register_recipient,name="registration"),
    path("recipients/", views.list_recipients,name="recipients_list"),

    path("loan/",register_loan,name="registration"),
    path("loans/", views.list_loans,name="loans_list"),

    path("reward/",register_reward,name="registration"),
    path("rewards/", views.list_rewards,name="rewards_list"),

    path("currency/",register_currency,name="registration"),
    path("currencies/", views.list_currencies,name="currencies_list"),

]
