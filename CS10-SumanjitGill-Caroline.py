import sys
#Storyline
class Character():
    def __init__(self, name, age, status, background, personality, charisma, intelligence, strength):
        self.name = name
        self.age = age
        self.status = status
        self.background = background
        self.personality = personality
        self.charisma = charisma
        
Caroline = ('Karolina "Caroline" Ativa')
Liam = ('Liam Youngblood')
Gabriela = ('Gabriela Solis')
EP = ('Estevan Antonov')
Bri = ('Brianna Scholtz')
Ana = ('Analiese Hanz')
Queen_Laurenya = ('Nicole Laurenya')
Liev = ('Liev Ativa')
Ziva = ('Ziva Antonov')
Arnav = ('Arnav Srivastva')

node = None

class Room:
    def __init__(self, n_path, s_path, e_path, w_path, name, description):
        self.north = n_path
        self.south = s_path
        self.east = e_path
        self.west = w_path
        self.name = name
        self.description = description
        
    def move(self, direction):
        if direction in ['q', 'quit', 'exit']:
            sys.exit(0)
        while True:
            global node
            node = globals()[getattr(self, direction)]
            break
            
while True:
    print node.name
    print node.description
    user_command = raw_input('> ')
    if user_command in ['north','south','west','east']:
        try:
            node.move(user_command)
        except:
            print 'You can\'t go that way! Try again.'