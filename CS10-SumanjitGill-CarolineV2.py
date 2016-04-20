# -*- coding: utf-8 -*-
#WARNING: GAME UNFINISHED
#More involvement in game :) ~ puzzles and more functions to search the rooms
#from _____ import *

import sys
import random
import time

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
hang = Inventory()

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

cell_phone = Item('Nicole\'s Cell Phone', 'There is a passcode on this phone but\
there must be some good evidence on here; Why not take it to Gabi?')

teacup = Item('Teacup', 'This broken cup can be taken to Gabi. Nicole drinks tea\
every morning... any ideas?')

body = Item('Nicole\'s Body', 'There are no trauma signs; Could she have been killed\
with poison?')

paperwork = Item('Financial Paperwork', 'This paperwork lets you know that Sakshi\
and Nicole were business rivals.')

#To be updated later

pic = ''

pic_2 = ''

pic_3 = ''

tea_grounds = Item('Tea Grounds', '')

morphine_capsules = Item('Morphine Capsules', '')

chair = Item('Chair', '')

pen = Item('Sakshi\'s Pen', '')

water_glass = Item('Sakshi\'s Gllass', '')

water_glass_2 = Item('','')

vase = Item('','')

fridge = Item('','')

vase_2 = Item('','')

pen_2 = Item('','')

desk = Item('','')

wrapper = Item('','')

clarinet = Item('','')

bench = Item('','')

news_clipping = Item('','')

pill_bottle = Item('','')

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
'''
        
    def locate(character):
        print character.name+ 'is located in: %s' %character.location
    '''
        
Caroline = Character('Caroline','Karolina "Caroline" Ativa', 22, 'Alive', 'Caroline is a dedicated police officer and takes her tasks seriously.', 'You are her... So wherever you are that\'s where she is.')
Liam = Character('Liam','Liam Youngblood', 23, 'Alive', 'Liam is your fellow officer and is very charasmatic and likes to make light of situations to keep your spirits up.', 'He\'s always by your side.')
Gabriela = Character('Gabi','Gabriella Solis',18, 'Alive', 'Gabi is a technology and science geek and loves to invent new things; she\'s the scientific aide to your father\'s police department.', 'She\'s found in the lab at the police office.')
Andres = Character('Andres','Andres Leal', 30, 'Alive; Suspect', 'Andres is a calm doctor who loves to play his clarinet.', 'He\'s found in the garden.')
Bree = Character('Bree','Breanna "Bree" Scholtz', 35, 'Alive; Suspect', 'She works as Leng\'s maid around the mansion.', 'She\'s found in the living room.')
Nicole = Character('Nicole','Nicole Laurenya', 31, 'Dead; Victim', 'She was a rich heiress of Twilight Grove.', 'Her corpse is found in her bedroom.')
Liev = Character('Liev','Liev Ativa', 45, 'Alive', 'He is your father and the police chief who assigned you to this investigation.', 'He is found in the police office.')
Sakshi = Character('Sakshi','Sakshi Goenka', 32, 'Alive; Suspect','Sakshi is a business tycoon and is Leng\'s girlfriend.', 'She is found in the study.')
Leng = Character('Leng','Leng Li', 33, 'Alive; Suspect', 'He is a renowned chef and is Sakshi\'s lover.', 'He is found in the kitchen.')

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

#class Dialogue:
 #   def __init__(self, dialogue):
  #      self.dialogue = dialogue
   #     
    #def say(self,char):
     #   print char.name+':','"'+self.dialogue+'"'
        
