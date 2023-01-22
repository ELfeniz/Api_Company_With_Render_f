from django.urls import path   # nos permitira establecer una ruta

from .views import companyListView


urlpatterns = [                 # el as_view(), es para convertirla en una lista
    path('company/', companyListView.as_view(), name='company_list' ),  # ruta raiz que nos devolvera todas las compañias
    path('company/<int:id>/', companyListView.as_view(), name='company_process')
]