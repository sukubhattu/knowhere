from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views
urlpatterns = [
	path('', user_views.home, name = 'users_index'),
	path('register/', user_views.register, name = 'user_sign_up'),
	path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'user_log_in'),
	path('logout', auth_views.LogoutView.as_view(template_name= 'users/logout.html'), name = 'user_log_out'),
]