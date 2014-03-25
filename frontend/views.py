#-*- encoding: -utf-8-*-

from django.shortcuts import render, HttpResponseRedirect
#agrego los siguientes:
from django.shortcuts import render_to_response, RequestContext
from .forms import ComentarioForm
from django.contrib import messages


# Create your views here.
def home(request):
	print "holo"

	return render_to_response("home.html",
								 locals(),
				 					context_instance=RequestContext(request))

def aboutus(request):
	print "acerca de"
	return render_to_response("aboutus.html",
									 locals(),
					 					context_instance=RequestContext(request))

def coment(request):
	form= ComentarioForm(request.POST or None) # Valores de la Forma
	
	print request.POST.get('nombre')

	if form.is_valid():
		save_it= form.save(commit=False)
		save_it.save()
		return  HttpResponseRedirect('/gracias')

	return render_to_response("comentario.html",
								 locals(),
				 					context_instance=RequestContext(request))


def gracias(request):
	print "gracias"
	return render_to_response("gracias.html",
									 locals(),
					 					context_instance=RequestContext(request))