from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Redirect root URL to /projects/
    path('', RedirectView.as_view(url='/projects/', permanent=True)),
    
    path("", include("pages.urls")),
    path("projects/", include("projects.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)