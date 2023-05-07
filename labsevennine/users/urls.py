from django.urls import path, include
from users.views import Register, user_home, UserUpdateView

urlpatterns = [
    # include authentication-related views, such as login and logout
    path('', include('django.contrib.auth.urls')),
    #as_view() method is used to create the view function that handles the GET and POST requests
    path('register/', Register.as_view(), name = 'register'),
    path('user_home/', user_home, name='user_home'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),

 
]