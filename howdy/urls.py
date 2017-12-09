from django.conf.urls import url
from howdy import views

urlpatterns = [
    url(r'^search$', views.search),
    url(r'^index', views.index),
    url(r'^locations$', views.locations),
    url(r'^itemManagment', views.items),
    url(r'^add', views.add_items),
    url(r'^delete', views.delete_items),
    url(r'^view', views.view_items),
    url(r'^login', views.login),
    url(r'^signup', views.signup),
]

