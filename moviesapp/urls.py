
from django.urls import path,include
from . import views
app_name='moviesapp'
urlpatterns = [
       path('',views.index,name='index'),
       path('movie/<int:movie_id>/',views.detail,name='detail'),
       path('add/',views.add,name='add'),
       path('update/<int:id>/',views.update,name='update')



]
