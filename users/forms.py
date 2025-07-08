from django.contrib.auth.forms import AuthenticationForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    """
    Кастомная форма логина, которая наследуется от Django's AuthenticationForm.
    Она может быть расширена дополнительными полями или методами валидации.
    """
    class Meta:
        model = User
        fields = ['username', 'password']   # Подробнее про class Meta: file:///E:/My%20project/DjangoForBeginners/Help/Class%20Meta.txt
