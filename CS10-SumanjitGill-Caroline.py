import sys
#Storyline
class Character():
    def __init__(self, name, full_name):
        self.name = name
        self.full_name = full_name
        #self.age = age
        #self.status = status
        #self.background = background
        #self.personality = personality
        #self.charisma = charisma
        
Caroline = Character('Caroline','Karolina "Caroline" Ativa')
Liam = Character('Liam','Liam Youngblood')
Gabriela = Character('Gabi','Gabriela Solis')
Andres = Character('Andres','Andres Leal')
Bree = Character('Bree','Breanna "Bree" Scholtz')
Nicole = Character('Nicole','Nicole Laurenya')
Liev = Character('Liev','Liev Ativa')
Sakshi = Character('Sakshi','Sakshi Goenka')
Leng = Character('Leng','Leng Li')

'''
class Room:
    def __init__(self, n_path, s_path, e_path, w_path, name, description):
        self.north = n_path
        self.south = s_path
        self.east = e_path
        self.west = w_path
        self.name = name
        self.description = description
        
    def move(self, direction):
        while True:
            global node
            node = globals()[getattr(self, direction)]
            break
            
while True:
    print node.name
    print node.description
    user_command = raw_input('> ')
    if user_command in ['q', 'quit', 'exit']:
        sys.exit(0)
    if user_command in ['north','south','west','east']:
        try:
            node.move(user_command)
        except:
            print 'You can\'t go that way! Try again.'
'''
            
'''class Notebook:
    def __init__(self):
        self.notebook = []
        
    def write_in_notebook(self):
        user_note = raw_input('What would you like to write in your notebook?')
        self.notebook.append(user_note)
        
    def show_entry_amount(self):
        if len(self.notebook) ==1:
            print 'You have 1 entry.'
        elif len(self.notebook) ==0:
            print 'You don\'t have any entries.'
        else:
            print 'You have', len(self.notebook),'entries.'
        
    def read_entry(self):
        for i in enumerate(self.notebook):
            print i
        user_entry_choice = raw_input('Which entry would you like to read?')
        try:
           path = [int(user_entry_choice)]
           print self.notebook[path]
        except:
            print 'Invalid Number. Try a valid number.'
            
your_notebook = Notebook()
#4691 E Harvard Ave Fresno, CA 93703-2075
'''

class Dialogue:
    def __init__(self, dialogue):
        self.dialogue = dialogue
        
    def say(self,char):
        print char.name+':','"'+self.dialogue+'"'
        
hello = Dialogue('Hello')
        
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
#Do dialogue in order this way by continously calling the dialogue 'say' function
#Progress stories this way

        