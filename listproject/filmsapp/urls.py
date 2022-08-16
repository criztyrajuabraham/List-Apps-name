from . import views
from django.urls import path
app_name='filmsapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:film_id>/',views.detail,name='detail'),
    path('addfilm',views.addfilm,name='addfilm'),
    path("updates/<int:id>/" , views.updates,name='updates'),
    path("delete/<int:id>/",views.delete,name='delete')
]