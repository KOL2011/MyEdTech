
from django.urls import path #Make sure this is imported to work!!!
from basic_app import views
from django.urls import path



#TEMPLATE URLs
app_name = 'basic_app'

urlpatterns=[

path('register/',views.register,name='register'),
path('user_login/',views.user_login,name='user_login'),

]
