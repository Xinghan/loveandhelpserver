from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter, SimpleRouter
from news import views as news_views
from account import views as account_views
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register(r'entries', news_views.EntryViewSet)
router.register(r'accounts', account_views.UserView)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proj1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token')
)
