# Create your views here.
from  django.http  import  HttpResponse
from prueba.models import Usuario
from django.shortcuts import  render_to_response
from django.template import RequestContext
from prueba.form import  UsuarioForm

def usuario(request):

    form = UsuarioForm()
    return render_to_response('prueba/Registrar.html', {'form': form},
                              context_instance=RequestContext(request))
