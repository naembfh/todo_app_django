from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name= 'homePage'),
    path('add_task/',views.add_task,name= 'addTask'),
    path('show_tasks/',views.show_tasks,name= 'show_Tasks'),
    path('delete_task/<int:id>/',views.delete_task,name='delete_Task'),
    path('edit_task/<int:id>/',views.edit_task,name='edit_Task'),
    path('complete_task/<int:id>/',views.complete_task,name='complete_Task'),
    path('completed_tasks/',views.completed_tasks,name= 'completed_Tasks'),
]
