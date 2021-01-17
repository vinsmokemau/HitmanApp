"""Hit URLs."""

# Django
from django.urls import path

# Views
from apps.hits import views


urlpatterns = [

    # Hit
    path(
        route='hits/',
        view=views.HitList.as_view(),
        name='list'
    ),
    path(
        route='hits/bulk/',
        view=views.BulkList.as_view(),
        name='bulk'
    ),
    path(
        route='hits/create/',
        view=views.CreateHit.as_view(),
        name='create'
    ),
    path(
        route='hits/<int:id>/',
        view=views.HitDetail.as_view(),
        name='detail'
    ),
    path(
        route='hits/<int:hit_id>/failed/',
        view=views.FailedHit.as_view(),
        name='failed'
    ),
    path(
        route='hits/<int:hit_id>/completed/',
        view=views.CompletedHit.as_view(),
        name='completed'
    ),
    path(
        route='hits/<int:id>/update/',
        view=views.NewAssignee.as_view(),
        name='update'
    ),

]
