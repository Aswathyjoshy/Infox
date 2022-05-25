from . import views
from django.urls import path

urlpatterns = [
    path('',views.load_profile_page,name='load_profile_page'),
    path('add_profile',views.add_profile,name='add_profile'),
    path('show_details',views.show_details,name='show_details'),
    path('edit_user_page/<int:pk>',views.edit_user_page,name='edit_user_page'),
    path('edit_user_data/<int:pk>',views.edit_user_data,name='edit_user_data'),
    path('delete_user_data/<int:pk>',views.delete_user_data,name='delete_user_data'),
]