class Actor():
    name = None
    age = None
    strenght = None
    wisdom = None
    tech_skills = None

    def __init__(self, name, age, strenght, wisdom, tech_skills):
        self.name = name
        self.age = age
        self.strenght = strenght
        self.wisdom = wisdom
        self.tech_skills = tech_skills

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_strenght(self):
        return self.strenght

    def get_wisdom(self):
        return self.wisdom

    def get_tech_skills(self):
        return self.tech_skills

    def set_wisdom(self, wisdom_value):
        self.wisdom = wisdom_value

    def set_tech_skills(self, tech_skills_value):
        self.tech_skills = tech_skills_value

    def set_strenght(self, strenght_value):
        self.strenght = strenght_value
