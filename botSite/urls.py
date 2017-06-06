from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="base_homepage.html"), name="homepage"),
    url(r'^database/', include('database.urls'), name="database")
]
