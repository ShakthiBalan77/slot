    # my_app/urls.py
    from django.urls import path
    from . import views

    urlpatterns = [
        path('timetable/', views.my_view),
    ]