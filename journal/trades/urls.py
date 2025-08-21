from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('trades/', views.TradeListView.as_view(), name='trade-list'),
    path('trades/new/', views.TradeCreateView.as_view(), name='trade-create'),
    path('trades/<int:pk>/edit/', views.TradeUpdateView.as_view(), name='trade-update'),
    path('trades/<int:pk>/delete/', views.TradeDeleteView.as_view(), name='trade-delete'),
]
