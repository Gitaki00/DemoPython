from . import views
from django.urls import path
app_name='todoapp'

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:taskid>/',views.update,name='update'),
    path('listview/',views.tasklistview.as_view(),name='list_view'),
    path('detailview/<int:pk>/',views.taskdetailview.as_view(),name='detail_view'),
    path('updateview/<int:pk>/',views.taskupdateview.as_view(),name='update_view'),
    path('deleteview/<int:pk>/',views.taskdeleteview.as_view(),name='delete_view')
]