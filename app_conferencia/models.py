from django.db import models

# Create your models here.

'''
    tipos de datos para los campos de los modelos 

    -Todos los campos se obtienen de models 
    ->CharField(max_lenght=25 )
    ->TextField()
    ->IntegerField()
    ->DecimalField(max_digits=10, decimal_places=2) 99.99
    ->PositiveIntegerField()
    ->SmallIntegerField()
    ->BooleanField()
    ->EmailField()
    ->ImageField(uploads_to='fotos')
    ->FileField(uploads_to='archivos')
    ->SlugField()
    
    campos para establecer relaciones entre Modelos:
    ->ForeingKey()
    ->OneToOneField()
    ->ManyToManyField()

'''
class Conferencista(models.Model):
    nombre = models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    experiencia= models.TextField()

    def __str__(self):
        return self.nombre

class Conferencia(models.Model):
    nombre = models.CharField(max_length=35)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha = models.DateField()
    hora = models.TimeField()
    Conferencista= models.ForeignKey(Conferencista, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Conferencia: {self.nombre} - Conferencista: {self.Conferencista}'


class Participante(models.Model):
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    correo = models.EmailField()
    twitter = models.CharField(max_length=35, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    