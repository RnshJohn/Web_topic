
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from face_emotion import views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),

]
