from django.urls import path
from .views import UserViewSet

app_name = 'users'

urlpatterns = [
    path('signup/', UserViewSet.as_view({'post':'create'}), name='user_signup')
]