from django.urls import path

from . import views

app_name = "products_app"

urlpatterns = [
    # Crear producto
    path(
        'api/products/create/',
        views.CreateProduct.as_view(),
    ),
    # Listar productos
    path(
        'api/products/list/<int:idEvent>/',
        views.List_ProductEvent.as_view(),
    ),
    # Borrar producto
    path(
        'api/products/delete/<int:pk>/',
        views.DeleteProduct.as_view(),
    ), 
]