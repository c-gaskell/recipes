from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('test/', views.TestView.as_view(), name='test'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('user/<str:user>/recipe/<str:recipe>', views.RecipeView.as_view(), name='recipe'),
    path('user/<str:user>', views.ProfileView.as_view(), name='profile'),

]
