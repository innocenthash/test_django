

from django.urls import path

from cours.views import CourCreateView, CourDeleteView, CourDetailView, CourListView, CourUpdateView, FCourCreateView, FCourDeleteView, FCourUpdateView, FcourDetailView, FcoursListView


urlpatterns = [
    path('list_cours/', FcoursListView.as_view(), name='cours_list'),
    path('detail_cours/<int:pk>', FcourDetailView.as_view(), name='detail_cours'),
    path('create_cours/', FCourCreateView.as_view(), name='cours_create'),
    path('update_cours/<int:pk>', FCourUpdateView.as_view(), name='cours_update'),
    path('delete_cours/<int:pk>', FCourDeleteView.as_view(), name='cours_delete'),
]
# urlpatterns = [
#     path('list_cours/', CourListView.as_view(), name='cours_list'),
#     path('detail_cours/<int:pk>', CourDetailView.as_view(), name='detail_cours'),
#     path('create_cours/', CourCreateView.as_view(), name='cours_create'),
#     path('update_cours/<int:pk>', CourUpdateView.as_view(), name='cours_update'),
#     path('delete_cours/<int:pk>', CourDeleteView.as_view(), name='cours_delete'),
# ]