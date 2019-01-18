from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views
from graphene_django.views import GraphQLView

urlpatterns = [
    url(r'^django-admin/', admin.site.urls),

    url(r'', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),

    url(r'^search/$', search_views.search, name='search'),

    url(r'', include(wagtail_urls)),

]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
