from django.urls import path

from . import views

urlpatterns = [
    path('partner/<str:id>/', views.PartnerDetailView.as_view(), name='partner-detail'),
    path('partners/nearest/', views.NearestPartnerView.as_view(), name='nearest-partner'),
]
