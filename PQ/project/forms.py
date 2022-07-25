from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class ProjctForm(ModelForm):
	class Meta:
		model = projects
		fields = '__all__'

class BidForm(ModelForm):
	class Meta:
		model = bids
		fields = '__all__'


class bid_BOQ_fORM(ModelForm):
	class Meta:
		model = bid_BOQ
		fields = '__all__'


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
