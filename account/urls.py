from django.urls import path

from .views import profile_user, login_view, logout_view, sign_up, change_password, update_view

app_name = 'account'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', sign_up, name='signup'),
    path('profile/', profile_user, name='profile'),
    path('password/', change_password, name='ch_password'),
    path('update/', update_view, name='update_view')
]
