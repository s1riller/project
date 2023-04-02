from django.urls import path, include
from . import views



urlpatterns = [

    path('',views.home,name='home'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('index/', views.index, name='index')
]