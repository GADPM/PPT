# PPT_app/views.py
from django.shortcuts import render
import random

def menu(request):
    """
    View para exibir o menu inicial.
    Aqui você pode oferecer opções de dificuldade ou outras configurações do jogo.
    """
    return render(request, 'PPT_app/menu.html')


def winning_move(user_choice):
    """
    Função auxiliar: retorna a jogada que vence a escolha do usuário.
    """
    if user_choice == "pedra":
        return "papel"
    elif user_choice == "papel":
        return "tesoura"
    elif user_choice == "tesoura":
        return "pedra"
    return random.choice(['pedra', 'papel', 'tesoura'])


def play(request):
    """
    View para a jogabilidade do jogo.
    """
    # Lista de escolhas (sem imagens, apenas texto)
    choices = [
        {'name': 'Pedra'},
        {'name': 'Papel'},
        {'name': 'Tesoura'},
    ]
    
    context = {
        'choices': choices,
        'difficulty': request.GET.get('difficulty', 'facil'),
    }
    
    if request.method == "POST":
        user_choice = request.POST.get('choice')
        difficulty = request.POST.get('difficulty', 'facil')
        
        # Seleção da jogada do computador com base na dificuldade
        if difficulty == 'facil':
            computer_choice = random.choice(['pedra', 'papel', 'tesoura'])
        elif difficulty == 'medio':
            computer_choice = (winning_move(user_choice)
                               if random.random() < 0.5
                               else random.choice(['pedra', 'papel', 'tesoura']))
        elif difficulty == 'dificil':
            computer_choice = winning_move(user_choice)
        else:
            computer_choice = random.choice(['pedra', 'papel', 'tesoura'])
        
        # Determina o resultado do jogo
        if user_choice == computer_choice:
            result = "Empate!"
        elif (user_choice == "pedra" and computer_choice == "tesoura") or \
             (user_choice == "papel" and computer_choice == "pedra") or \
             (user_choice == "tesoura" and computer_choice == "papel"):
            result = "Você ganhou!"
        else:
            result = "Você perdeu!"
        
        context.update({
            'user_choice': user_choice,
            'computer_choice': computer_choice,
            'result': result,
            'difficulty': difficulty,
        })
    
    return render(request, 'PPT_app/play.html', context)
