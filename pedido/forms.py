from django import forms

from .models import Pedido

class PedidoForm(forms.ModelForm):

    class Meta:
        model = Pedido
        fields = ['nome', 'dtNascimento', 'nrTelCelular', 'nome_mae', 'conclusao', 'atendimento', 'data_pedido', 'descricao']