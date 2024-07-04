from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from home.views import home, contact, success_page
from food.views import receipes, delete_receipe, update_receipe, login_page,register_page

urlpatterns = [
    path('', home, name="home"),
    path('receipes/', receipes, name="receipe"),
    path('delete-receipe/<int:id>/', delete_receipe, name="delete_receipe"),
path('update-receipe/<int:id>/', update_receipe, name=" update_receipe"),


    # Corrected URL pattern
    path('contact/', contact, name="contact"),
    path('success_page/', success_page, name="success_page"),
    path('admin/', admin.site.urls),
    path('login/', login_page, name="login_page"),
    path('register/', register_page, name="register_page"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Note: You don't need to include staticfiles_urlpatterns() if you're serving static files with Django in DEBUG mode.