scene_1 = 'Chief: "Chief Ativa speaking. Yes, sir. Yes, sir. I understand. Yes, sir, I will make sure it is taken care of."\n\
\n\
The Chief hangs up the phone and looks at a picture with him and his daughter  (you) on the day she (you) graduated from the police academy.\n\
\n\
You are sitting outside at your desk with paperwork, you partner Liam talking your ear off.\n\
\n\
Liam: "And that\'s when I said, I don\'t care how much money he has. It\'s all about how his --" \n\
\n\
Chief: "Ativa and Youngblood, get in here."\n\
\n\
Liam: "Pants. And yes, sir! Your dad seems grumpy."\n\
\n\
You: "Probably saw your face too early in the morning."\n\
\n\
Liam: "Ouch, that hurts."\n\
\n\
You both enter the Chief\'s office."\n\
\n\
Chief: "There\'s been a highly suspicious death."\n\
\n\
Liam: "Naturally, we are the homicide division."\n\
\n\
\n\
You shoot Liam a look, fighting the urge to roll your eyes, which the Chief does do.\n\
\n\
Chief: "Youngblood, I don\'t want to hear another word until I am done briefing you. There\'s been a death in Twilight Grove."\n\
\n\
Liam whistles, getting another irritated look from the Chief. You know what Liam meant. Twilight Grove is a very affluent neighborhood.\n\
\n\
Chief: "As you can understand, it\'s a high profile case and the Mayor is concerned. The crime scene is quite isolated so it has been kept quiet. \n\
I want both of you to head the case and wrap it up. Come talk to me as soon as you\'ve solved it."\n\
\n\
You exit the Chief\'s office with Liam.\n'

chief = '\nChief: "What are you waiting for? Finish up the case!"'

gabi = '\nGabi: "No evidence, no entry, no Gabi. Come back later you lovable bozos."'

scene_2 = '\nLiam: "That is one huge—"\n\
\n\
You: "According to the case files, it belongs to a guy named Leng Li. He\'s a renowned chef."\n\
\n\
Liam: "If he\'s so rich, why can\'t he buy a trash can? There\'s so much junk around here."\n\
\n\
You: "Oh, right, the garbage strike. Did you read about how --" \n\
\n\
Liam: "No, I didn\'t. Well, I can take solace in the fact that my house is cleaner than a rich guy\'s." \n\
\n\
You: "And there\'s no dead body in yours. I hope."'

scene_3 = '\nLiam: "Pretty girl. At least she didn\'t die in the "living" room, eh?"\n\
\n\
You: "This is Nicole Laurenya, a rich heiress well-known for her social life."\n\
\n\
Liam: "Just going to ignore my joke?"\n\
\n\
You: "Yup."'

examine = '\nYou: "I don\'t see any signs of trauma and I hardly think it\'s natural causes. It could be poison…"\n\
\n\
Liam: "The killer\'s probably a woman then. Poison is usually used by women."\n\
\n\
You: "Didn\'t you say you would kill someone with cyanide if you wanted to make a clean getaway?"\n\
\n\
Liam: "I\'m special. Anyways, let\'s let the coroner take a look. Gabriella will tell us more."'

cup = '\nYou: "Gabriella can also tell us more about this."\n\
\n\
Liam: "Now I\'m thirsty."\n\
\n\
You: "You want a sip?"\n\
\n\
Liam: "Ha, ha, hilarious."'

phone = 'You: "Found something."\n\
\n\
Liam: "The victim\'s cell phone. Nice."\n\
\n\
You: "It has a passcode but I\'m sure we can figure it out later."'

sakshi_1 = 'You enter the study to see a woman sitting at the desk and writing with a fancy pen, her expression clearly upset. \n\
\n\
You: "Hello. I am Detective Ativa and this is my partner, Detective Youngblood. We need to ask you some questions. What is your name?"\n\
\n\
Woman: "I\'m Sakshi Goenka."\n\
\n\
Liam: "The business tycoon?"\n\
\n\
Sakshi: "The very same."\n\
\n\
Liam: "And how were you related to the victim?"\n\
\n\
Sakshi: "Her name was Nicole. You can at least say her name. And she was my best friend." \n\
\n\
You: "I\'m so sorry for your loss. Can you tell us what happened?"\n\
\n\
Sakshi: "I don’t know. My boyfriend, Leng, invited our friends over for a few days so we can spend some time together and…all I know is Nicole was alive last night and this morning, when she didn\'t come down for breakfast, the maid went to check on her and she was dead. Just like that. She shouldn\'t be. Nicole was the sweetest, funniest, most fun person you could know."\n\
\n\
You: "Thank you for your time. We\'ll be back later if we have more questions."'

