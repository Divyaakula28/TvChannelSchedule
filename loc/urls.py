from loc import views
from django.urls import path, include

urlpatterns = [
    path('loc/',views.loc,name='loc'), 
    path('drop/',views.drop,name='drop'), 
    path('home/',views.home,name='home'), 
    path('nav/',views.nav,name='nav'), 
    path('dis/',views.dis,name='dis'), 
    path('test/',views.test,name='test'),

  
]
