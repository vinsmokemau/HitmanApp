"""Users URLs."""

# Django
from django.urls import path

# Views
from apps.users import views


urlpatterns = [
    
    # Registration
    path(
        route='',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),

    # Users
    path(
        route='hitmen/',
        view=views.UserList.as_view(),
        name='list'
    ),
    path(
        route='hitmen/<int:id>/',
        view=views.UserDetail.as_view(),
        name='detail'
    ),
    path(
        route='hitmen/<int:user_id>/inactive/',
        view=views.InactiveUser.as_view(),
        name='inactive'
    ),

    # Managers
    path(
        route='manager/<int:id>/add/',
        view=views.AddLackeyView.as_view(),
        name='add-lackey'
    ),

]