leng_1 = '\nYou enter the kitchen to see a man pouring himself a glass of water, looking lost.\n\
\n\
You: "Hello. I am Detective Ativa and this is my partner, Detective Youngblood. We need to ask you some questions. What is your name?"\n\
\n\
Man: "My name is Leng, Leng Li." \n\
\n\
Liam: "And how were you related to the victim?"\n\
\n\
Leng: "Nicole is, was, one of my best friends. She, my girlfriend Sakshi, Andres, and I grew up together."\n\
\n\
You: "I\'m so sorry for your loss. Can you tell us what happened?"\n\
\n\
Leng: "All of us finally had some time off and so I invited everyone to stay for a few days. I was looking forward to it. I can\'t believe the nightmare it has become. Everything was so normal and nostalgic. Nicole was having a blast the entire time, we all were. This morning…we all came for breakfast but Nicole wasn\'t there. I told Bree, my maid, to call her. She screamed so loud and we all ran up there and saw…she was dead. I still can\'t believe she\'s really gone."\n\
\n\
You: "Thank you for your time. We\'ll be back later if we have more questions."'

bree_1 = '\nYou enter the living room to see a woman nervously arranging a vase of flowers, her face disturbed.\n\
\n\
You: "Hello. I am Detective Ativa and this is my partner, Detective Youngblood. We need to ask you some questions. What is your name?\n\
\n\
Woman: "My name is Bree Scholtz."\n\
\n\
Liam: "And how were you related to the victim?"\n\
\n\
Bree: "I\'m not. I mean, I\'m Mr. Li\'s maid so I only knew Ms. Nicole in passing."\n\
\n\
You: "I understand. Can you tell us what happened? You found the body, correct?"\n\
\n\
Bree: "Yes, it was horrible. Last night, Ms. Nicole had asked me to bring her a cup of the special blend that Mr. Li had set aside for her in the morning at precisely 8 a.m. Unfortunately, I didn\'t get up there until about 8:30 a.m. and Ms. Nicole was in the shower. I helped Mr. Li in the kitchen until breakfast was to be served. Mr. Li sent me upstairs when Ms. Nicole didn\'t come down. I went to her room and opened the door to see her lying on the ground, completely still. I screamed and they all came running up. I don\'t remember who said she was dead; I was in shock. It was a truly horrifying experience."\n\
\n\
Liam: "So you were also the last person to see the victim alive?"\n\
\n\
Bree: "I suppose so. Ms. Nicole was in the shower when I went there so I never saw her exactly."\n\
\n\
You: "Thank you for your time. We\'ll be back later if we have more questions."'

andres_1 = '\nYou enter the garden to see a man sitting in the garden, mournfully playing a tune on his clarinet. \n\
\n\
You: "Hello. I am Detective Ativa and this is my partner, Detective Youngblood. We need to ask you some questions. What is your name?"\n\
\n\
Man: "I\'m Dr. Andres Leal." \n\
\n\
Liam: "And how were you related to the victim?"\n\
\n\
Andres: "Nicole was one of my closest friends. Sakshi, Leng, Nicole, and I have been best friends since as long as I can remember."\n\
\n\
You: "I\'m so sorry for your loss. Can you tell us what happened?"\n\
\n\
Andres: "Leng had invited all of us for the week and it was going great. It was nice to all hang out again. This morning, the maid went up to call Nicole down for breakfast and she just started screaming. We all ran up there and Nicole was lying on the floor. I went over to her and checked if there was a pulse but I couldn\'t find one and she wasn\'t breathing. I tried to do CPR but…we were too late."\n\
\n\
You: "Thank you for your time. We\'ll be back later if we have more questions."'

