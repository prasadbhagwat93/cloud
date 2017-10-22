from django.conf.urls import url
from howdy import views

urlpatterns = [
    url(r'^search$', views.search),
    url(r'^index/', views.index)
]
