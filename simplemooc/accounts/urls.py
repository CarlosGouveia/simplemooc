from django.conf.urls import include, url
from simplemooc.accounts import views
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^entrar/$', login, {'template_name': 'accounts/login.html'},
        name='login'),
    url(r'^sair/$', logout, {'next_page': 'core:home'},
        name='logout'),
    url(r'^cadastre-se/$', views.register, name='register'),

]