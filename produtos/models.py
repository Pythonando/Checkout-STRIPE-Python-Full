from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import CharField, IntegerField

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.FloatField()

    def __str__(self) -> str:
        return self.nome
    
    def exibe_preco(self):
        return "{:.2f}".format(self.preco)


class Pedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=DO_NOTHING)
    payment_intent = CharField(max_length=30, unique=True)
    email = models.EmailField()
    valor_pago = IntegerField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.email
