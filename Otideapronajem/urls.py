
from django.contrib import admin
from django.urls import path, include
from homepage import views
import rezervace.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('cenik', views.cenik, name='cenik'),
    path('ucebny/', include('ucebny.urls'), name='ucebny'),
    path('rezervace/', rezervace.views.rezervace, name='rezervace'),
    path('sitemap.xml', views.sitemap, name='sitemap'),
    path('rezervace-poslana', rezervace.views.rezervace_poslana, name='rezervace_poslana'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
