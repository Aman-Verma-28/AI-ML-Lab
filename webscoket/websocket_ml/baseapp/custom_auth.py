from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
myKey = "<YourKey>"
class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.GET.get('username')
        secret_key = request.GET.get("secret_key")
        
        if secret_key is None:
            return (None, "400: Bad Request \n No key provided")
        if secret_key != myKey:
            return ("403: Provided key is incorrect", None)
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return (None, "404: User not found")
        
        return (user, secret_key)
