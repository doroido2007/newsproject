from django.urls import path
from . import views

app_name = 'newsapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('post/', views.CreateNewsView.as_view(), name='post_news'),

    path('post_done/', views.PostSuccessView.as_view(), name='post_done2'),

    path('photos/<int:category>', views.CategoryView.as_view(), name='news_cat'),

    path('user-list/<int:user>', views.UserView.as_view(), name='user_list2'),

    path('photo-detail/<int:pk>/', views.DetailView.as_view(), name='detail2'),

    path('news/<int:pk>/delete', views.NewsDeleteView.as_view(), name='news_delete'),
]