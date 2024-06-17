from django.http import HttpRequest, JsonResponse
from django.urls import path

from . import views
from .errors.request_error_handling import request_method_error


def resolve_path_collision(request: HttpRequest, service_name: str) -> JsonResponse:
    if request.method == 'POST':
        return views.create_or_update(request, service_name)
    elif request.method == 'GET':
        return views.get_password_by_service_name(request, service_name)
    else:
        return JsonResponse(request_method_error(request), status=400)


urlpatterns = [
    path('password/<str:service_name>/', resolve_path_collision, name='resolve_path_collision'),
    path('password/', views.get_password_by_part_of_service_name, name='get_password_by_part_of_service_name'),
]
