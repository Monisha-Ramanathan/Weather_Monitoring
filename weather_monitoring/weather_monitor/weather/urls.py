from.import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='main'),
    path('index/',views.style,name='index'),
    path('style/',views.style,name='style'),
    path('script/',views.script,name='script'), 
]