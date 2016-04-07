import sys
import random

class Inventory:
    def __init__(self):
        self.inventory = []
        self.inventory_two = []
        
    #def view inventory (inventory_two)
    def view_inventory(self):
        print self.inventory_two
    #def examine item (inventory)
    def examine_item(self, obj):
        if obj not in self.inventory:
            print 'You can\'t examine this object because it is not in your\
            inventory. Try an object you have.'
        else:
            print obj.name
            print obj.description
    
user_inventory = Inventory()

#-------------------------------------------------------------------------------
    
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def examine(self):
        print self.name
        print self.description
        
    def pick_up(self, Inventory):
        Inventory.inventory.append(Item)
        Inventory.inventory_two.append(self.name)
        print 'You have picked up: %s.' %self.name
        
    def give_item(self):
        Inventory.inventory.remove(Item)
        Inventory.inventory_two.remove(self.name)

axe = Item('Axe', 'Pointy')

#-------------------------------------------------------------------------------

#Storyline
class Character():
    def __init__(self, name, full_name, age, status, background, location):
        self.name = name
        self.full_name = full_name
        self.age = age
        self.status = status
        self.background = background
        self.location = location
        
    def stats(self):
        print self.full_name
        print self.age
        print self.status
        print self.background
        
    def locate(character):
        print character.name+ 'is located in: %s' %character.location
        
#Caroline = Character('Caroline','Karolina "Caroline" Ativa', 22, 'Alive', '', 'You are her... So wherever you are that\'s where she is.')
#Liam = Character('Liam','Liam Youngblood', 23, 'Alive', '', 'He\'s always by your side.')
#Gabriela = Character('Gabi','Gabriela Solis',18, 'Alive', '', 'She\'s found in the lab at the police office.')
#Andres = Character('Andres','Andres Leal', 30, 'Alive; Suspect', '', 'He\'s found in the garden.')
#Bree = Character('Bree','Breanna "Bree" Scholtz', 35, 'Alive; Suspect', 'She works as Leng\'s maid around the mansion.', 'She\'s found in the living room.')
#Nicole = Character('Nicole','Nicole Laurenya', 31, 'Dead; Victim', 'She was a rich heiress of Twilight Grove.', 'Her corpse is found in her bedroom.')
#Liev = Character('Liev','Liev Ativa', 45, 'Alive', 'He is your father and the police chief who assigned you to this investigation.', 'He is found in the police office.')
#Sakshi = Character('Sakshi','Sakshi Goenka', 32, 'Alive; Suspect','Sakshi is a business tycoon and is Leng\'s girlfriend.', 'She is found in the study.')
#Leng = Character('Leng','Leng Li', 33, 'Alive; Suspect', 'He is a renowned chef and is Sakshi\'s lover.', 'He is found in the kitchen.')

#-------------------------------------------------------------------------------

#def help():
#    user_q = raw_input('What do you need help with?\n')

#-------------------------------------------------------------------------------
           
#For Version 2: 
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

#-------------------------------------------------------------------------------

class Dialogue:
    def __init__(self, dialogue):
        self.dialogue = dialogue
        
    def say(self,char):
        print char.name+':','"'+self.dialogue+'"'
        
hello = Dialogue('Hello')

#-------------------------------------------------------------------------------

#Rooms

#Have three parameters in __init__ for the item name
#Refer to it as you did with dialogue
        
class Room:
    def __init__(self, name, description, item, item_two, item_three):
        self.name = name
        self.description = description
        self.item = item
        self.item_two = item_two
        self.item_three = item_three
        
    def see_item(self, cosa):
        print cosa.description
            
police_office = Room('Police Chief Ativa\'s Office', 'This office.', None, None, None)
study = Room('The Study', 'This study.', None, None, None)
garden = Room('Garden', 'This garden.', None, None, None)
living_room = Room('Living Room', 'This room.', None, None, None)
kitchen = Room('Kitchen', 'This kitchen.', None, None, None)
bedroom = Room('Nicole\'s Bedroom', 'This is the crime scene.', None, None, None)
lab = Room('Gabi\'s Room', 'This lab.', None, None, None)
front_yard = Room('Front Yard', 'This front yard.', None, None, None)

global node 
node = living_room           
'''                                
while True:
    print node.name
    print node.description
    user_command = raw_input('> ')
    if user_command in ['q', 'quit', 'exit']:
        sys.exit(0)
    elif user_command == 'police office':
        node = police_office
    elif user_command == 'study':
        node = study
    elif user_command == 'garden':
        node = garden
    elif user_command == 'living room':
        node = living_room
    elif user_command == 'kitchen':
        node = kitchen
    elif user_command == 'bedroom':
        node = bedroom
    elif user_command == 'lab':
        node = lab
    elif user_command == 'front yard':
        node = front_yard
    '''
bathroom = Room('Bathroom', 'This is where you shower and excrete your junk.', axe, None, None)

#-------------------------------------------------------------------------------
        
#Do dialogue in order this by continously calling the dialogue 'say' function
#Progress stories this way

'''while True:
    user_response = raw_input('> ')
    if user_response in ['q','quit','exit']:
        sys.exit(0)
        '''
        
#Win Conditions as a class to make sure that the person accomplished everything 
#before winning
#Series of red flags/conditionals to make sure that the tasks are completed        
        


#Hangman

#Numerical Riddle (1982)

#Riddle

#Hangman

#Riddle

#Numerical Riddle (Passcode = (0129))
    #- Tells you which digits you got correct and which you didn't
    #- 
    
#-------------------------------------------------------------------------------
    
'''
#Setting up variables to be called on later
life = 5
bank = ["zero one twenty nine"]
word = random.choice(bank)

letters_left = list(set(word)) #creating a list of letters in word
if ' ' in word:
    letters_left.remove(' ') #removing the space if there is one
            

user_guesses = [] #More variables
wrong_answers = 0
hidden_phrase = []
foo = list(word) 

print ("You have five chances right now.")

while life > 0: #The dreaded while loop
    


    for letter in word:    
        hidden_phrase = [] 
        if letter in user_guesses:
            print letter,
        elif letter == ' ':
            print letter,
        else:
            print ('_'),
            
            
    current_guess = raw_input("Guess a letter: ") #This takes in raw input
    user_guesses.append(current_guess)
    if current_guess in word: #If guess in word, remove from letters_left
        letters_left.remove(current_guess)              
        #print letters_left
    print user_guesses #Prints guesses so far
    if current_guess not in word: #If you guess incorrectly
        life -= 1
        wrong_answers += 1
        print ("Your life count: ") + str(life)
            
    if len(letters_left) == 0:
        gaby.say()
        '''