gabi_2 = '\nYou enter the lab to see Gabi typing quickly on a computer.\n\
\n\
You: "Hey, Gabriella."\n\
\n\
Gabriella: "Karolina, Liam, my two fav idiots."\n\
\n\
Liam: "What\'s the good word, Gabi?"\n\
\n\
Gabriella: "First, let me say thank you for such a sweet case. I mean, Twilight Grove? Money City!"\n\
\n\
Liam: "You\'re telling me. The mansion is so huge, I keep getting confused which room is where."\n\
\n\
You: *clear throat* "Guys, focus." \n\
\n\
Gabriella: "Right, you\'re right. I\'m still waiting on the coroner to send me the full report but what I can tell you is that this tea cup contains poison."\n\
\n\
Liam: "What kind of poison?"\n\
\n\
Gabriella: "I don\'t know yet. And before you ask, I am working on it and the cellphone. You\'ll have to come back later. Why don\'t you two go back and snoop around. Make yourselves useful and bring some more goodies!"'

gabi_3 = '\nGabi: "Got more? No? I\'m not a miracle worker; bring me something I can work my magic on."'

riddle_win = 'You find some financial paperwork.\n\
You: "This is interesting."\n\
Liam: "What is it?"\n\
You: "Looks like Sakshi and Nicole may have been best friends but their companies are business rivals. We need to have another chat--"\n\
At this moment, Sakshi walks in.\n\
Sakshi: "What are you two doing here?"\n'

sofa = 'You: "A…a-choo!"\n\
Liam: "That maid must be doing a sub-par job."\n'

bookshelf = 'You: "Wow, he has a great collection."\n\
Liam: "But nothing useful for the case."\n'

sakshi_2 = 'You: "Sakshi, it looks like Nicole may have been poisoned."\n\
Sakshi: "That\'s horrible. Was it her tea? That\'s the first thing she drinks every morning."\n\
Liam: "So you knew about that?"\n\
Sakshi: "Everyone knows about that."\n\
You: "Does everyone also know about your business feud with you best friend?"\n\
Sakshi: "I\'d hardly call it a feud. If you\'re even asking that question, you don\'t know Nicole very well. Nicole is,\
was, a sweetheart but she hated business. She didn\'t make any of the decisions."\n\
Liam: "So what you\'re saying is that your company would be better off if you killed the CEO but not Nicole?"\n\
Sakshi: "Exact—wait, what? That\'s not what I\'m saying at all! Are you accusing me of killing my best friend? I\
would never! And especially not over business! If anyone here did it, it\'s probably Andres. Leave me out of it."\n\
You: "We\'ll come back when we have more questions."\n'

cupboard = 'You find a small container of tea grounds.\n\
You: "This is probably the tea supply Leng had set aside for Nicole."\n\
Liam: "We should ask him about that. Why did he set aside a special little box for her?"'

fridge = 'Liam: "I\'m starving. You think they would mind if I grabbed a slice of pizza or something?"\n\
You: "At a crime scene where someone was poisoned? Yeah, you take that chance."'

sink = 'You: "Nothing but dirty dishes."\n\
Liam: "Figures. Don\'t look at me, it\'s not my job to clean them."'

leng_2 = 'You: "Leng, it seems like Nicole was poisoned."\n\
Leng: "Oh my god, that\'s terrible. But how?"\n\
Liam: "Maybe you can help us with that. Any reason you had special tea set aside for Nicole?"\n\
Leng: "Yes, it\'s called being considerate! Nicole loved that tea. It\'s the same reason I bought Pop-tarts for Andres \
and organic orange juice for Sakshi. Are you guys insinuating that I killed her? Why would I? I cared about Nicole \
very much. If anyone did it, it\'s probably Bree! She\'s the one who took Nicole her tea."\n\
You: "We\'ll come back when we have more questions."'

bree_2 = 'You: "Bree, it seems that Nicole may have been poisoned."\n\
Bree: "That\'s awful."\n\
Liam: "Poison was found in her teacup. Can you explain how that happened?"\n\
Bree: "Are you saying that I--? No, no, of course not! I had nothing to do with it. All I did was prepare the tea Mr. Li\
and Ms. Nicole asked me to. That\'s it! Why would I hurt Ms. Nicole?"\n\
You: "We\'ll come back when we have more questions."'

trees = 'Liam: "Yew!"\n\
You: "What?"\n\
Liam: "I stepped on yew berries."\n\
You roll your eyes.'

bushes = 'Liam: "Any minute, we\'re going to tumble down a rabbit hole."\n\
You: "I don\'t think that’s exactly how Alice in Wonderland worked."'

