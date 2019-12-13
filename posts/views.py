from django.shortcuts import render
from .forms import PedidoForm

# Create your views here.
def home(request):
    nome = 'groger'
    # posts = {
    #     'Gabriel' : 'Narnia para projetos ágeis',
    #     'Vinicius': 'IA para comer biscoitos',
    #     'Ana Lu': 'BTS é muito bondoso',
    #     'Downtown': 'Não seja maníaco'
    # }

    lista = ['Roré', 'Generro', 'Anlu', 'DOwnT0wn']
    contexto = {
        'nome': nome,
        'lista': lista
        
    }
    return render(request, 'home.html', contexto)

def lista(request):
    return render(request, 'lista.html')


def login(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        form.save()
        context =  {
            'msg':"Pedido deu certo!"
        
        }   

        return render(request, 'login.html', context)
    context = {
        'formulario' : form
    }
    return render(request, 'login.html', context)
