from django.urls import path
from . import views


urlpatterns = [
        path('register/', views.registerPage, name="register"),
        path('login/', views.loginPage, name="login"),
        path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name = "home"),
    path('bid/', views.bid, name="bid"),
    path('create_project/', views.createProject, name="create_project"),
    path('create_bid/', views.createbid, name="create_bid"),
    path('createbid_boq/', views.createbid_BOQ, name="createbid_boq"),
    path('BOQ/', views.BOQ, name="BOQ"),
    path('update_BOQ/<str:pk>//', views.updateBOQ, name="update_BOQ"),
    path('user/', views.userPage, name="user-page"),
    path('update_order/<str:pk>/', views.updateProject, name="update_order"),
    path('update_bid/<str:pk>/', views.updateBid, name="update_bid"),

]
