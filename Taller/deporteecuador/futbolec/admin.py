from django.contrib import admin
from futbolec.models import Equipof, Jugador, Campeonato, Campeonato_equipo

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'siglas', 'tusername')
    search_fields = ('nombre', 'siglas')

admin.site.register(Equipof, EquipoAdmin)

class JugadorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'posicion', 'camiseta', 'sueldo', 'equipo')
    search_fields = ('nombre', 'camiseta')

admin.site.register(Jugador, JugadorAdmin)

class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombreausp')
    search_fields = ('nombre',)

admin.site.register(Campeonato, CampeonatoAdmin)

class Campeonato_equipoAdmin(admin.ModelAdmin):
    list_display = ('equipo', 'campeonato', 'anio')
    search_fields = ('equipo', 'campeonato')

admin.site.register(Campeonato_equipo, Campeonato_equipoAdmin)
