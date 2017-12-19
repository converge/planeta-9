class Mission():

    difficulty = None
    planet_name = None
    planet_density = None
    planet_population = None
    story = None

    def __init__(self,
                 difficulty,
                 planet_name,
                 planet_density,
                 planet_population,
                 story):
        self.difficulty = difficulty
        self.planet_name = planet_name
        self.planet_density = planet_density
        self.planet_population = planet_population
        self.story = story

    def get_story(self):
        return self.story

    def step_1(self,
               question,
               option_1,
               option_2,
               option_3):

        print(question)
        print(option_1)
        print(option_2)
        print(option_3)

