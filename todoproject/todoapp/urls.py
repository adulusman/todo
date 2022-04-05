from django.urls import path
from . import views

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('chome/',views.Tasklistview.as_view(),name='chome'),
    path('cdetail/<int:pk>/',views.Taskdetailview.as_view(),name='cdetail'),
    path('cupdate/<int:pk>/',views.Taskupdateview.as_view(),name='cupdate'),
    path('cdelete/<int:pk>/',views.Taskdeleteview.as_view(),name='cdelete')
]
