import random

class drink:

    def __init__(self, name, temperature, size_ml, state, type_of_milk):
        self.name = name
        temperature = int
        size_ml = int
        state = ''
        type_og_milk = ''
        

        

class water(drink):
    def __init__(self):
        self.temperature = 40
        self.size_ml = 150
        self.state = 'liquid'

    def frozen(self):
        self.size_ml = 100
        self.temperature = -10
        self.state = 'ice'
    

class coffee(drink):
    def __init__(self):
        self.temperature = 80
        self.size_ml = 50

        
    

class milk(drink):
    def __init__(self):
        self.type_of_milk = 'cow'
        self.temperature = 32
        self.size_ml = 200
        self.state = 'liquid'

    def soy(self):
        self.type_of_milk = 'soy'
        
    def almond(self):
        self.type_of_milk = 'almond'
        
    def ants(self):
        self.type_of_milk = 'ants'

    def condenced(self):
        self.type_of_milk = 'condenced'
    
    def for_latte(self):
        self.temperature = 70
        self.state = 'frothy'
        
class vietnamese(coffee):
    def make_it(self):
        add_1 = milk()
        add_1.condenced()
        add_2 = water()
        add_2.frozen()
        self.temperature = (self.temperature + add_1.temperature + add_2.temperature)/3
        self.size_ml += (add_1.size_ml + addd_2.size_ml)    
    
    

class latte(coffee):
     def make_it(self):
        add = milk.for_latte() 
        self.temperature = 0.5*(self.temperature + add.temperature)
        self.size_ml += add.size_ml

    
class espresso(coffee):
    
    pass
    
    

class americano(coffee):
     def make_it(self):
        add = water()
        self.temperature = 0.5*(self.temperature + add.temperature)
        self.size_ml += add.size_ml
    
 
class barista:

    def help_in_ordering(self):
        #использую полиморфизм, можно было бы ещё с типами молока доработать, но я устала, если нужно для полный картины - доработаю))
        print(random.choice(['How are you doing?', 'What a lovely weather we\'re having!']))
        drink = input('What would you like to drink? (type water, coffee or milk)')
        
        if drink == 'coffee':
            if input('With milk? (type yes or no)') == 'yes':
                if input('Condenced? (type yes or no)') == 'yes':
                    self.drink_ordered = vietnamese()
                else:
                    self.drink_ordered = latte()
            else:
                drink = input('Espresso or Americano? (type espresso or americano)')    
                if drink ==  'expresso':
                    print('Go away')
                    
                if drink == 'espresso':
                    self.drink_ordered = espresso()

                if drink == 'americano':
                    self.drink_ordered = americano()

        elif drink == 'milk':
            self.drink_ordered = milk()

        elif drink == 'water':
            self.drink_ordered = water()

        else:
            self.drink_ordered = None

        return self.drink_ordered
    
a = barista()
drink_you_wanted = a.help_in_ordering()
if drink_you_wanted != None:
    print(drink_you_wanted.temperature) #вместо температуры можно набрать любой другой, просто чтобы проверить объект атрибут
