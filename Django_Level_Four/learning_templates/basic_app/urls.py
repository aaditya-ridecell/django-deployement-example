from django.urls import path
from . import views

#Template Tagging.
#Always set the app_name when using template tagging. Django looks for it
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name="relative"),
    path('other/', views.other, name="other")
]
