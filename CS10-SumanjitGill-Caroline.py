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
        print self.personality
        
    def locate(character):
        print character.name+ 'is located in: %s' %character.location
        
#Caroline = Character('Caroline','Karolina "Caroline" Ativa')
#Liam = Character('Liam','Liam Youngblood')
#Gabriela = Character('Gabi','Gabriela Solis')
#Andres = Character('Andres','Andres Leal')
#Bree = Character('Bree','Breanna "Bree" Scholtz')
#Nicole = Character('Nicole','Nicole Laurenya')
#Liev = Character('Liev','Liev Ativa')
#Sakshi = Character('Sakshi','Sakshi Goenka')
#Leng = Character('Leng','Leng Li')

#def help():
#    user_q = raw_input('What do you need help with?\n')
            
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
        
    def move(self, room):
        while True:
            global node
            node = globals()[getattr(self, room)]
            break
 
node = living_room           
                                  
while True:
    print node.name
    print node.description
    user_command = raw_input('> ')
    if user_command in ['q', 'quit', 'exit']:
        sys.exit(0)
    if user_command in ['office','study','garden','living', 'kitchen', 'bedroom', 'lab']:
        try:
            node.move(user_command)
        except:
            print 'You can\'t go there! Try again.'
            
#police_office
#study
#garden
#living_room
#kitchen
#bedroom
#lab
        
bathroom = Room('Bathroom', 'This is where you shower and excrete your junk.', axe, None, None)
        
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
'''
#Setting up variables to be called on later
life = 5
bank = ["illuminati confirmed", "slenderman", "guess", "password", "luigi", "king boo", "kevin", "caaaaaarl", "john cena"]
word = random.choice(bank)

letters_left = list(set(word)) #creating a list of letters in word
if ' ' in word:
    letters_left.remove(' ') #removing the space if there is one
            

user_guesses = [] #More variables
wrong_answers = 0
hidden_phrase = []
foo = list(word) 

print ("You currently have 5 lives. Try not to waste them.")

while life > 0: #The dreaded while loop
    


    for letter in word:     #This is replacing every letter in the word with a pound symbol
        hidden_phrase = []  #If the letter is guessed, it is replaced by the correct letter
        if letter in user_guesses:  #Else, it remains a hastag
            print letter,
        elif letter == ' ':
            print letter,
        else:
            print ('#'),
            
            
    current_guess = raw_input("Guess a letter: ") #This takes in raw input
    user_guesses.append(current_guess)
    if current_guess in word: #If guess in word, remove from letters_left
        letters_left.remove(current_guess)              
        #print letters_left
    print user_guesses #Prints guesses so far
    if current_guess not in word: #If you guess wrong, lose life energy
        life -= 1
        wrong_answers += 1
        print ("Oh, how sad. Lost a life. You have ") + str(life) + (" lives.")
    


    
            
    if len(letters_left) == 0:
        print ("You've won! Don't you feel proud to actually accomplish something?")
        break #Win if the letter_left has nothing in the list
        
        '''