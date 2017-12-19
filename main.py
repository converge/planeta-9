from actor import Actor
from missions.mission import Mission
from colorama import Fore, Back, Style
import os

# create Adiv character
adiv = Actor(name='Adiv',
             age=21,
             strenght=10,
             wisdom=5,
             tech_skill=20)

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
    print(Back.BLUE + Fore.WHITE + first_mission.get_story())
    print(Style.RESET_ALL)
    

print(Style.RESET_ALL)