from django.db import models 
import uuid 

# Create your models here.


class State(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    state = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.state)
    
    class Meta:
        ordering = ['state']


class Person(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    nome = models.CharField(max_length=20)
    sobrenome = models.CharField(blank=True, null=True, max_length=30)
    state = models.ForeignKey(State, blank=True, null=True, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.nome)