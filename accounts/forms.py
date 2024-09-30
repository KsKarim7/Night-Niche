from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserAccount
from django.core.validators import MinLengthValidator



class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    phone_number = forms.CharField(max_length=11, validators=[MinLengthValidator(11)])
  
    class Meta:
        model = User
        fields = ['username','password1','password2','first_name','last_name','email','birth_date','phone_number']

    def save(self,commit=True):
        our_user = super().save(commit=False)
        if(commit == True):
            our_user.save() 
            phone_number = self.cleaned_data['phone_number']
            birth_date = self.cleaned_data['birth_date']

                    
        UserAccount.objects.create(
                user = our_user,
                birth_date = birth_date,
                phone_number =phone_number,
                account_no = 222010 + our_user.id
        )
        return our_user
    
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class' : (
                    'appearance-none block w-full bg-blue-300 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })