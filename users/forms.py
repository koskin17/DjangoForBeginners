from django import forms # Этот файл импортируется для кастомизации форм
from django.contrib.auth.forms import AuthenticationForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    """
    Кастомная форма логина, которая наследуется от Django's AuthenticationForm.
    Она может быть расширена дополнительными полями или методами валидации.
    """
    
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'})) # Задаётся строковый тип данных и указывается виджет о том, что происходит в этой форме. В atts в виде словаря указываются все дополнительные параметры из html-верстки
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    
    class Meta:
        model = User
        fields = ['username', 'password']   # Подробнее про class Meta: file:///E:/My%20project/DjangoForBeginners/Help/Class%20Meta.txt
        
        
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'            
        
