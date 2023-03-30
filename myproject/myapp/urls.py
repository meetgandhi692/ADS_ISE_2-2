from django.urls import path
from . import views

urlpatterns=[
    path('',views.userreg,name='userreg'),
    path('insertuser',views.create_user,name='userreg ')
]