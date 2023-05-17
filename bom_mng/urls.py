from django.urls import path

from .views import base_views, bom_views

app_name = 'bom_mng'

urlpatterns = [
    path('', base_views.index, name = 'index'),
    path('<int:bom1_id>/', base_views.detail, name='detail'),
    path('add_bom/', bom_views.add_bom, name='add_bom'),
    path('edit_bom/<int:bom1_id>/', bom_views.edit_bom, name = 'edit_bom'),
    path('delete_bomitm/',bom_views.delete_bomitm, name = 'del_bomitm'),
    path('uploadbom/', bom_views.upload_bom, name = 'uploadbom'),
]

