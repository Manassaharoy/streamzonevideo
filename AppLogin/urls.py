from django.urls import path
from AppLogin import views

app_name = "App_login"

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.login_page, name='login'),
    path('edit/', views.edit_profile, name='edit'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_user, name='logout'),
]
