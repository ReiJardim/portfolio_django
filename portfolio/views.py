from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .dados import habilidades, projetos, experiencias, formacoes

def home(request):
    """
    View para renderizar a página inicial com informações sobre o profissional,
    habilidades em destaque e projetos recentes.
    """
    # Pegar apenas projetos em destaque para a página inicial
    projetos_destaque = {k: v for k, v in projetos.items() if v.get('destaque', False)}
    
    context = {
        'habilidades': habilidades,
        'projetos': projetos_destaque,
        'experiencias': experiencias,
        'formacoes': formacoes,
    }
    
    return render(request, 'home.html', context)


def lista_projetos(request):
    """
    View para listar todos os projetos com opções de filtragem por categoria
    """
    # Opcionalmente, poderia ordenar por data ou destaque
    # projetos_ordenados = dict(sorted(projetos.items(), key=lambda x: x[1].get('data', ''), reverse=True))
    
    context = {
        'projetos': projetos
    }
    
    return render(request, 'projetos.html', context)


def detalhes_projeto(request, id_projeto):
    """
    View para mostrar detalhes completos de um projeto específico
    """
    projeto = projetos.get(id_projeto)
    
    if not projeto:
        raise Http404("Projeto não encontrado")
    
    # Encontrar projetos relacionados com a mesma categoria
    categoria = projeto.get('categoria', '')
    projetos_relacionados = {k: v for k, v in projetos.items() 
                            if v.get('categoria') == categoria and k != id_projeto}
    
    context = {
        'projeto': projeto,
        'id_projeto': id_projeto,
        'projetos': projetos,  # Para mostrar relacionados
        'projetos_relacionados': projetos_relacionados
    }
    
    return render(request, 'detalhes_projeto.html', context)


def sobre(request):
    """
    View para mostrar informações detalhadas sobre o profissional,
    incluindo formação acadêmica e experiência profissional
    """
    context = {
        'experiencias': experiencias,
        'formacoes': formacoes,
        'habilidades': habilidades
    }
    
    return render(request, 'sobre.html', context)


def contato(request):
    """
    View para exibir informações de contato e formulário
    """
    mensagem = None
    
    if request.method == 'POST':
        # Aqui poderíamos processar o formulário e enviar email
        # Por enquanto, apenas retornamos uma mensagem de sucesso
        mensagem = {
            'tipo': 'sucesso',
            'texto': 'Sua mensagem foi enviada com sucesso! Entrarei em contato em breve.'
        }
        
    context = {
        'mensagem': mensagem
    }
    
    return render(request, 'contato.html', context)
