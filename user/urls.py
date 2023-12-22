from django.urls import path, include

from user import views
from user.views import RegisterView, loguot_view, ProfileView, DeleteProfileView, EditProdileView

app_name = "user"
urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', views.sign_in, name='login'),
    path('logout/', loguot_view, name="logout"),
    path('profile/<int:pk>/', ProfileView.as_view(), name="profile"),
    path('edit_profile/<int:pk>/', EditProdileView.as_view(), name="edit_profile"),
    path('delete_profile/<int:pk>/', DeleteProfileView.as_view(), name="delete_profile"),
]
