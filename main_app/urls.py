from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('allCollection/', views.allCollection, name='allCollection'),
    path('allCollection/<int:nft_id>/', views.nftDetails, name='detail'),
    path('allCollection/create/', views.NftCreate.as_view(), name='nft_create'),
    path('allCollection/<int:pk>/update/', views.nftUpdate.as_view(), name='nft_update'),
    path('allCollection/<int:pk>/delete/', views.nftDelete.as_view(), name='nft_delete'),
    path('allCollection/<int:nft_id>/add_rating/', views.add_rating, name='add_rating'),

    path('chain/', views.ChainList.as_view(), name='chain_index'),
    path('chain/<int:pk>/', views.ChainDetail.as_view(), name='chain_detail'),
    path('chain/create/', views.ChainCreate.as_view(), name='chain_create'),
    path('chain/<int:pk>/update/', views.ChainUpdate.as_view(), name='chain_update'),
    path('chain/<int:pk>/delete/', views.ChainDelete.as_view(), name='chain_delete'),

]