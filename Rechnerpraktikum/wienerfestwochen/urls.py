from django.urls  import path, include
from .            import views


app_name = 'wienerfestwochen'

urlpatterns = [
    path('dialog1/', views.dialog1, name='dialog1'),
    path('', views.index, name="index"),
    path('Produktion/', views.Produktion_view, name="Produktion"),
]
