# from django.urls import path
# from .views import Home

# app_name = 'netflixpp'

# urlpatterns = [
#     path('', Home.as_view(), name="Home")
# ]
from django.contrib import admin
from django.urls import path, include
from netflixpp.views import account, admin, account_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('netflixpp.urls')),
    path('account/', include('allauth.urls')),
]