from django.http import HttpResponse
from django.shortcuts import render #pega template retorna response

def hello(request):
    return render(request, 'index.html')


def ano(request, year):#converte pq veio como int
    return HttpResponse('Ano '+ str(year))


def buscar_pessoa(nome):

    pessoas = [
        {'nome':'Nome1', 'idade':11, 'vivo': True},
        {'nome':'Nome2', 'idade':22, 'vivo': False},
        {'nome':'Nome3', 'idade':33, 'vivo': True}
    ]

    for pessoa in pessoas:
        if pessoa['nome'] == nome:
            return pessoa
    
    return {'nome':':(', 'idade':0}

    
def fname2(request, nome):

    p= buscar_pessoa(nome) 
    return render(request, 'pessoa.html', {'v_nome':p['nome'], 'v_idade':p['idade']})

