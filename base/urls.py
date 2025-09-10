from django.urls import path
from .import views

urlpatterns=[
    path('home',views.home,name='home'),
    path('details/<str:all_tasks>',views.details,name='details'),
    path('about',views.about,name='about'),
    path('add',views.add,name='add'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('confirm_delete/<int:pk>',views.confirm_delete,name='confirm_delete'),
    path('delete_/<int:pk>',views.delete_,name='delete_'),
    path('history',views.history,name='history'),
    path('delete_history_confirm/<int:pk>',views.delete_history_confirm,name='delete_history_confirm'),
    path('history_delete/<int:pk>',views.history_delete,name='history_delete'),
    path('history_restore/<int:pk>',views.history_restore,name='history_restore'),
    path('history_clear',views.history_clear,name='history_clear'),
    path('history_restore_all',views.history_restore_all,name='history_restore_all'),
    path('complete_task/<int:pk>',views.complete_task,name='complete_task'),
    path('completed',views.completed,name='completed'),
    
]