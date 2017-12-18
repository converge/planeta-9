from actor import Actor
from missions.mission import Mission
import pyglet

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
                 'do Planeta Terra. O planeta escolhido para receber esta '
                 'nova população chama-se Planeta 9, e apresenta condições '
                 'atmosféricas parecidas com as encontradas na terra, assim '
                 'os novos habitantes não precisarão de grandes mudanças p/ '
                 'se adaptar. Para esta missão foram designados 7 cientistas, '
                 'dentre eles está Adiv chefe espacial com poderes especiais, '
                 'que tem a missão de viajar até o Planeta Terra e '
                 'transportar os 10 novos habitantes p/ o Planeta 9.')

first_mission = Mission(difficulty=1,
                        planet_name='Júpiter',
                        planet_density=10,
                        planet_population=10,
                        story=initial_story)


window = pyglet.window.Window()

label = pyglet.text.Label(first_mission.get_story()[:80],
                          font_name='Verdana',
                          font_size=14,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

label2 = pyglet.text.Label('teste',
                           font_name='Times New Roman',
                           font_size=10,
                           x=window.width//3, y=window.height//3,
                           anchor_x='center', anchor_y='center')


@window.event
def on_draw():
    window.clear()
    label.draw()
    label2.draw()


pyglet.app.run()
