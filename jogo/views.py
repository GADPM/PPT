from django.shortcuts import render
import random

def menu_inicial(request):
    """Página inicial do menu do jogo"""
    return render(request, 'jogo/menu_inicial.html')

def historia(request):
    """Página de história do jogo"""
    return render(request, 'jogo/historia.html')

def creditos(request):
    """Página de créditos"""
    return render(request, 'jogo/creditos.html')

# Função para gerar a escolha do computador
def computador_escolhe():
    return random.choice(['pedra', 'papel', 'tesoura'])

# Função para exibir a página onde o usuário escolhe a jogada
def index(request):
    return render(request, 'jogo/index.html')  # Renderiza a página de seleção de jogada

# Função para processar a escolha do usuário e gerar o resultado
def jogar(request):
    escolha_usuario = request.GET.get('escolha')  # Obtém a escolha do usuário
    escolha_computador = computador_escolhe()  # Gera a escolha do computador

    # Lógica para determinar o resultado
    resultado = ""
    if escolha_usuario == escolha_computador:
        resultado = "Empate!"
    elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
         (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
        resultado = "Você venceu!"
    else:
        resultado = "Você perdeu!"

    return render(request, 'jogo/jogar.html', {
        'resultado': resultado,
        'escolha_usuario': escolha_usuario,
        'escolha_computador': escolha_computador
    })