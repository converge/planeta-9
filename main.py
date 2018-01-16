from actor import Actor
from missions.mission import Mission
from colorama import Fore, Back, Style
import os
from time import sleep

# create Adiv character
adiv = Actor(name='Adiv',
             age=21,
             strenght=10,
             wisdom=5,
             tech_skills=20)

initial_story = ('Em 2021 Júpiter, um planeta 300 anos mais avançado do que a'
                 ' Terra, após uma reunião do Comando Estelar, recebeu a '
                 ' missão de preparar um planeta p/ receber a cada 360 dias, '
                 '10 dos homens e mulheres que mais contribuíram p/ o avanço '
                 'do Planeta Terra. \n\nO planeta escolhido para receber esta '
                 'nova população chama-se Planeta 9, e apresenta condições '
                 'atmosféricas parecidas com as encontradas na terra, assim '
                 'os novos habitantes não precisarão de grandes mudanças p/ '
                 'se adaptar.\n\nPara esta missão foram designados 7 '
                 'cientistas, dentre eles está Adiv chefe espacial com '
                 'poderes especiais, que tem a missão de viajar até o Planeta '
                 'Terra e transportar os 10 novos habitantes p/ o Planeta 9.')

first_mission = Mission(difficulty=1,
                        planet_name='Júpiter',
                        planet_density=10,
                        planet_population=10,
                        story=initial_story)

os.system('clear')


def menu():
    # menu
    print(Back.BLACK, Fore.GREEN + '########################################')
    print(Back.BLACK, Fore.GREEN + '# PLANETA 9 (versao alpha 0.0.1)       #')
    print(Back.BLACK, Fore.GREEN + '# Desenvolvedores:                     #')
    print(Back.BLACK, Fore.GREEN + '# Joao Vanzuita <joaovanzuita@me.com>  #')
    print(Back.BLACK, Fore.GREEN + '# Paulo Vanzuita <pvanzuita@gmail.com> #')
    print(Back.BLACK, Fore.GREEN + '########################################')
    print(Back.BLACK, Fore.GREEN + '#                                      #')
    print(Back.BLACK, Fore.GREEN + '# 1 - Iniciar                          #')
    print(Back.BLACK, Fore.GREEN + '# 2 - Sair                             #')
    print(Back.BLACK, Fore.GREEN + '#                                      #')
    print(Back.BLACK, Fore.GREEN + '########################################')
    menu_opcao = int(input('Opcao: '))

    if menu_opcao == 1:
        os.system('clear')
        print(Back.BLUE + Fore.WHITE + first_mission.get_story())
    elif menu_opcao == 2:
        exit()

def contagem_regressiva():
    x = 5
    print('Contagem regressiva..')
    while(x != 0):
        print(x)
        sleep(3)
        x = x - 1


def get_adiv_status():
    print(Back.BLACK, Fore.YELLOW + '\n----------------------------')
    print('| Nome: {}               |'.format(adiv.get_name()))
    print('| Idade: {}                |'.format(adiv.get_age()))
    print('| Força: {}                |'.format(adiv.get_strenght()))
    print('| Sabedoria: {}             |'.format(adiv.get_wisdom()))
    print('| Habilidades Técnicas: {} |'.format(adiv.get_tech_skills()))
    print('---------------------------')


# chama a funcao menu
menu()

get_adiv_status()

# acao 1
question = ('Adiv está se preparando para sua missão, são 9:00hrs da manhã, '
            'e a decolagem será realizada as 14:00hrs, o que ele deve fazer ?')
option_1 = '1 - descansar até o horário da decolagem'
option_2 = '2 - ir até a base fazer revisão do equipamento'
option_3 = '3 - meditar'
first_mission.step_1(question, option_1, option_2, option_3)
answer = int(input())
if answer == 1:
    adiv.set_strenght(adiv.get_strenght() + 1)
elif answer == 2:
    adiv.set_tech_skills(adiv.get_tech_skills() + 1)
elif answer == 3:
    adiv.set_wisdom(adiv.get_wisdom() + 1)

get_adiv_status()

question = ('Chegou o momento da decolagem, está tudo pronto p/ a partida.')
option_1 = '1 - Confirmar decolagem'
option_2 = '2 - Abandonar missão'
first_mission.step_2(question, option_1, option_2)
answer = int(input())
if answer == 1:
    contagem_regressiva()
elif answer == 2:
    print('Missão abandonada, retornando p/ casa...')

# quando sair, limpa cores
print(Style.RESET_ALL)
