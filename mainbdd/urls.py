from django.urls import path
from django.conf import settings
from . import views


urlpatterns=[
    path('allMag/', views.getAllMagasins),
    path('AllCategories/', views.getAllCategories),
    path('getTopCategories/', views.getTopCategories),
    path('getMagasinsEnTandance/', views.getMagasinsEnTandance),
    path('CategorieMagasins/<int:id>/', views.getCategorieMagasins),
    path('getMagasinDetail/<int:id>/', views.getMagasinDetail),
    path('getFavoris/<int:id>/', views.getFavoris),
    path('CategorieMagasins/<int:id>/', views.getCategorieMagasins),
    path('ALlServices/', views.getALlServices),
    path('getUserDetails/<int:id>/', views.getUserDetails),



    path('postPublication/<int:id>/', views.postPublication),
    path('postMagasin/<int:id>/', views.postMagasin),
    path('postHoreur/<int:id>/', views.postHoreur),
    path('getPublicationDetails/<int:id>/', views.getPublicationDetails),
    path('ModifierMagasin/<int:id>/', views.ModifierMagasin),
    path('user/', views.user),
    #path('postService/', views.postService),

    path('filtrer/<int:prix_min>/<int:prix_max>/<int:rank_min>/<int:rank_max>/<int:categorie>/', views.filtrer),

]
