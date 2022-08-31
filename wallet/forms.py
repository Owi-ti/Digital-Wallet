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


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model= Customer
        fields= "__all__"

class WalletRegistrationForm(forms.ModelForm):
    class Meta:
        model= Wallet
        fields= "__all__"

class AccountRegistrationForm(forms.ModelForm):
    class Meta:
        model= Account
        fields= "__all__"

class TransactionRegistrationForm(forms.ModelForm):
    class Meta:
        model= Transaction
        fields= "__all__"

class CardRegistrationForm(forms.ModelForm):
    class Meta:
        model= Card
        fields= "__all__"

class ThirdPartyRegistrationForm(forms.ModelForm):
    class Meta:
        model= ThirdParty
        fields= "__all__"

class NotificationRegistrationForm(forms.ModelForm):
    class Meta:
        model= Notification
        fields= "__all__"  

class RecipientRegistrationForm(forms.ModelForm):
    class Meta:
        model= Recipient
        fields= "__all__"  

class LoanRegistrationForm(forms.ModelForm):
    class Meta:
        model= Loan
        fields= "__all__"     

class RewardRegistrationForm(forms.ModelForm):
    class Meta:
        model= Reward
        fields= "__all__"             