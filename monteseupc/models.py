from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

# Create your models here.
processadores = [
    ('INTEL', 'Intel'),
    ('AMD', 'Amd'),
    ('ambos', 'Intel e AMD'),
]

slots_suportado = [
    ('2', '2'),
    ('4', '4'),
]

tamanho_memorias = [
    ('4GB', '4GB'),
    ('8GB', '8GB'),
    ('16GB', '16GB'),
    ('32GB', '32GB'),
    ('64GB', '64GB'),
]


class MonteSeuPC(models.Model):
    processador = models.ForeignKey("Processador", verbose_name=("Processador"), on_delete=models.CASCADE)
    placa_mae = models.ForeignKey("PlacaMae", verbose_name=("Placa mae"), on_delete=models.CASCADE)
    memoria = models.ForeignKey("Memoria", verbose_name=("Memoria Ram"), on_delete=models.CASCADE)
    qtd_de_memoria = models.IntegerField("Quantidade de Memoria", validators=[MinValueValidator(1),MaxValueValidator(4)])
    tamanho_da_memoria = models.CharField("Tamanho da Memoria", choices=tamanho_memorias, max_length=50)
    placa_de_video = models.ForeignKey("PlacaDeVideo", verbose_name=("Placa de Video"), on_delete=models.CASCADE, null=True)


class Processador(models.Model):
	produto = models.CharField("Produto", max_length=50)
	marca = models.CharField("Marca", choices=processadores,max_length=50)
	def __str__(self):
  		return self.produto


class PlacaMae(models.Model):
    produto = models.CharField("Produto", max_length=50)
    processadores_suportados = models.CharField("Processador Suportados", choices=processadores, max_length=50)
    slots = models.IntegerField("Quantidade de Slots", choices=slots_suportado)
    memoria_suportada = models.CharField("Memoria suportada", choices=tamanho_memorias, max_length=10)
    video_integrado = models.BooleanField("Video integrado", default=True)

    def __str__(self):
        return self.produto


class Memoria(models.Model):
    produto = models.CharField("Produto", max_length=50)
    def __str__(self):
        return self.produto


class PlacaDeVideo(models.Model):
    produto = models.CharField("Produto", max_length=50)
    def __str__(self):
        return self.produto
    


	