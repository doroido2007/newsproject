from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        '''UserCreationFormのサブクラス'''
        model = CustomUser

        fields = ('username', 'email', 'password1', 'password2')