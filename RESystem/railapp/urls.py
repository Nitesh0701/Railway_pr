from django.urls import path
from railapp.views import train_search_view,train_search_view_org,railinfo,index1,index2

urlpatterns=[
    path('',train_search_view),
    path('t/',train_search_view_org),
    path('welcome/',railinfo),
    path('search/',index1),
    path('pnr/',index2),

]