gazebo = 'You find an old newspaper clipping that describes Andres punching another scientist.\n\
You: "Who would have thought clarinet-boy would have a temper?"\n\
Liam: "I did, I mean, it\'s the clarinet. Under-appreciated in the music world just like the violas. That would make \
anyone angry."'

andres_2 = 'You: "Andres, it seems that Nicole may have been poisoned."\n\
Andres: "That\'s so horrible. She didn\'t deserve that."\n\
Liam: "No one deserves that. As a doctor, you would certainly know a good deal about poisons, right?"\n\
Andres: "What are you trying to say? That I killed her? I would never do something like that. Nicole and I have \
always had our ups and downs. We were even engaged at one point but we have always remained good friends and I \
would never hurt her. You\'re right about one thing though: I am a doctor but that means I save lives, not take them."\n\
You: "We\'ll come back when we have more questions."'

gabi_4 = 'Gabriella: "I have good news, bad news, and confusing news."\n\
Liam: "Lay it on us."\n\
Gabriella: "The tea grounds you brought; definitely poisoned."\n\
You: "So that\'s the good news?"\n\
Gabriella: "No, that\'s the confusing news because the coroner sent me Nicole\'s stomach contents and she didn\'t drink \
any tea at all."\n\
Liam: "Then what poisoned her?"\n\
Gabriella: "You should check her room again. Maybe she ingested something else. Her blood toxicology report \
showed opioid use. And now the good news is I opened Nicole\'s phone. The bad news is: I opened Nicole\'s phone."\n\
You: "Meaning…?"\n\
Gabriella: "Entertain me for a bit and you get the passcode."'

message_unknown = 'Unknown: Turn me in and I\'ll spill your secret.'

message_leng = 'Leng: Hey, babe.\n\
Nicole: Hey, sweets. Excited for this week. Speaking of which…\n\
Leng: Please don\'t start.\n\
Nicole: If you\'re serious about us, you have to tell Sakshi. I don\'t care about your restaurant funding. I\'ll fund it!\n\
Leng: Nicky, please.\n\
Nicole: It\'ll get “her” off my back.\n\
Leng: We\'ll talk.'

message_andres = 'Nicole: I\'m glad you\'re coming. Leng said you weren\'t sure.\n\
Andres: I\'ll be there. Leng better have my Pop Tarts.\n\
Nicole: Ha ha. I\'ll tell him. I hope we can clear some things up this week.\n\
Andres: I already said I\'m over it.\n\
Nicole: But there\'s more. I want to do it in person.\n\
Andres: Okay, see you soon.'

end_messages = 'You: We have a lot more interviews to conduct."\n\
Liam: "And we still need to find what poisoned Nicole."\n\
Gabriella: "And you have to sign my legalize Wiebe campaign."\n\
You and Liam give Gabriella a look.\n\
Gabriella: "What? You guys have work to do. Get out of here."'

#-------------------------------------------------------------------------------

#Rooms

#Have three parameters in __init__ for the item name
#Refer to it as you did with dialogue
        
class Room:
    def __init__(self, name, description, item, item_two, item_three, item_four):
        self.name = name
        self.description = description
        self.item = item
        self.item_two = item_two
        self.item_three = item_three
        self.item_four = item_four
        
    def see_item(self, cosa):
        print cosa.description
        
    def search_room(self):
        print  
            
police_office = Room('Police Chief Ativa\'s Office', 'This is your father\'s police \
office. He is sitting at his desk doing some paperwork.', None, None, None, None)

study = Room('The Study', 'This study is where Sakshi stays.', paperwork, chair, pen, water_glass)

garden = Room('Garden', 'In this garden is Andres.', wrapper, clarinet, bench, news_clipping)

living_room = Room('Living Room', 'This room is where Bree resides.', vase_2, pen_2, desk, None)

kitchen = Room('Kitchen', 'This kitchen is where Leng is located.', tea_grounds, water_glass_2, vase, fridge)

