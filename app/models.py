from django.db import models

# Create your models here.

class motos(models.Model):
    # seguir os modelos das colunas 
    #               <th scope="col">Modelo</th>
    #             <th scope="col">Marca</th>
    #             <th scope="col">Preço</th>
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=150)
    preço = models.IntegerField(max_length=150)
