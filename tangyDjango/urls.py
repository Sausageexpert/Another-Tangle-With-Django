# Create URL patterns here
from . import views # the dot means same folder
from django.urls import path 
#from .views import HomePageView
app_name = 'tangyDjango'

urlpatterns = [
    path('',views.index, name='index'),
    path('item/', views.item, name='item'),
    path('<int:item_id>/', views.detail, name='detail'), # displaying an integer (the primary key) as the name of the page
    path('add', views.create_item, name='create_item'),
    path('edit/<int:id>/', views.edit_item, name="edit_item"),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]

'''
the quotes would be empty for an empty path, index is the name of the path to views.index.
If something was in the quotations it would appear as tangyDjango/something in the localhost
'''