bedroom = Room('Nicole\'s Bedroom', 'This is the crime scene. A woman\'s body lies \
next to the bed, a splattered tea cup by her side. You may examine the body, pick up the teacup, \
and look under the bed.', cell_phone, teacup, body, morphine_capsules)

lab = Room('Gabi\'s Lab', 'This lab is where you can always find Gabi. Come here \
when you need some evidence examined!', None, None, None, None)

front_yard = Room('Mansion\'s Front Yard', 'A lush green lawn spreads like a blanket in front of a massive and ornately structured mansion, the view only marred by splashes of trash.\n', pill_bottle, None, None, None)

global node 
node = police_office  

#Initiators
start = 0  
pill_bottle = 0
case_solved = False  
warning = 0
conversation = 0
sakshi_one = 0
leng_one = 0
bree_one = 0
andres_one = 0
arrival = 0
bedroom_arrival = 0
sakshi_two = 0
leng_two = 0
bree_two = 0
andres_two = 0
gabi_four = 0
messages_read = 0
leng_message = 0
andres_message = 0
unknown_message = 0
message_end = 0

global financial_riddle
financial_riddle = False

global passcode_won
passcode_won = False

global game_one
game_one = False

global game_two
game_two = False




#---------------------------------------------------------------------------------------------------------------------     




#Actual Gameplay   
  
