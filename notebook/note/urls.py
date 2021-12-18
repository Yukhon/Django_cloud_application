from django.urls import path
from . import views

urlpatterns = [

    path('add_note', views.add_note_view),
    path('all', views.note_index_view),
    path('mod/<int:id>', views.update_view),
    path('del/<int:id>', views.del_view)


]
