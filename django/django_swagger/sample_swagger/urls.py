from django.urls import path, include
import sample_swagger.views as views
urlpatterns =[
    path('mysql/',views.mysql,name='mysql'),
    path('producer/',views.producer,name='producer'),
    path('consumer/',views.consumer,name='consumer'),
    path('dbinput/',views.dbinput,name='dbinput'),]
