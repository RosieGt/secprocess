from django.urls import path
from .views import base, cadastrar_pedido, listar_pedido, pedidoView, editPedido, deletePedido, changeStatus, pedido_finalizado


urlpatterns = [
    path('', base, name='base'),
    path('cadastrar/', cadastrar_pedido, name='cadastrar_pedido'),
    path('listar/', listar_pedido, name='listar_pedido'),
    path('changestatus/<int:id>', changeStatus, name="change-status"),
    path('pedido/<int:id>', pedidoView, name="pedidoView"),
    path('edit/<int:id>', editPedido, name="editPedido"),
    path('delete/<int:id>', deletePedido, name="deletePedido"),
    path('done/', pedido_finalizado, name='pedido_finalizado'),
]    