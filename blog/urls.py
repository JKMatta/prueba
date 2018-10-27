from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	path('', views.inicio, name='inicio'),
	path('inicio', views.inicio, name='inicio'),
    path('galery', views.post_list, name='post_list'),
    path('adopta', views.adopta, name='adopta'),
    path('contacto', views.contacto, name='contacto'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    path(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]