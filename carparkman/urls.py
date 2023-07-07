from django.urls import path
from . import views

app_name = "carparkman"

urlpatterns = [

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout', views.logout_request, name="logout"),
    # path('', views.button),
    # path('csd', views.stream_video, name="csd"),

    # path("run-script/", views.run_script, name='run-script'),

    path("dashboard/", views.index, name="dashboard"),
    path("charts/", views.charts, name="charts"),
    path("widgets/", views.widgets, name="widgets"),


]
