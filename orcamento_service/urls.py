
from django.contrib import admin
from django.urls import path

from orcamento import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('orcamento/<int:id>/', views.orcamento, name='orcamento'),
]
