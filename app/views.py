from django.shortcuts import render
from django.http import HttpResponse

from django.db.models import Q
from service.forms import FormFilterSelect
from service.models import RealState,galeryService
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

'''
# esta funcion va a hacer el query
def get_bienRaiz_queryset(query=None):
	queryset = []    
	queries = query 

	posts = BienRaiz.objects.filter(Q(region=queries[1]) & Q(type_p=queries[2]) & Q(operation=queries[3]) 
        ).distinct()

	for post in posts:
		queryset.append(post)

	return list(set(queryset))
'''

'''
class HomeView(View):
    def get(self,request):
        print(request.GET)
        form = CreateBienForm(request.GET)
        if form.is_valid():
            if form.cleaned_data['status'] == 'todo' and form.cleaned_data['region'] == 'todo':
                data = BienRaiz.objects.all() # generar una consulta mostrando los mas cercano con respecto al tiempo
            else:
                #data = BienRaiz.objects.filter()        
'''

from django.views import View

from django.views.generic import TemplateView
from django.http import JsonResponse    
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from service.models import Region,City


#@method_decorator(login_required)

class TestView(TemplateView):
    template_name = 'home.html'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        print(request.POST) 
        try:
            action = request.POST['action']
            if action == 'search_product_id':
                data = []
                for i in City.objects.filter(region__id=request.POST['id']):
                    data.append({'id': i.id, 'name': i.name})
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
            print(str(e))
        return JsonResponse(data, safe=False)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FormFilterSelect()
        return context 


class HomeViewRequest(View):
    #@method_decorator(login_required)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        action = request.POST.get('action')
        if action == 'search_product_id':
            data = []
            for i in City.objects.filter(region__id=request.POST['id']):
                data.append({'id': i.id, 'name': i.name})
        elif request.POST.get('status'):
            real_state = RealState.objects.filter(status=request.POST.get('status'),region__id=int(request.POST.get('region')),city__id=int(request.POST.get('city')))
            print(real_state)
            context = {'realState': real_state}
            return render(request,"search.html",context)
        else:
            data['error'] = 'Ha ocurrido un error'
 
        return JsonResponse(data, safe=False)
    
    
    def get(self,request):
        template_name = "home.html"
        context = {
            'form': FormFilterSelect(),
            'recomended': "re",
            'favorite': RealState.objects.filter(favorite=True)
        }
        return render(request,template_name,context)





class HomeView(View):
    def post(self,request):
        print("mandando un post")
        context = {}
        form = FormFilterSelect(request.POST)
        if form.is_valid():
            if int(form.cleaned_data['region']) == 0 and int(form.cleaned_data['city']) == 0 and int(form.cleaned_data['status']) ==0:
                bien_raiz = RealState.objects.all()
            elif form.cleaned_data['search']:
                bien_raiz = RealState.objects.get(code=form.cleaned_data['search'])
            else:
                bien_raiz = RealState.objects.all().filter(
                    region=form.cleaned_data['region'],
                    city=form.cleaned_data['city'],
                    status=form.cleaned_data['status']
                )
            context['servicios'] = bien_raiz
        return render(request,'search.html',context)

        # redireccionamos a un a vista definida de error en e formulario
        
    def get(self,request):
        print("mandand un get")
        context = {}
        template_name = 'home.html'
        form = FormFilterSelect()
        bien_raiz = RealState.objects.all()

        context['form'] = form    
        context['servicios'] = bien_raiz
        return render(request,template_name,context)


# aqui vamos a implementar le query
@csrf_exempt
def home_page(request):
    context = {}
    form = FormFilterSelect()  
    if request.GET:
        form = FormFilterSelect(request.GET)       
        if form.is_valid():
            if int(form.cleaned_data['region']) == 0 and int(form.cleaned_data['city']) == 0 and int(form.cleaned_data['status']) ==0:
                bien_raiz = RealState.objects.all()
            elif form.cleaned_data['search']:
                bien_raiz = RealState.objects.get(code=form.cleaned_data['search'])
            else:
                bien_raiz = RealState.objects.all().filter(
                    region=form.cleaned_data['region'],
                    city=form.cleaned_data['city'],
                    status=form.cleaned_data['status']
                )
            context['servicios'] = bien_raiz

        context['form'] = form
        return render(request,'search.html',context)
        
    bien_raiz = RealState.objects.all()

    context['form'] = form    
    context['servicios'] = bien_raiz
    return render(request,'home.html',context)



def nosotros_page(request):
    return render(request,'nosotros.html',{})

def servicios_page(request):
    return render(request,'servicios.html',{})


from .forms import CreateClientForm
from django.core.mail import send_mail,BadHeaderError,EmailMultiAlternatives
from decouple import config
from django.conf import settings
from django.template.loader import get_template
from django.http import HttpResponse



def contacto_page(request):
    form = CreateClientForm()
    context = {}

    if request.method == 'POST':
        form = CreateClientForm(request.POST)
        if form.is_valid():
            form.save()
            
            config_email_destino = config('USER_MAIL_USER_DES')
            send_email_function(config_email_destino,form)

    context['form'] = form
    return render(request,'contacto.html',{'form':form})



def venta_page(request):
    context = {} 
    servicio = RealState.objects.filter(is_vent = True,)
    context['servicios'] = servicio
    return render(request,'venta.html',context)


def arriendo_page(request):
    context = {} 
    servicio = RealState.objects.filter(is_vent = False)
    context['servicios'] = servicio
    return render(request,'arriendo.html',context)



# configuracion de envio de correo en la pagina de la empresa
def send_email_function(mail,cliente):
    info_form = cliente.cleaned_data
    lista_Datos = [info_form['name'],info_form['phone'],info_form['email'],info_form['message']]  

    context = {'email':mail,'cliente':info_form}

    template = get_template('send/send.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'un correo de prueba',
        'Empresa',
        settings.EMAIL_HOST_USER,
        [mail],
    )
    email.attach_alternative(content,'text/html')
    email.send()



def detail_service(request,id):

    context = {}
    services = RealState.objects.get(id=id)
    context["servicio_imagen"] = galeryService.objects.filter(owner=services)
    context["servicios"] = services
    
    return render(request,'detail.html',context)

from django.views.generic import TemplateView
class TestVie(TemplateView):
    template_name = 'test.html'
    
