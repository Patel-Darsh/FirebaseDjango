from django.urls import path
from custom_auth import views

app_name = 'cust'

urlpatterns = [
    path('', views.signIn),
    path('postsignIn/', views.postsignIn),
    path('signUp/', views.signUp, name="signup"),
    path('logout/', views.logout, name="log"),
    path('postsignUp/', views.postsignUp),

    # -------------------------------------------------------

    path('reset/', views.reset),
    path('postReset/', views.postReset),
]
