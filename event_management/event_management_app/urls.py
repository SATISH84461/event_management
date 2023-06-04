from django.urls import path
from . import views

urlpatterns = (
    path('', views.home, name="Homepage"), #home page will list all the upcoming and past event
    path('create_event', views.create_event, name="create_event"),#create new event
    path('signup', views.create_user, name="create_user"),#sigup/register user
    path('signin', views.login_user, name="login_user"),#login/signin user
    path('signout', views.logout_user, name="logout"),# logout user
    path('profile', views.profile, name="profile"),# view user profile
    path('event/<int:id>', views.get_event_details, name="event_detail"), # get complete details of he event
    path('register/event/<int:event_id>', views.event_register, name="event_register"), # register for an event
)