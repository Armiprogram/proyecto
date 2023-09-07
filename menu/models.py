from django.db import models

# Create your models here.
class Menu(models.Model):
    tittle=models.CharField(max_length=100, verbose_name="Título")
    content=models.TextField(verbose_name="Contenido")
    image=models.ImageField(verbose_name="Imagen", upload_to="menu")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    
    class Meta:
        verbose_name="Menu"
        verbose_name_plural="Menus"
        ordering=["-created"]
    
    def __str__(self):
        return self.tittle