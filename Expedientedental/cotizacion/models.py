from django.db import models
from altas.models import Medico,Paciente
from precios.models import PrecioServicio
from precios.models import GrupoServicio
<<<<<<< HEAD
from decimal import Decimal






class Cotizacion (models.Model):
	fecha=models.DateTimeField(auto_now_add=True)
	paciente=models.ForeignKey(Paciente)
	medico =models.ForeignKey(Medico)
	def __unicode__(self):
		return'['+str(self.fecha.day)+'/'+str(self.fecha.month)+'/'+str(self.fecha.year)+'] ' + self.paciente.nombre + self.medico.nombre
	def total (self):
		cotizaciondetails=CotizacionDetail.objects.filter(cotizacion__id__exact=self.id)
		total=0
		for cotizaciondetail in cotizaciondetails:
			total+=cotizaciondetail.cantida*cotizaciondetail.servicio.precio
		return total



class CotizacionDetail(models.Model):
	cotizacion=models.ForeignKey(Cotizacion)
	servicio=models.ForeignKey(GrupoServicio)
	cantidad = models.DecimalField(max_digits = 5, decimal_places = 2)

	def total(self):
		total=self.cantidad*self.servicio.precio
		return total




=======
from precios.models import GrupoPrecios

class Cotizacion(models.Model):
	fecha = models.DateTimeField(auto_now_add = True)
	paciente = models.ForeignKey(Paciente)
	medico = models.ForeignKey(Medico)
>>>>>>> 154c6b5070238634cd3200583e0caa7a83d57c56

	def __unicode__(self):
		return '['+str(self.fecha.day)+'/'+str(self.fecha.month)+'/'+str(self.fecha.year)+']  '+self.paciente.nombre+' '+self.paciente.apellidoPaterno
	
	def total(self):
		cotizaciondetails = CotizacionDetail.objects.filter(cotizacion__id__exact = self.id)
		total = 0
		for cotizaciondetail in cotizaciondetails:
			total += cotizaciondetail.precio
		return total

class CotizacionDetail(models.Model):
	cotizacion = models.ForeignKey(Cotizacion)
	nombreDelServicio = models.ForeignKey(PrecioServicio)
	nombreDelGrupo = models.ForeignKey(GrupoPrecios)
	precio = models.DecimalField(max_digits = 6, decimal_places = 2)
	def total(self):
		total = self.precio
		return total

	def __unicode__(self):
		datos = "%s %s"%(self.nombreDelServicio,self.nombreDelGrupo)
		return datos

	def __unicode__(self):
		precio = "%s"%(self.precio)
		return precio
