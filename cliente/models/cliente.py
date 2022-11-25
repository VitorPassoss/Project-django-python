from django.db import models

class Cliente(models.Model):
    tipo_pessoa = [
        ("F", "Fisica"),
        ("J", "Juridica")
    ]
    nome = models.CharField(max_length=100, blank=False)
    cpf_cnpj  = models.CharField(max_length=14 , blank=False)
    tipo = models.CharField(max_length=1, choices=tipo_pessoa)
    dt_criacao = models.DateTimeField(verbose_name="data_de_criacao", auto_now_add=True)
    dt_alteracao = models.DateTimeField(verbose_name="data_de_alteracao", auto_now=True)
    def __str__(self):
        return self.nome 


    