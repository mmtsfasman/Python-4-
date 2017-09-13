import random.choice

class drink:

    def __init__(self, name, type_of_milk, temperature, size):
        self.name = name

        

class water(drink):

    def def __init__(self, temperature, size, state):
        self.name = name
        self.temperature = 40
        self.size_ml = 150
        self.state = 'liquid'

    def frozen(self):
        self.size_ml = 100
        self.temperature = -10
        self.state = 'ice'
    

class coffee(drink):

    def __init__(self, name, temperature, size_ml):
        self.name = name
        self.temperature = 80
        self.size_ml = 50

        
    

class milk(drink):

    def __init__(self, name, type_of_milk, temperature, size_ml, state):
        self.name = name
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

    def __init__(self, name):
        self.name = name
    add_1 = milk.condenced()
    add_2 = water.frozen()
    self.temperature = (self.temperature + add_1.temperature + add_2.temperature)/3
    self.size_ml += (add_1.size_ml + addd_2.size_ml)    
    
    

class latte(coffee):
    def __init__(self, name):
        self.name = name
    add = milk.for_latte() 
    self.temperature = 0.5*(self.temperature + add.temperature)
    self.size_ml += add.size_ml

    
class espresso(coffee):

    def __init__(self, name):
        self.name = name
    

class americano(coffee):

    def __init__(self, name):
        self.name = name
    add = water()
    self.temperature = 0.5*(self.temperature + add.temperature)
    self.size_ml += add.size_ml
    
 
class barista():

    def __init__(self, name):
        self.name = name

    def help_in_ordering(self):
        #использую полиморфизм, можно было бы ещё с типами молока доработать, но я устала, если нужно для полный картины - доработаю))
        print(random.choice(['How are you doing?', 'What a lovely weather we\'re having!']))
        drink = raw_input('What would you like to drink? (type water, coffee or milk)')
        
        if drink == 'coffee':
            if raw_input('With milk? (type yes or no)') = 'yes':
                if raw_input('Condenced? (type yes or no)') = 'yes':
                    drink_ordered = vietnamese()
                else:
                    drink_ordered = latte()
            else:
                drink = raw_input('Espresso or Americano? (type espresso or americano)')    
                if drink ==  'expresso':
                    print('Go away')
                    
                if drink == 'espresso':
                    drink_ordered = espresso()

                if drink == 'americano':
                     drink_ordered = americano()

        elif drink == 'milk':
            drink_ordered = milk()

        elif drink == 'water':
            drink_ordered = water()

        else:
            drink_ordered = None

        return drink_ordered


        
            


        
                    
    
        
        


    
    
