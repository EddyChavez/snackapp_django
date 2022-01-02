from django.contrib import admin
from django.urls import path
from knox import views as knox_views

from . import views

app_name = "users_app"

urlpatterns = [
    # registrar nuevo usuario
    path(
        'api/register/',
        views.RegisterAPI.as_view(),
    ),
    # login
    path(
        'api/login/',
        views.LoginAPI.as_view(),
    ),
    # cerrar sesion
    path(
        'api/logout/',
        knox_views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        'api/logoutall/',
        knox_views.LogoutAllView.as_view(),
        name='logoutall'
    ),
    # recuperar usuario
    path(
        'api/user/',
        views.UserAPI.as_view(),
    ),
    # Listar usuarios mortales
    path(
        'api/users/',
        views.ListUsers.as_view(),
    ),
    # editar usuario
    path(
        'api/user/edit/<int:pk>/',
        views.EditUserAPI.as_view(),
    ),
    # agregar permisos al grupo
    path(
        'api/tribes/assign-permissions/<int:pk>/',
        views.AssignPermissions.as_view(),
    ),
    # cambiar contraseña
    path(
        'api/change-password/',
        views.ChangePasswordView.as_view(),
    ),
    # listar grupos creados por cada usuario
    path(
        'api/tribes/by-user/',
        views.List_Tribes.as_view(),
    ),
    # listar grupos a los que pertenece cada usuario
    path(
        'api/users/belong-tribes/',
        views.List_BelongTribes.as_view(),
    ),
    # agregar grupo
    path(
        'api/tribes/add/',
        views.AddTribes.as_view(),
    ),
    # editar grupo
    path(
        'api/tribes/edit/<int:pk>/',
        views.EditTribes.as_view(),
    ),
    # eliminar grupo
    path(
        'api/tribes/remove/<int:pk>/',
        views.RemoveTribes.as_view(),
    ),
    # recuperar miembros del grupo
    path(
        'api/tribes/members/<int:pk>/',
        views.RetrieveMemebers.as_view(),
    ),
    # enviar correo a todos los participantes del evento
    path(
        'api/tribes/invitations/',
        views.Invitations.as_view(),
    ),
    # autocompletable para grupos, solo muestra lo que creo cada usuario
    path(
        'api/tribes/',
        views.List_Groups.as_view(),
    ),
    # Enviar correo llego pedido
    path(
        'api/tribes/delivered/',
        views.Delivered.as_view(),
    ),
    # Enviar correo agradecimiento por donacion
    path(
        'api/tribes/thank/',
        views.Thank.as_view(),
    ),
    # salir del grupo
    path(
        'api/tribes/leave/<int:pk>/<int:idUser>/',
        views.LeaveTribe.as_view(),
    ),
    # envio de correo de contacto
    path(
        'api/users/contact/',
        views.Contact.as_view(),
    ),
    # Prueba de Mensaje WhatsApp
    path(
        'api/tribes/alertas/',
        views.Alertas.as_view(),
    ),
    # Prueba Agregar producto    
]
