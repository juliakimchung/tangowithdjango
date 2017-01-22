from django.conf.urls import url
from rango import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

	url(r'^rango', views.index, name='index'),
	url(r'^about/', views.about, name='about'),
	url(r'^static/', views.static, name="static")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)