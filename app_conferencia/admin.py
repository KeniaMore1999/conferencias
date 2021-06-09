from django.contrib import admin
from app_conferencia.models import Conferencia, Conferencista, Participante

# Register your models here.

class ConferenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha', 'hora', 'Conferencista')
    list_editable = ('nombre', 'Conferencista')

admin.site.register(Conferencia, ConferenciaAdmin)
admin.site.register(Conferencista)
admin.site.register(Participante)