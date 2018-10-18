from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from .routers import router


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]