while True:
    while warning == 0:
        print('\nDisclaimer: This game is not yet completely finished.\n\n')
        warning +=1
    print('\n')
    print node.name
            
    if node == police_office and start == 0:
        print('\n')
        print(scene_1)
        start +=1
        
    if node == police_office and case_solved == False:
        print(chief)
    
    if node == lab and len(user_inventory.inventory) == 0:
        print(gabi)
        
    if node == lab and len(user_inventory.inventory) == 1 and conversation <=4:
        print('\nGabi: There\'s another piece of evidence lurking around in that house. Go forth!')
        
    if node == front_yard and arrival == 0:
        print(scene_2)
        arrival+=1
    
    if node == bedroom and bedroom_arrival == 0:
        print(scene_3)
        bedroom_arrival+=1
        
    if node == study and sakshi_one == 0:
        print(sakshi_1)
        sakshi_one+=1
        conversation+=1
        
    if node == garden and andres_one == 0:
        print(andres_1)
        andres_one+=1
        conversation+=1
        
    if node == kitchen and leng_one == 0:
        print(leng_1)
        leng_one+=1
        conversation+=1
        
    if node == living_room and bree_one == 0:
        print(bree_1)
        bree_one+=1
        conversation +=1
        
    if conversation == 4 and len(user_inventory.inventory) == 2 and node == lab:
        print(gabi_2)
        conversation +=1
        
    if sakshi_two == 0 and sakshi_one == 1:
        study.description = 'You may now look under the sofa, in the bookshelf, and in the desk. Maybe there\'s some evidence in here.'
    
    if leng_two == 0 and leng_one == 1:
        kitchen.description = 'You may search in the cupboard, in the sink, or in the fridge. Could there be something incriminating here?'
    
    if andres_two == 0 and andres_one == 1:
        garden.description = 'You can check out the area behind the trees, in the bushes, or in the gazebo. There might be something intresting here.'               
                                                          
        
    if node in [police_office, lab]:
        print('\nYou can go to:\n\
        -mansion\n\
        -lab\n\
        -police office\n\
        \n\
Additional commands:\n\
        - search')
    elif node in [study, kitchen, front_yard, living_room, garden]:
        print('\nYou can go to:\n\
        - study\n\
        - mansion\n\
        - kitchen\n\
        - crime scene\n\
        - living room\n\
        - garden\n\
        - police office\n\
        - lab\n\
        \n\
Additional commands:\n\
        - search\n\
        - pick up *item name*')
    
    user_command = raw_input('> ') 
   
    if user_command in ['q', 'quit', 'exit']:
        sys.exit(0)
    elif 'police office' in user_command:
        node = police_office
    elif 'study' in user_command and node in [front_yard, garden, living_room, kitchen, bedroom]:
        node = study
    elif 'garden' in user_command and node in [front_yard, study, living_room, kitchen, bedroom]:
        node = garden
    elif 'living room' in user_command and node in [front_yard, garden, study, kitchen, bedroom]:
        node = living_room
    elif 'kitchen' in user_command and node in [front_yard, garden, living_room, study, bedroom]:
        node = kitchen
    elif 'crime scene' in user_command and node in [front_yard, garden, living_room, kitchen, study]:
        node = bedroom
    elif 'lab' in user_command:
        node = lab
    elif 'mansion' in user_command:
        node = front_yard
    elif 'search' in user_command:
        print node.description
        
    #Games----------------------------------------------------------------------------------------------------------------
    
    #Setting up variables to be called on later
    
    def passcode_hangman():

        life = 5
        bank = ["zero one twenty nine"]
        word = random.choice(bank)
        letters_left = list(set(word)) #creating a list of letters in word
        if ' ' in word:
            letters_left.remove(' ') #removing the space if there is one
                    
        user_guesses = [] #More variables
        wrong_answers = 0
        print ("You have five chances right now.")
        while life > 0: 
            
            for letter in word:
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
                print('Gabriella: "Which conversation do you wanna read?"\
                    - Leng\n\
                    - Andres\n\
                    - Unknown')
                pic_3.append(hang)
                break
                
    
    
    def andres_hangman():
        life = 5
        bank = ["temper tantrum"]
        word = random.choice(bank)
        letters_left = list(set(word)) #creating a list of letters in word
        if ' ' in word:
            letters_left.remove(' ') #removing the space if there is one
                    
        user_guesses = [] #More variables
        wrong_answers = 0
        print ("You have five chances right now.")
        while life > 0: 
            
            for letter in word:
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
                print(gazebo)
                pic.append(hang)
                break
                
    def leng_hangman():
        life = 5
        bank = ["poisonous tea?"]
        word = random.choice(bank)
        letters_left = list(set(word)) #creating a list of letters in word
        if ' ' in word:
            letters_left.remove(' ') #removing the space if there is one
        if '?' in word:
            letters_left.remove('?')
                    
        user_guesses = [] #More variables
        wrong_answers = 0
        while life > 0: 
            
            for letter in word:  
                if letter in user_guesses:
                    print letter,
                elif letter == ' ':
                    print letter,
                elif letter == '?':
                    print letter,
                else:
                    print ('_'),         
                
            current_guess = raw_input("Guess a letter: ") #This takes in raw input
            user_guesses.append(current_guess)
            if current_guess in word: #If guess in word, remove from letters_left
                letters_left.remove(current_guess)              
                #print letters_left
            if current_guess not in word: #If you guess incorrectly
                life -= 1
                wrong_answers += 1
                print ("Your life count: %s")%life
                    
            if len(letters_left) == 0:
                break
        
        if life <=0:
            print 'You\'ve messed up on this minigame. Come back and try again.'
        else:   
            print('\n')     
            print(cupboard)
            hang.inventory.append(pic_2)
                

    def financial_riddle():
        key = 'bree'
        #Time = 20 seconds; if they don\'t leave in time, lose game.
        
        riddle = 'There is one of us here in the mansion\n\
    Who is not what they seem\n\
    They may seem to be kind\n\
    But that\'s a mirage and a dream\n\
    Simple-like fashion\n\
    With formal like language\n\
    And a nervous register\n\
    Who am I?\n'
        
        print riddle
            
        user_riddle_guess = raw_input('Take a guess:\n')
        if user_riddle_guess.strip().lower() == key:
            print 'You have guessed correctly;\n\
    it is Bree. Press "enter" to continue and see \n\
    what you find.'   
            user_riddle_guess_two = raw_input('> ')
            if user_riddle_guess_two.strip() == '':
                paperwork.pick_up(user_inventory)
                print riddle_win     
                
        else:
            print 'Sorry. That\'s not who it is.\n'
            print 'You and Liam quickly cover your ears.\n\
    Liam: "What is that horrible ringing noise?!"\n\
    You: "We must have set off an alarm when we tried opening the desk lock!\n\
    Liam: "We have to get out of the mansion!"\n\
    You: "Now!!"'
       
        
    if financial_riddle == False and node == study and sakshi_one >0:
        if 'under' and 'sofa' in user_command:
            print(sofa)
            
        elif 'bookshelf'in user_command:
            print(bookshelf)
            
        elif user_command == 'desk':
            financial_riddle()
        
        if paperwork in user_inventory.inventory:
            financial_riddle = True
            
    if financial_riddle == True and node == study and sakshi_two == 0 and sakshi_one>0:
        print(sakshi_2)
        sakshi_two+=1
        
    if game_one == False and node == garden and andres_one >0:
        if 'bushes' in user_command:
            print(bushes)
            
        elif 'trees' in user_command:
            print(trees)
            
        elif 'gazebo' in user_command:
            andres_hangman()
        
        if pic in hang.inventory:
            game_one = True    
            
    if game_one == True and node == garden and andres_two == 0 and andres_one >0:
        print(andres_2)
        andres_two+=1
        
    if game_two == False and node == kitchen and leng_one >0:
        if 'cupboard' in user_command:
            leng_hangman()
            
        elif 'fridge' in user_command:
            print(fridge)
        
        elif 'sink' in user_command:
            print(sink)
            
        if pic_2 in hang.inventory:
            game_two = True
            
    if game_two == True and node == kitchen and leng_two == 0 and leng_one >0:
        print(leng_2)
        leng_two +=1
            
    if node == living_room and bree_two == 0 and bree_one >0:
        print(bree_2)
        bree_two +=1
        
    if leng_two == 1 and bree_two == 1 and andres_two == 1 and sakshi_two == 1 and node == lab:
        print(gabi_4)
        passcode_hangman()
        
    if messages_read < 3 and pic_3 in hang.inventory:
        
        if 'leng' in user_command:
            print(message_leng)
            leng_message +=1
            if leng_message == 1:
                messages_read +=1
        
        if 'andres' in user_command:
            print(message_andres)
            andres_message +=1
            if andres_message == 1:
                messages_read +=1
        
        if 'unknown' in user_command:
            print(message_unknown)
            unknown_message +=1
            if unknown_message ==1:
                messages_read +=1
                
    if messages_read == 3 and node == lab and message_end == 0:
        print(end_messages)
        message_end+=1
        print('\nWell, that\'s all the sleuthing we have for now!')
        
            
    elif 'examine body' in user_command:
        print(examine)
        
    elif user_command == 'pick up chair' and node == study:
        chair.pick_up(user_inventory)
        
    elif user_command == 'pick up glass' and node == study:
        water_glass.pick_up(user_inventory)
        
    elif user_command == 'pick up pen' and node == study:
        pen.pick_up(user_inventory)
        
    elif user_command == 'pick up cell phone' and node == bedroom:
        cell_phone.pick_up(user_inventory)
        
    elif user_command == 'look under bed' and node == bedroom:
        print(phone)
        
    elif user_command == 'pick up teacup' and node == bedroom:
        teacup.pick_up(user_inventory)
        print(cup)
        
    elif user_command == 'pick up morphine capsules' and node == bedroom:
        morphine_capsules.pick_up(user_inventory)
        
    elif user_command == 'check trash' and node == front_yard:
        print  
        
    elif user_command == 'pick up pill bottle' and node == front_yard:
        pill_bottle.pick_up(user_inventory)
        pill_bottle+=1
        
    elif user_command == 'pick up vase' and node == living_room:
        vase_2.pick_up(user_inventory)
        
    elif user_command == 'pick up pen' and node == living_room:
        pen_2.pick_up(user_inventory)
        
    elif user_command == 'pick up wrapper' and node == garden:
        wrapper.pick_up(user_inventory)
        
    elif user_command == 'pick up clarinet' and node == garden:
        clarinet.pick_up(user_inventory)

    elif user_command == 'pick up news clipping' and node == garden:
        news_clipping.pick_up(user_inventory)
        
    else:
        print '?'
    
financial_riddle()
        

    
        

#-------------------------------------------------------------------------------
        
#Do dialogue in order this by continously calling the dialogue 'say' function
#Progress stories this way
        
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
    
