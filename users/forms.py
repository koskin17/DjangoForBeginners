from django import forms # Этот файл импортируется для кастомизации форм
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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
            
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Введите имя"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Введите фамилию"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Введите имя пользователя"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': "Введите адрес эл. почты"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Введите пароль"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Подтвердите пароль"}))
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')       
        
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'   
        
