from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings # add
from django.conf.urls.static import static # add

urlpatterns = [
    url(r'^$', views.first_view, name='first_view'),
    # url(r'^count/$', views.count, name='count'),
    path('count', views.count, name="login"),
   
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)