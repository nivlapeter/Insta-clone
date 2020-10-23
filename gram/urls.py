from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns = [
    url('', views.index, name='index'),
    url('', views.registration, name='registration'),
    url('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.confirm, name='confirm'),
    url('user/(?P<username>\w{0,50})', views.profile, name='profile'),
    url('search/', views.profile_search, name='profile_search'),
    url('upload/$', views.pic_upload, name='pic_upload'),
    url('image/(?P<image_id>\d+)', views.solo_image, name='solo_image'),
    url('accounts/edit/', views.profile_edit, name='profile_edit'),
]



