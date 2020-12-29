from django.conf.urls import include, url
from rest_framework import routers
from photos import views


router = routers.DefaultRouter()
router.register(r"image", views.ImageView)
router.register(r"album", views.AlbumView)


urlpatterns = [url("^", include(router.urls)), url("^album/<int:pk>/", views.AlbumView)]

