"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from vue import views as vue_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vue_views.startingpageBaseline, name='startingpageBaseline'),
    path('XAI/', vue_views.startingpageXAI, name='startingpageXAI'),
    path('experiment/<int:participant_id>/<str:condition>/<int:timer_active>/<int:slide_counter>/', vue_views.experiment, name='experiment'),
    path('end/<str:condition>/', vue_views.endpage, name='endpage'),
    path('training/<int:participant_id>/<str:condition>/<int:timer_active>/<int:slide_counter>/', vue_views.training, name='training'),
    path('prestudy/<int:participant_id>/<str:condition>/', vue_views.prestudy, name='prestudy'),
    path('startexperiment/<int:participant_id>/<str:condition>/', vue_views.startexperiment, name='startexperiment'),
    path('poststudy/<int:participant_id>/<str:condition>/', vue_views.poststudy, name='poststudy'),
    path('confidence/<int:participant_id>/<str:condition>/<int:timer_active>/<int:slide_counter>/', vue_views.confidence, name='confidence'),
    path('mobile/', vue_views.mobile, name='mobile')
]

urlpatterns += staticfiles_urlpatterns()
