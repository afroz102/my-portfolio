from django.urls import path
from . import views

# If more than one pages named details or anything exists in that case we will have to assign an app_name to distinguish it with the other pages with same name
app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.details, name='details'),
]
