from django.db import models

from django.db.models.signals import pre_save,post_delete
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver



class Region(models.Model):
    name = models.CharField(max_length=300,verbose_name='Nombre')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regiones'
        ordering = ['id']
        
class City(models.Model):
    name = models.CharField(max_length=300,verbose_name='Ciudad')
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ['id']



def upload_location(instance, filename):
	file_path = 'Servicio{owner_id}/Bien{bienid}/{filename}'.format(
				owner_id=str(instance.owner.author.pk),bienid=str(instance.owner.title), filename=filename)
	return file_path

    

def upload_location2(instance, filename):
	file_path = 'Servicio{owner_id}/Bien{bienow}/{title}-{filename}'.format(
				owner_id=str(instance.author.id),bienow=str(instance.title),title=str(instance.title), filename=filename)
	return file_path


    
class RealState(models.Model):

    TYPE_STATUS = [
        ("Venta","Venta"),
        ("Arriendo","Arriendo"),
    ]

    title               = models.CharField(max_length=50, null=False, blank=False)
    description         = models.TextField(max_length=5000, null=False, blank=False)
    date_published      = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    date_updated        = models.DateTimeField(auto_now=True, verbose_name="date updated")
    price               = models.CharField(max_length=20,null=False, blank=False)                        # precio
    common_expenses     = models.IntegerField(null=True, blank=True)                                     # gastos comunes

    m2_construction         = models.IntegerField()                                     # metros cuadrados construccion
    m2_terrain              = models.IntegerField()                                     # metros cadrados terreno
    height                  = models.FloatField()                                       # alto
    width                   = models.FloatField()                                       # ancho
    n_bath                  = models.IntegerField()                                     # numero de baños
    n_room                  = models.IntegerField()                                     # numero habitaciones
    n_parking               = models.IntegerField()                                     # numero de estacionamiento
    n_flat                  = models.IntegerField()                                     # numero de pisos 
    country                 = models.CharField(max_length=50,null=False, blank=False)   # pais
    town                    = models.CharField(max_length=50,null=False, blank=False)   # ciudad
    sector                  = models.CharField(max_length=50,null=False, blank=False)   # sector
    
    is_vent                 = models.BooleanField(default=False)
    favorite                = models.BooleanField(default=False)

    # definicion de formulario de busqueda    
    region                  = models.ForeignKey(Region,on_delete=models.CASCADE)
    city                    = models.ForeignKey(City,on_delete=models.CASCADE) 
    status                  = models.CharField(max_length=50,null=False,blank=False,choices=TYPE_STATUS,default = "No seleccionado") 


    # definimos el usuario y el cosigo de servicio
    author                  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # usuario
    img_principal           = models.ImageField(upload_to=upload_location2, null=True, blank=True)
    
    
    # este es el codigo de busqueda de propiedad
    code                    = models.IntegerField(unique=True)
     
    def __str__(self):
        return self.title + "  Codigo: " + str(self.code)

class galeryService(models.Model):
    image		 			= models.ImageField(upload_to=upload_location, null=True, blank=True)
    owner 					= models.ForeignKey(RealState, on_delete=models.CASCADE)
    slug                    = models.SlugField(blank=True, unique=True)



# esto esta bien definido(*)
@receiver(post_delete, sender=galeryService)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False) 

def pre_save_service_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.owner.author.username + "-" + str(instance.id))

pre_save.connect(pre_save_service_receiver, sender=galeryService)


