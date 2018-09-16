# authly_app/urls.py
from django.urls import path
from django.conf.urls import url
from tidder import views

# SET THE NAMESPACE!
app_name = 'tidder'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('post', views.create_post, name='create_post'),
    path('', views.index, name='post_view'),
    # path('/api/users', views.sendJson, name='sendJson')
]