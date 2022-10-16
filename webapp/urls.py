from django.urls import path
from webapp.views.tasks import TaskView, add_view,  delete_view, confirm_delete, TaskUpdateView
from webapp.views.base import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tasks/add/', add_view, name='task_add'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', delete_view, name='task_delete'),
    path('tasks/<int:pk>/confirm-delete/', confirm_delete, name='confirm_delete'),
    path('tasks/', IndexView.as_view()),
    path('tasks/<int:pk>', TaskView.as_view(), name='task_detail')
]
