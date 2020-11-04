# -*- coding:utf-8 _*-
""" 
@Author: John
@Email: workspace2johnwu@gmail.com
@License: Apache Licence 
@File: url.py.py 
@Created: 2020/10/18
@site:  
@software: PyCharm 

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃            ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神獸保佑    ┣┓
                ┃　永無BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛ 
"""

from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url
from main import views

from django.conf.urls import include
app_name = 'main'
urlpatterns = [
    path("", views.homepage, name='homepage'),
    path("login/", views.loginPage, name='login'),
    # re_path(r'^user/(?P<pk>\d+)/room/$', views.userPage, name='room'),
    path('user/', views.userPage, name='user-page'),
    re_path(r'^user/(?P<pk>\d+)/profile/update/$', views.profile_update, name='profile_update'),
    re_path(r'^user/(?P<pk>\d+)/pwd_change/$', views.pwd_change, name='pwd_change'),
    path("rigister/", views.register, name='rigister'),
    path("logout/", views.logout, name='logout')
]