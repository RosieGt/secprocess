from django.db import models

# Create your models here.
class Pedido(models.Model):
    
    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done'),
    )

    nome = models.CharField("Nome do Aluno", max_length=150)
    dtNascimento = models.DateField(blank=True, null=True, verbose_name='Data de nascimento')
    nome_mae = models.CharField("Nome da Mãe", max_length=150)
    nrTelCelular = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular') 
    conclusao = models.CharField("Ano de conclusão", max_length=15)
    atendimento = models.CharField("Atendente", max_length=150)
    data_pedido = models.DateField("Data do pedido")
    descricao = models.TextField("Descrição")
    done = models.CharField(
        max_length=15,
        choices=STATUS,
        default='done',
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     
    def __str__(self):
        return "{} - {}".format(self.nome)


    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"