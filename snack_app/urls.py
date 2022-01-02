from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),

    # resetear contraseña
    path('api/password_reset/',
         include('django_rest_passwordreset.urls',
                 namespace='password_reset')),

    # apps locales
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.events.urls')),
    re_path('', include('applications.orders.urls')),
    re_path('', include('applications.payments.urls')),
    re_path('', include('applications.products.urls')),

    # urls para ckeditor
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),

    # routers
    re_path('', include('applications.events.routers')),
    re_path('', include('applications.orders.routers')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
