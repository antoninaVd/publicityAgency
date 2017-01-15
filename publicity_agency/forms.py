from django import forms

class OrderForm(forms.Form):
	PUBLICITY=[('transport','tr_lable'),('presse','pr_lable')]
	company=forms.CharField(max_length=100)
	product=forms.CharField(max_length=200)
	design=forms.BooleanField(required=False)
	publicity_type=forms.ChoiceField(choices=PUBLICITY, widget=forms.RadioSelect)
	duration=forms.CharField(max_length=50)
	contact=forms.CharField()
	tel=forms.CharField()
	email=forms.EmailField()
