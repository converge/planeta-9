class Actor():
    name = None
    age = None
    strenght = None
    wisdom = None
    tech_skill = None

    def __init__(self, name, age, strenght, wisdom, tech_skill):
        self.name = name
        self.age = age
        self.strenght = strenght
        self.wisdom = wisdom
        self.tech_skill = tech_skill

    def get_name(self):
        return self.name
