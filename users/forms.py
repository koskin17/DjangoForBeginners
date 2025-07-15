from django import forms # Этот файл импортируется для кастомизации форм
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm  # UserChangeForm - специальный встроенный в django модуль для редактирования информации 

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
        
class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}))  # Параметр readonly: True позволяет отображать значение поля, но запретить его изменение (в данном случае блокировка изменения пользователем в своем профиле.)
    email = forms.CharField(widget=forms.EmailInput(attrs={'readonly': True}))  # Параметр readonly: True позволяет отображать значение поля, но запретить его изменение (в данном случае блокировка изменения пользователям в своем профиле.)
    image = forms.ImageField(widget=forms.FileInput(), required=False)  # Параметр required=False позволяет не загружать изображение, т.е. делает это поле не обязательным.
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image')
        
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'  
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'