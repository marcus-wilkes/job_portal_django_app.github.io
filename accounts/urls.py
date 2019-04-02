from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "accounts"

urlpatterns = [
    path('employee/register', RegisterEmployee.as_view(), name='employee-register'),
    path('login', LoginView.as_view(), name='login'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
