<<<<<<< HEAD
from django.contrib	import admin
=======

from django.contrib import admin
>>>>>>> cbcd5d25ec67dfc9ca2e41cb8aabfb315d4deffa
from Inventario.models import categoriaProducto
from Inventario.models import producto
from Inventario.models import tipoPaquete
from Inventario.models import paquete

class categoriaProductoAdmin(admin.ModelAdmin):
	list_display = ('nombre','descripcion',)
	list_filter = ('nombre','descripcion',)
	search_fields = ['nombre','descripcion']
	fields = ('nombre','descripcion',)

class productoAdmin(admin.ModelAdmin):
	list_display = ('nombre','precio','stock',)
	list_filter = ('nombre','precio','stock',)
	search_fields = ['nombre','precio','stock']
	fields = ()

class tipoPaqueteAdmin(admin.ModelAdmin):
	list_display = ('nombre','descripcion',)
	list_filter = ('nombre','descripcion',)
	search_fields = ['nombre','descripcion']
	fields = ()

class paqueteAdmin(admin.ModelAdmin):
	list_display = ('nombre','precio','stock',)
	list_filter = ('nombre','precio','stock',)
	search_fields = ['nombre','precio','stock']
	fields = ()

<<<<<<< HEAD
admin.site.register(categoriaProducto,categoriaProductoAdmin)
admin.site.register(producto,productoAdmin)
admin.site.register(tipoPaquete,tipoPaqueteAdmin)
admin.site.register(paquete,paqueteAdmin)

=======
admin.site.register(categoriaProducto)
admin.site.register(producto)
>>>>>>> cbcd5d25ec67dfc9ca2e41cb8aabfb315d4deffa