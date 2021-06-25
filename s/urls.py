from django.urls import path
from . import views
app_name = 's'
urlpatterns = [
    path('create/', views.urlShort, name="short_url"),
    path("s/<str:short_url>", views.urlRedirect, name="redirect")
]
