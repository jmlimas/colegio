from django.views.generic import CreateView,ListView
from .models import Transporte,AlumnoTrasp,Conducta
from .forms import AddTransporteForm,AddAlumnoTraspForm,AddConductaForm

class AddTransporteView(CreateView):
	model = Transporte
	form_class = AddTransporteForm
	success_url = '/listransporte'

class ListTransporteView(ListView):
	context_object_name = 'trasporte'
	model = Transporte

class AddAlumTransView(CreateView):
	model = AlumnoTrasp
	form_class = AddAlumnoTraspForm
	success_url = '/'

class ListAlumTrasp(ListView):
	context_object_name = 'alumtrans'
	model = AlumnoTrasp

class AddConducta(CreateView):
	model = Conducta
	form_class = AddConductaForm
	success_url = '/listconducta'

class ListConducta(ListView):
	context_object_name = 'conducta'
	model = Conducta
 

