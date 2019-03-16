from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include
from mysite.views import PersonSet, PersonList, EmployeeSet, PersonAdd, Test, FileView, RegisterUser
from .router import router
from rest_framework.authtoken import views
from django.contrib.auth.views import LogoutView, LoginView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = format_suffix_patterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    # path('api/user', EmployeeSet.as_view(), name='user-list'),
    path('api/list', PersonList.as_view(), name='person-list'),
    path('api/person/<int:pk>', PersonSet.as_view(), name='person'),
    path('api/pp/<int:pk>', PersonSet.as_view(), name='pp'),
    path('api/update/<int:pk>', PersonAdd.as_view(), name='pp'),
    path('api/add', PersonAdd.as_view(), name='pp'),
    # path('api/+'r'(?P<fname>)'+'add',Test.as_view(), name ='pp')
    path('api/test/<int:pk>', Test.as_view(), name='pp'),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-auth-token'),

    path('api/register', RegisterUser.as_view(), name='register'),

    path('list', LoginView.as_view(), name='aut-list'),

    path ('api/files', FileView.as_view(), name='files')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
