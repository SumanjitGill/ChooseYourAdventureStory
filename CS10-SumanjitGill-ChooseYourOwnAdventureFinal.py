# -*- coding: utf-8 -*-
#WARNING: GAME UNFINISHED
#More involvement in game :) ~ puzzles and more functions to search the rooms
#from _____ import *

import sys
import random
import time
import pickle
global p_win
p_win = False

global c_win
c_win = False


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

cell_phone = Item('Nicole\'s Cell Phone', 'There is a passcode on this phone but\
there must be some good evidence on here; Why not take it to Gabi?')

teacup = Item('Teacup', 'This broken cup can be taken to Gabi. Nicole drinks tea\
every morning... any ideas?')

body = Item('Nicole\'s Body', 'There are no trauma signs; Could she have been killed\
with poison?')

paperwork = Item('Financial Paperwork', 'This paperwork lets you know that Sakshi\
and Nicole were business rivals.')

#To be updated later

pic = Item('Pic', 'What are you doing examining this? Get back to work.')

pic_2 = Item('Pic 2', 'If you\'re looking at this, you aren\'t doing your job.')

pic_3 = Item('Pic 3', 'Seriously, get back to work.')

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
The Chief user_inventorys up the phone and looks at a picture with him and his daughter  (you) on the day she (you) graduated from the police academy.\n\
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
Andres: "Leng had invited all of us for the week and it was going great. It was nice to all user_inventory out again. This morning, the maid went up to call Nicole down for breakfast and she just started screaming. We all ran up there and Nicole was lying on the floor. I went over to her and checked if there was a pulse but I couldn\'t find one and she wasn\'t breathing. I tried to do CPR but…we were too late."\n\
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
\n\
You: "This is interesting."\n\
\n\
Liam: "What is it?"\n\
\n\
You: "Looks like Sakshi and Nicole may have been best friends but their companies are business rivals. We need to have another chat--"\n\
\n\
At this moment, Sakshi walks in.\n\
\n\
Sakshi: "What are you two doing here?"\n'

sofa = 'You: "A…a-choo!"\n\
\n\
Liam: "That maid must be doing a sub-par job."\n'

bookshelf = 'You: "Wow, he has a great collection."\n\
\n\
Liam: "But nothing useful for the case."\n'

sakshi_2 = 'You: "Sakshi, it looks like Nicole may have been poisoned."\n\
\n\
Sakshi: "That\'s horrible. Was it her tea? That\'s the first thing she drinks every morning."\n\
\n\
Liam: "So you knew about that?"\n\
\n\
Sakshi: "Everyone knows about that."\n\
\n\
You: "Does everyone also know about your business feud with you best friend?"\n\
\n\
Sakshi: "I\'d hardly call it a feud. If you\'re even asking that question, you don\'t know Nicole very well. Nicole is,\
was, a sweetheart but she hated business. She didn\'t make any of the decisions."\n\
\n\
Liam: "So what you\'re saying is that your company would be better off if you killed the CEO but not Nicole?"\n\
\n\
Sakshi: "Exact—wait, what? That\'s not what I\'m saying at all! Are you accusing me of killing my best friend? I\
would never! And especially not over business! If anyone here did it, it\'s probably Andres. Leave me out of it."\n\
\n\
You: "We\'ll come back when we have more questions."\n'

cupboard = 'You find a small container of tea grounds.\n\
\n\
You: "This is probably the tea supply Leng had set aside for Nicole."\n\
\n\
Liam: "We should ask him about that. Why did he set aside a special little box for her?"'

fridge = 'Liam: "I\'m starving. You think they would mind if I grabbed a slice of pizza or something?"\n\
\n\
You: "At a crime scene where someone was poisoned? Yeah, you take that chance."'

sink = 'You: "Nothing but dirty dishes."\n\
\n\
Liam: "Figures. Don\'t look at me, it\'s not my job to clean them."'

leng_2 = 'You: "Leng, it seems like Nicole was poisoned."\n\
\n\
Leng: "Oh my god, that\'s terrible. But how?"\n\
\n\
Liam: "Maybe you can help us with that. Any reason you had special tea set aside for Nicole?"\n\
\n\
Leng: "Yes, it\'s called being considerate! Nicole loved that tea. It\'s the same reason I bought Pop-tarts for Andres \
and organic orange juice for Sakshi. Are you guys insinuating that I killed her? Why would I? I cared about Nicole \
very much. If anyone did it, it\'s probably Bree! She\'s the one who took Nicole her tea."\n\
\n\
You: "We\'ll come back when we have more questions."'

bree_2 = 'You: "Bree, it seems that Nicole may have been poisoned."\n\
\n\
Bree: "That\'s awful."\n\
\n\
Liam: "Poison was found in her teacup. Can you explain how that happened?"\n\
\n\
Bree: "Are you saying that I--? No, no, of course not! I had nothing to do with it. All I did was prepare the tea Mr. Li \
and Ms. Nicole asked me to. That\'s it! Why would I hurt Ms. Nicole?"\n\
\n\
You: "We\'ll come back when we have more questions."'

trees = 'Liam: "Yew!"\n\
\n\
You: "What?"\n\
\n\
Liam: "I stepped on yew berries."\n\
\n\
You roll your eyes.'

bushes = 'Liam: "Any minute, we\'re going to tumble down a rabbit hole."\n\
\n\
You: "I don\'t think that’s exactly how Alice in Wonderland worked."'

gazebo = 'You find an old newspaper clipping that describes Andres punching another scientist.\n\
\n\
You: "Who would have thought clarinet-boy would have a temper?"\n\
\n\
Liam: "I did, I mean, it\'s the clarinet. Under-appreciated in the music world just like the violas. That would make \
anyone angry."'

andres_2 = 'You: "Andres, it seems that Nicole may have been poisoned."\n\
\n\
Andres: "That\'s so horrible. She didn\'t deserve that."\n\
\n\
Liam: "No one deserves that. As a doctor, you would certainly know a good deal about poisons, right?"\n\
\n\
Andres: "What are you trying to say? That I killed her? I would never do something like that. Nicole and I have \
always had our ups and downs. We were even engaged at one point but we have always remained good friends and I \
would never hurt her. You\'re right about one thing though: I am a doctor but that means I save lives, not take them."\n\
\n\
You: "We\'ll come back when we have more questions."'

gabi_4 = 'Gabriella: "I have good news, bad news, and confusing news."\n\
\n\
Liam: "Lay it on us."\n\
\n\
Gabriella: "The tea grounds you brought; definitely poisoned."\n\
\n\
You: "So that\'s the good news?"\n\
\n\
Gabriella: "No, that\'s the confusing news because the coroner sent me Nicole\'s stomach contents and she didn\'t drink \
any tea at all."\n\
\n\
Liam: "Then what poisoned her?"\n\
\n\
Gabriella: "You should check her room again. Maybe she ingested something else. Her blood toxicology report \
showed opioid use. And now the good news is I opened Nicole\'s phone. The bad news is: I opened Nicole\'s phone."\n\
\n\
You: "Meaning…?"\n\
Gabriella: "Check it out."'

message_unknown = 'Unknown: Turn me in and I\'ll spill your secret.'

message_leng = 'Leng: Hey, babe.\n\
\n\
Nicole: Hey, sweets. Excited for this week. Speaking of which…\n\
\n\
Leng: Please don\'t start.\n\
\n\
Nicole: If you\'re serious about us, you have to tell Sakshi. I don\'t care about your restaurant funding. I\'ll fund it!\n\
\n\
Leng: Nicky, please.\n\
\n\
Nicole: It\'ll get “her” off my back.\n\
\n\
Leng: We\'ll talk.'

message_andres = 'Nicole: I\'m glad you\'re coming. Leng said you weren\'t sure.\n\
\n\
Andres: I\'ll be there. Leng better have my Pop Tarts.\n\
\n\
Nicole: Ha ha. I\'ll tell him. I hope we can clear some things up this week.\n\
\n\
Andres: I already said I\'m over it.\n\
\n\
Nicole: But there\'s more. I want to do it in person.\n\
\n\
Andres: Okay, see you soon.'

end_messages = 'You: We have a lot more interviews to conduct."\n\
\n\
Liam: "And we still need to find what poisoned Nicole."\n\
\n\
Gabriella: "And you have to sign my legalize Wiebe campaign."\n\
\n\
You and Liam give Gabriella a look.\n\
\n\
Gabriella: "What? You guys have work to do. Get out of here."'

drawers = 'You: "She has a lot of socks…"\n\
\n\
Liam: "All signs point to her feet getting cold. Moving on."'

purse = 'Liam: Isn’t there a rule about not going through women’s purses?\n\
\n\
You: That doesn’t apply in a murder investigation. Or in some friendships apparently.\n\
\n\
Liam: One time. I swear. Once.'

trashcan = 'You: Bingo, baby. Morphine capsules.\n\
\n\
Liam: Bingo, baby? \n\
\n\
You: I went with it. Let’s get these to Gabi.'

sakshi_3 = 'Sakshi: Possibly my two least favorite people in the world. Come back to accuse me of murder again?\n\
\n\
You: Maybe. We could always make it a public one if you don\'t cooperate.\n\
\n\
Sakshi: Don\'t forget that I have the mayor\'s number on speed dial.\n\
\n\
Liam: And don\'t forget her dad\'s the Chief of police and the mayor\'s best friend.\n\
\n\You: Liam.\n\
Sakshi: Whatever. Just ask me what you need to.\n\
Liam: Poison is a clean, efficient, and calculating method of killing rather than a passionate one. A method that I\'m sure a ruthless tycoon would use in a heartbeat.\n\
\n\
Sakshi: A smart and rich business tycoon would use a hired killer rather than getting their own hands dirty. Is this all you have? Supposition?\n\
\n\
Liam: There was a threatening text on Nicole’s phone. Do you know anything about that?\n\
\n\
Sakshi: She never told me anything about it.\n\
\n\
You: For being Nicole\'s best friend, there\'s not a single text from you on her phone.\n\
\n\
Sakshi: So? When I want to talk to Nicole, I call. This is all so ridiculous. I still don\'t see any motive at all.\n\
\n\
You: So you weren\'t aware that your boyfriend, Leng, was having an affair with the victim?\n\
\n\
Sakshi: What?! There is no way in--- That two-timing… I never should have trusted her! Now I wish I had killed her!\n\
\n\
You: We\'ll come back when we have more questions.'

leng_3 = 'Leng: Do you have any news?\n\
\n\
You: Nothing we can share at this time.\n\
\n\
Leng: If there\'s anything I can do to help, please, let me know.\n\
\n\
Liam: It\'s interesting you say that.\n\
\n\
You: I wonder, if you really felt that way, why didn\'t you tell us you and Nicole were having an affair?\n\
\n\
Leng: Oh…yes, we were. I just didn\'t think it was relevant.\n\
\n\
Liam: Wasn\'t relevant? Or because you were afraid you would come under suspicion if we knew? Especially since Nicole wanted to tell Sakshi, which would threaten your restaurant funding and business expansion.\n\
\n\
Leng: I didn\'t kill her! I didn\'t care about Sakshi\'s money and I told Nicole that, too. I just didn\'t know how to spare Sakshi\'s feelings. She comes off cold but she cares about both of us. I had always been in love with Nicole but she had always been in love with Andres, even after they broke up. I wanted us to finally be together and now, we never will.\n\
\n\
You: There was a threatening text message on Nicole\'s phone. Was that from you?\n\
\n\
Leng: No! Of course not. It was from Bree.\n\
\n\
Liam: What do you mean?\n\
\n\
Leng: Nicole found out Bree was stealing from me but when we said we were going to turn her in, Bree threatened to tell Sakshi about our affair. That was another reason we were going to come clean to Sakshi. Bree has been blackmailing us this entire time.\n\
\n\
You: We\'ll come back when we have more questions.'

bree_3 = 'Bree: Detectives. Can I get you anything?\n\
\n\
You: No, thank you, but you can tell us how long you were blackmailing Nicole.\n\
\n\
Bree: Wh…what?\n\
\n\
Liam: Leng told us everything.\n\
\n\
Bree: It\'s his word against mine.\n\
\n\
You: Or so you hope. Nicole and Leng were going to come clean to Sakshi about the affair. No more affair, no more leverage, no more blackmail. Nothing was going to stop them from firing or turning you in.\n\
\n\
Bree: I swear I didn\'t do it!\n\
\n\
Liam: People do things when they\'re desperate. You had access to Nicole\'s room. You were the last one to see Nicole alive.\n\
\n\
Bree: Everyone had access! I didn\'t do this. I didn\'t even steal! Nicole just blamed me and Mr. Leng believed her. She was a sneaky one, that woman. People thought she was so sweet and clueless but they were wrong. Nicole was romancing her best friend\'s boyfriend while trying to get Mr. Andres back, too. I saw her this week, always trying to get him off alone. I may be glad she\'s dead but I didn\'t do it.\n\
\n\
You: We\'ll come back when we have more questions.'

andres_3 = 'Andres: Detectives, did you find anything new?\n\
\n\
You: Nothing we can share at this time.\n\
\n\
Andres: Are you putting enough time into this investigation? Shouldn\'t you have caught someone by now?\n\
\n\
Liam: We assure you. We are doing everything we can.\n\
\n\
Andres: Of course, I apologize. It\'s just…Nicole was very important to me.\n\
\n\
You: In your texts, Nicole said she wanted to clear some things up. What was that all about?\n\
\n\
Andres: Our relationship. I wanted us both to move on but Nicole didn\'t feel that way. I told her we were done.\n\
\n\
Liam: Why did you two break up?\n\
\n\
Andres: Nicole…was beautiful and kind but she could be very demanding. Everything had to be her way, no compromise, no discussion. I always wondered how she and Sakshi got along so well. Eventually, our engagement fell apart. I still cared for her, obviously, but we couldn\'t be together.\n\
\n\
You: Were you aware Nicole and Leng were having an affair?\n\
\n\
Andres: I wasn\'t sure. They seemed a lot more in touch with each other but I figured something was up. That\'s why I was surprised when Nicole really wanted me here and to talk me into starting something again.\n\
\n\
Liam: We know you have a temper. You once had a very public brawl. Maybe you weren\'t as over Nicole as you claim.\n\
\n\
Andres: That midget deserved it. He was stealing my work and claiming it as his own. If I really wanted Nicole back, I would never have killed her. How is that love?\n\
\n\
You: Nicole had a threatening message on her phone. Do you know anything about that?\n\
\n\
Andres: No, I don\'t. I wish I did. Maybe I could\'ve helped her.\n\
\n\
You: We\'ll come back when we have more questions.'

gab = 'You: Tell us something great, Gabi.\n\
\n\
Gabriella: Harry Potter. Harry Potter is great.\n\
\n\
Liam: Lord of the Rings over Harry Potter.\n\
\n\
Gabriella: Blasphemy.\n\
\n\
You: And passing over the impending fan fight?\n\
\n\
Gabriella: Nicole\'s morphine capsules aren\'t really morphine. They contain highly concentrated poison made from yew trees.\n\
\n\
You: So that\'s what killed her?\n\
\n\
Gabriella: No, I just said it as a joke.\n\
\n\
Liam: Well, does it happen to have her killer\'s name written on it?\n\
\n\
Gabriella: No dice. And no prints other than Nicole either. But here\'s some bonus information. This isn\'t even Nicole\'s pill bottle.\n\
\n\
You: What are you talking about?\n\
\n\
Gabriella: Sure, it has her name on it but it\'s not her prescription number; I checked. Somewhere out there, Nicole\'s real pill bottle is floating around.\n\
\n\
You: Guess we\'d better go hunting again.'

sakshi_4 = 'You: Did you know Nicole took painkillers?\n\
\n\
Sakshi: Of course I do. She\'d been on them for a while since she fell pretty badly on a skiing trip. I felt sorry for her then. Now I wish she had fallen a little harder.\n\
\n\
Liam: We\'ll be back if we have more questions.'

leng_4 = 'You: Did you know Nicole took painkillers?\n\
\n\
Leng: Yeah, one pill every 12 hours. She\'s been dealing with the pain since she fell when we went skiing in the mountains together.\n\
\n\
Liam: We\'ll be back if we have more questions.'

andres_4 = 'You: Did you know Nicole took painkillers?\n\
\n\
Andres: I prescribed them. She fell on a skiing trip. It was pretty hard for her since she had never been good with physical pain.\n\
\n\
Liam: We\'ll be back if we have more questions.'

bree_4 = 'You: Did you know Nicole took painkillers?\n\
\n\
Bree: No, I  don\'t know anything about that.\n\
\n\
Liam: We\'ll be back if we have more questions.'

trashed = 'You: Finally. It\'s empty; killer must have spilled the real morphine capsules. Someone really tried to scratch Nicole\'s information off of this bottle, too.\n\
\n\
Liam: Hopefully they forgot about wiping the prints. Let\'s get it to Gabi.'

#-------------------------------------------------------------

gabu = 'You: What\'s the word?\n\
\n\
Gabriella: Luscious.\n\
\n\
Liam: I would\'ve gone with ostentatious.\n\
\n\
You: I would go with “wasting our time.”\n\
\n\
Gabriella: That\'s more than one word. Anyways, this is definitely Nicole\'s bottle.\n\
\n\
Liam: Tell me there are prints on there.\n\
\n\
Gabriella: Nope. Killer wiped the outside clean.\n\
\n\
You: Great so we need to keep digging.\n\
\n\
Gabriella: Not as far as you think. Killer wiped the outside but forgot the inside of the bottle cap. You can say it; I\'m a genius.\n\
\n\
Liam: Gabi, you are a genius.\n\
\n\
Gabriella: Get me your suspects\' prints and I can match this for you in no time.'

s_chair = 'Liam: I was sure we\'d get some here.\n\
\n\
You: I told you, we should look—\n\
\n\
Liam: I\'ll find them before you!\n\
\n\
You: This isn\'t a game.'

s_pen = 'You: A clean set of prints. And you said I wouldn\'t find them first.\n\
\n\
Liam: You got lucky. Besides, this isn\'t a game.\n\
\n\
You: Now you say it.'

s_glass = 'You: Are you taking prints or just looking for a drink?\n\
\n\
Liam: Apparently just getting a drink; no prints here.'

l_glass = 'You: One set of prints down.\n\
\n\
Liam: How many to go? \n\
\n\
You: Really depends on the order the player chose.\n\
\n\
Liam: What are you talking about?\n\
\n\
You: Never mind.'

l_vase = 'You: Looks like no one has touched this in years.\n\
\n\
Liam: Well, when you have a maid who\'s blackmailing you, I doubt she does her job properly.'

l_fridge = 'Liam: Looking for food never pays off…\n\
\n\
You: No prints.\n\
\n\
Liam: Opposite problem; too many.'

b_vase = 'You: It may not be that clean but it\'s got some prints.\n\
\n\
Liam: That\'s what counts.'

b_pen = 'Liam: Do you like black or blue pens? I always forget.\n\
\n\
You: Does it matter?\n\
\n\
Liam: Hardly. There aren\'t any prints here anyways.'

b_desk = 'Liam: Nothing. I\'m tired.\n\
\n\
You: Oh, poor baby. Keep looking.'

a_pop = 'Liam: What was this..? Cinnamon? I like strawberry flavor.\n\
\n\
You: I like things with prints on them.\n\
\n\
Liam: Then you\'re out of luck.'

a_clarinet = 'Liam: Prints, prints everywhere.\n\
\n\
You: Then collect them already.'

a_bench = 'You: How do you sit on a bench without leaving a fingerprint?\n\
\n\
Liam: You just use your butt.'

gaba = 'Gabriella: Ding, ding! We have a winner. Your killer is….Andres. Tell the Chief that Team Gabi has done it again.'

daddy = 'Chief: I hope you\'re here because you know who the killer is.\n\
\n\
You: Yes, sir. It was Andres.\n\
\n\
Liam: All we need to do now is to arrest him. Permission to let the media explode?\n\
\n\
Chief: Keep the arrest quiet until you bring him back here. Then we let the mayor handle the media. You two have done your jobs. Good work.'

confess = 'Andres: My plan was perfect. How could this happen?\n\
\n\
You: Because you can\'t control everything. You switched out Nicole\'s painkillers with the poisoned ones but you forgot to wipe your print off the inside of the medicine bottle when you took the cap off to spill out her real medication. That would have been okay because on any normal day, the trash would\'ve headed to the dump except you couldn\'t have predicted the garbage strike happening.\n\
\n\
Liam: Not to mention you trying to pin the murder on Leng by dosing the tea grounds with poison as well. You thought Nicole would take her medication with her tea so no one would look any further than the tea grounds and would assume that\'s how she died. It would have worked except Bree took Nicole\'s tea later than she was told.\n\
\n\
You: We know the “how.” I want to know the “why.”\n\
\n\
Liam: Were you really that jealous of Nicole and Leng?\n\
\n\
Andres: Hardly. I could care less about that. I dumped Nicole and the princess couldn\'t take it. She\'s the one who leaked my research and work to my rivals. All of my work, just gone. She admitted it to me after her accident. She said she was trying to be better and wanted to make amends and apologize. Apologize? For stabbing me in the back? This wasn\'t just a dead houseplant or a rumor. She ruined my chance at being acknowledged within the science community; she took my credit. So I took her life.\n\
\n\
You: And now you lose your chance at having a life of your own.\n\
\n\
Liam: Enjoy prison.'

wrap_up = 'Andres was arrested and convicted of Nicole\'s murder. Sakshi and Leng are no longer together but Sakshi is still backing Leng\'s restaurant business. According to Sakshi, not doing it would just be bad business because the man really was a good chef. Bree was also arrested but for theft and blackmail. Whether her word stands up against Leng\'s or not still remains to be seen. Karolina, Liam, and the Chief let the mayor deal with the media storm, trying to stay out of the spotlight, but everyone knows who solved the murder and who deserves the credit. Don\'t you?'

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

global financia_riddle
financia_riddle = False

global passcode_won
passcode_won = False

global game_one
game_one = False

global game_two
game_two = False



scene_dos = 0
sakshi_act = 0
leng_act = 0
andres_act = 0
s_scene_dos = 0
l_scene_dos = 0
a_scene_dos = 0

global ga

ga = 0

s4 = 0
l4 = 0
a4 = 0
b4 = 0
s3 = 0
l3 = 0
a3 = 0
b3 = 0

gabbu = 0
trashg = 0

yog = 0
sp = 0
lg = 0
bv = 0
ac = 0
goy = 0
chidad = 0
conf = 0 

def save():
    global node, user_inventory, start, case_solved, conversation, sakshi_one, sakshi_two, bree_one, bree_two, leng_one, leng_two, andres_one, andres_two, messages_read
    with open('savegame.dat', 'wb') as f:
        pickle.dump([node, user_inventory, start, case_solved, conversation, sakshi_one, sakshi_two, bree_one, bree_two, leng_one, leng_two, andres_one, andres_two, messages_read], f, protocol=2)
    print 'Game successfully saved'
    
def load():
    global node, user_inventory, start, case_solved, conversation, sakshi_one, sakshi_two, bree_one, bree_two, leng_one, leng_two, andres_one, andres_two, messages_read
    with open('savegame.dat', 'rb') as f:
        node, user_inventory, start, case_solved, conversation, sakshi_one, sakshi_two, bree_one, bree_two, leng_one, leng_two, andres_one, andres_two, messages_read = pickle.load(f)
    print 'Game successfully loaded'
#---------------------------------------------------------------------------------------------------------------------     




#Actual Gameplay   
  
while True:
    print('\n')
    print node.name
            
    if node == police_office and start == 0:
        print('\n')
        print(scene_1)
        start +=1
        
    if node == police_office and goy ==0:
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
        
    def ana_two():
        word = 'Painkillers'
        ana = 'A Sniper Kill'
        guessed = False
        print 'Unscramble this anagram:\n'
        print ana
        user_guesses = 0
        while guessed == False:
            user_guess = raw_input('> ')
            if user_guess == word:
                print 'You guessed it!'
                guessed = True
                return trashed
                
            else:
                print 'Guess again!'
                user_guesses +=1
                
            if user_guesses == 2:
                user_hint = raw_input('Need a hint?\n')
                if user_hint in ['yes', 'ye', 'y', 'yea','ya', 'yeah', 'yah']:
                    print 'It\'s something that is commonly taken to reduce pain in the body.'
                    
                
            if user_guesses >=4:
                print 'You ran out of guesses! Well, I guess you aren\'t that competent to work on this case. Sorry, but, we\'re going to call another detective to find out what actually happened here.'
                sys.exit(0)
    
    def ana_three():
        word = 'temper tantrum'
        ana = 'Tamer Tempt Run'
        guessed = False
        print 'Unscramble this anagram:\n'
        print ana
        user_guesses = 0
        while guessed == False:
            user_guess = raw_input('> ')
            if user_guess.lower() == word:
                print 'You guessed it!'
                guessed = True
                pic.pick_up(user_inventory)
                
            else:
                print 'Guess again!'
                user_guesses +=1
                
            if user_guesses == 2:
                user_hint = raw_input('Need a hint?\n')
                if user_hint in ['yes', 'ye', 'y', 'yea','ya', 'yeah', 'yah']:
                    print 'It\'s something that occurs when, usually, a small and stubborn child gets very upset.'
                    
                
            if user_guesses >=4:
                print 'You ran out of guesses! Well, I guess you aren\'t that competent to work on this case. Sorry, but, we\'re going to call another detective to find out what actually happened here.'
                sys.exit(0) 
        
    def anagram():
        anagram = 'Favor A Life'
        word = 'Love Affair'
        guessed = False
        print 'Unscramble this anagram to find the phrase written on this paper:\n'
        print anagram
        user_guesses = 0
        while guessed == False:
            user_guess = raw_input('> ')
            if user_guess == word:
                print 'You guessed it! Now, what could this message mean...?'
                guessed = True
                global p_win
                p_win = True
                break
            else:
                print 'Guess again!'
                user_guesses +=1
                
            if user_guesses == 2:
                user_hint = raw_input('Need a hint?\n')
                if user_hint in ['yes', 'ye', 'y', 'yea','ya', 'yeah', 'yah']:
                    print 'It deals with a type of betrayal... one that hurts most in that little organ on the left side of your chest.'
                    
                
            if user_guesses >=4:
                print 'You ran out of guesses! Well, I guess you aren\'t that competent to work on this case. Sorry, but, we\'re going to call another detective to find out what actually happened here.'
                sys.exit(0)
    
        
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
        conversation+=1
        scene_dos +=1
        
    if sakshi_two == 0 and sakshi_one == 1 and conversation == 4:
        study.description = 'You may now look under the sofa, in the bookshelf, and in the desk. Maybe there\'s some evidence in here.'
    
    if leng_two == 0 and leng_one == 1 and conversation == 4:
        kitchen.description = 'You may search in the cupboard, in the sink, or in the fridge. Could there be something incriminating here?'
    
    if andres_two == 0 and andres_one == 1 and conversation == 4:
        garden.description = 'You can check out the area behind the trees, in the bushes, or in the gazebo. There might be something intresting here.'               
    
    if message_end == 1:
        bedroom.description = 'You are allowed to check out the victim\'s purse, drawers, and trashcan.'
    
    if gabbu == 1:
        front_yard.description = 'So much trash... Mind checking out the trashcan?'
         
    if yog == 1:
        study.description = 'You may examine the pen, glass, and chair for Sakshi\'s prints.'
        living_room.description = 'You are now allowed to examine the pen, vase, and desk in the room for Bree\'s prints.'
        kitchen.description = 'You\'re able to check out the fridge, glass, and vase for Leng\'s prints.'
        garden.description = 'Find Andres\'s prints by examining his clarinet, a pop tart wrapper, and a bench.'
    
                                                                                                                                                                                                                            
        
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
    
    elif user_command =='save':
        save()
    elif user_command =='load':
        load()
    
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
        
    elif node == kitchen and p_win == False and conversation <=4:
        print '\nThere is a piece of paper on the floor. Would you like to pick it up?'
        if user_command in ['yes', 'y', 'yeah', 'ye', 'yea', 'ya']:
            anagram()
        elif user_command in ['no', 'nope', 'n']:
            print 'Well, okay. That\'s your decision. Anything could help this case. If you\'re going to be negligent, we might as well drop you. Sorry!'
            sys.exit(0)
        
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
                print('\n')
                print('Gabriella: "Which conversation do you wanna read?"\n\
- Leng\n\
- Andres\n\
- Unknown')
                
                break
                
        if life<=0:
            print('Gabriella: "Ha! Come back and try again."')




                
    
    
    def riddletwo():
        key = 'poison'
            #Time = 20 seconds; if they don\'t leave in time, lose game.
        riddle = 'There is a type of beverage,\n\
one that is herbal; it was served to our victim.\n\
however there may have been a substance;\n\
one quite deadly to the human body --\n\
normally packaged in a bottle,\n\
a skull donned on its tag.\n\
What is it?'
    
        print riddle
        
        user_riddle_guess = raw_input('Take a guess:\n')
        if user_riddle_guess.strip().lower() == key:
            print 'You have guessed correctly;\n\
Press "enter" to continue.'   
            user_riddle_guess_two = raw_input('> ')
            if user_riddle_guess_two.strip() == '':
                pic_2.pick_up(user_inventory)
                return ''
            
        else:
            print 'Sorry. That\'s not the answer.\n'
            print 'Unfortunately your negligence has caused the police to drop you from this case. Sorry!'
            sys.exit(0) 
                

    def financial_riddle():
        while paperwork not in user_inventory.inventory:
            print  
            
    a = ['search cupboard', 'cupboard']
    b = ['search desk', 'desk']
    c = ['search gazebo', 'gazebo']
    
    if sakshi_act == 0 and user_command == 'search' and node == study and sakshi_one>0 and sakshi_two ==0 and scene_dos == 1:
        s_scene_dos +=1 
        
    while financia_riddle == False and node == study and sakshi_two ==0 and sakshi_one >0 and s_scene_dos == 1:
        user_command_2 = raw_input('> ')
        if user_command_2 in b:
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
        it is Bree. Press "enter" to continue and see\n\
        what you find.'   
                user_riddle_guess_two = raw_input('> ')
                if user_riddle_guess_two.strip() == '':
                    paperwork.pick_up(user_inventory)
                    financia_riddle = True
                    print riddle_win
                    print('\n')
                    print(sakshi_2)
                    sakshi_two+=1
                    break
                    
                    
            else:
                print 'Sorry. That\'s not who it is.\n'
                print 'You and Liam quickly cover your ears.\n\
Liam: "What is that horrible ringing noise?!"\n\
You: "We must have set off an alarm when we tried opening the desk lock!\n\
Liam: "What do we do?!"\n\
You: "I don\'t know!"\n\
\n\
Unfortunately Sakshi ended up calling the police, in which your father arrived at the scene. Upset with your negligence, he decided to put someone else on the case. Sorry!'
                sys.exit(0)
            
        elif 'under sofa' in user_command_2:
            print(sofa)
            
        elif 'bookshelf'in user_command_2:
            print(bookshelf)
        
        elif user_command_2 in ['q', 'quit', 'exit']:
            sys.exit(0)
        
    if a_scene_dos == 0 and user_command == 'search' and node == garden and andres_one>0 and andres_two ==0 and scene_dos == 1:
    
        a_scene_dos +=1 
        
        
    while game_one == False and node == garden and andres_one >0 and andres_two == 0 and a_scene_dos==1:
        user_command_3 = raw_input('> ')
        if user_command_3 in c:
            word = 'temper tantrum'
            ana = 'Tamer Tempt Run'
            guessed = False
            print 'Unscramble this anagram:\n'
            print ana
            user_guesses = 0
            while guessed == False:
                user_guess = raw_input('> ')
                if user_guess.lower() == word:
                    print 'You guessed it!'
                    guessed = True
                    game_one = True
                    print(andres_2)
                    andres_two+=1
                    
                else:
                    print 'Guess again!'
                    user_guesses +=1
                    
                if user_guesses == 2:
                    user_hint = raw_input('Need a hint?\n')
                    if user_hint in ['yes', 'ye', 'y', 'yea','ya', 'yeah', 'yah']:
                        print 'It\'s something that occurs when, usually, a small and stubborn child gets very upset.'
                        
                    
                if user_guesses >=4:
                    print 'You ran out of guesses! Well, I guess you aren\'t that competent to work on this case. Sorry, but, we\'re going to call another detective to find out what actually happened here.'
                    sys.exit(0)
            
        elif 'bushes' in user_command_3:
            print(bushes)
            
        elif 'trees' in user_command_3:
            print(trees)
            
        elif user_command_3 in ['q', 'quit', 'exit']:
            sys.exit(0)
            
    
        
    if leng_act == 0 and user_command == 'search' and node == kitchen and leng_one>0 and leng_two ==0 and scene_dos == 1:

        l_scene_dos +=1 
        
    while game_two == False and node == kitchen and leng_two == 0 and leng_one >0 and l_scene_dos == 1:
        user_command_4 = raw_input('> ')
        if user_command_4 in a:
            key = 'poison'
            #Time = 20 seconds; if they don\'t leave in time, lose game.
            riddle = 'There is a type of beverage,\n\
one that is herbal; it was served to our victim.\n\
however there may have been a substance;\n\
one quite deadly to the human body --\n\
normally packaged in a bottle,\n\
a skull donned on its tag.\n\
What is it?'
    
            print riddle
        
            user_riddle_guess = raw_input('Take a guess:\n')
            if user_riddle_guess.strip().lower() == key:
                print 'You have guessed correctly;\n\
Press "enter" to continue.'   
                user_riddle_guess_two = raw_input('> ')
                if user_riddle_guess_two.strip() == '':
                    game_two = True
                    print(cupboard)
                    print('\n')
                    print(leng_2)
                    leng_two +=1
                    break
            
            else:
                print 'Sorry. That\'s not the answer.\n'
                print 'Unfortunately your negligence has caused the police to drop you from this case. Sorry!'
                sys.exit(0) 
            
        elif 'fridge' in user_command_4:
            print(fridge)
        
        elif 'sink' in user_command_4:
            print(sink)
            
        elif user_command_4 in ['q', 'quit', 'exit']:
            sys.exit(0)
            
        
            
    if node == living_room and bree_two == 0 and bree_one >0:
        print(bree_2)
        bree_two +=1
        
    if node == lab and leng_two == 1 and bree_two == 1 and andres_two == 1 and sakshi_two == 1:
        print(gabi_4)
        print('\n')
        print('Gabriella: "Which conversation do you wanna read?"\n\
- Leng\n\
- Andres\n\
- Unknown')
        
    if 'leng' in user_command and messages_read<3 and node == lab and leng_two == 1 and bree_two == 1 and andres_two == 1 and sakshi_two == 1:
        print(message_leng)
        leng_message +=1
        if leng_message == 1:
            messages_read +=1
    
    if 'andres' in user_command and messages_read<3 and node == lab and leng_two == 1 and bree_two == 1 and andres_two == 1 and sakshi_two == 1:
        print(message_andres)
        andres_message +=1
        if andres_message == 1:
            messages_read +=1
    
    if 'unknown' in user_command and messages_read<3 and node == lab and leng_two == 1 and bree_two == 1 and andres_two == 1 and sakshi_two == 1:
        print(message_unknown)
        unknown_message +=1
        if unknown_message ==1:
            messages_read +=1
                
    if messages_read == 3 and node == lab and message_end == 0:
        print(end_messages)
        message_end+=1
        
        
    if node == bedroom and message_end == 1 and trashg == 0 and user_command in ['trashcan', 'check trash', 'check trashcan', 'check out trashcan']:
        print(trashcan)
        trashg+=1
    
    elif node == bedroom and message_end == 1 and trashg == 0 and user_command in ['purse', 'look in purse', 'check purse']:
        print(purse)
        
    elif node == bedroom and message_end == 1 and trashg == 0 and user_command in ['drawers', 'check drawers', 'look in drawers']:
        print(drawers)
        
    if node == study and message_end == 1 and s3 == 0:
        print(sakshi_3)
        s3+=1
    
    elif node == kitchen and message_end == 1 and l3 == 0:
        print(leng_3)
        l3+=1
        
    elif node == living_room and message_end == 1 and b3 == 0 and l3 == 1:
        print(bree_3)
        b3 +=1
        
    elif node == garden and message_end == 1 and a3 == 0:
        print(andres_3)
        a3+=1
        
    elif node == lab and s3 == 1 and l3 ==1  and a3 ==1 and b3 ==1 and gabbu == 0 and trashg == 1:
        print(gab)
        gabbu+=1
        
    if gabbu == 1 and node == front_yard and user_command in ['trashcan', 'check trashcan']:
        word = 'Painkillers'
        ana = 'A Sniper Kill'
        guessed = False
        print 'Unscramble this anagram:\n'
        print ana
        user_guesses = 0
        while guessed == False:
            user_guess = raw_input('> ')
            if user_guess == word:
                print 'You guessed it!'
                guessed = True
                print trashed
                break
                
            else:
                print 'Guess again!'
                user_guesses +=1
                
            if user_guesses == 2:
                user_hint = raw_input('Need a hint?\n')
                if user_hint in ['yes', 'ye', 'y', 'yea','ya', 'yeah', 'yah']:
                    print 'It\'s something that is commonly taken to reduce pain in the body.'
                    
                
            if user_guesses >=4:
                print 'You ran out of guesses! Well, I guess you aren\'t that competent to work on this case. Sorry, but, we\'re going to call another detective to find out what actually happened here.'
                sys.exit(0)
        
    if gabbu == 1 and node == study and s4 == 0:
        print(sakshi_4)
        s4+=1
    
    if gabbu == 1 and node == living_room and b4 == 0:
        print(bree_4)
        b4+=1
        
    if gabbu == 1 and node == kitchen and l4 == 0:
        print(leng_4)
        l4+=1
    
    if gabbu == 1 and node == garden and a4 == 0:
        print(andres_4)
        a4+=1
        
    if a4 == 1 and l4 == 1 and s4 == 1 and b4 == 1 and node == lab and yog == 0:
        print(gabu)
        yog +=1
        
    if yog == 1 and node == study:
        if user_command in ['pen', 'examine pen'] and sp == 0:
            print(s_pen)
            sp+=1
        elif user_command in ['glass', 'examine glass'] and sp == 0:
            print(s_glass)
        elif user_command in ['chair', 'examine chair'] and sp == 0:
            print(s_chair)
        
    if yog == 1 and node == kitchen:
        if user_command in ['glass', 'examine glass'] and lg == 0:
            print(l_glass)
            lg+=1
        elif user_command in ['vase', 'examine vase'] and lg == 0:
            print(l_vase)
        elif user_command in ['fridge', 'examine fridge'] and lg == 0:
            print(l_fridge)
               
    if yog == 1 and node == living_room:
        if user_command in ['vase', 'examine vase'] and bv == 0:
            print(b_vase)
            bv +=1
        elif user_command in ['pen', 'examine pen'] and bv == 0:
            print(b_pen)
        elif user_command in ['desk', 'examine desk'] and bv == 0:
            print(b_desk)
    
    if yog == 1 and node == garden:
        if user_command in ['clarinet', 'examine clarinet'] and ac == 0:
            print(a_clarinet)
            ac+=1
        elif user_command in ['pop tart', 'wrapper', 'pop tart wrapper', 'examine wrapper', 'examine pop tart wrapper'] and ac == 0:
            print(a_pop)
        elif user_command in ['bench', 'examine bench'] and ac == 0:
            print(a_pop)
            
    if ac == 1 and bv == 1 and sp == 1 and lg == 1 and node == lab and goy == 0:
        print(gaba)
        goy+=1
        
    if goy == 1 and node == police_office and chidad == 0:
        print(daddy)
        chidad +=1
    if chidad == 1 and node == garden and conf == 0:
        print(confess)
        conf+=1
        print('\n')
        print wrap_up
        sys.exit(0)
        
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

#-------------------------------------------------------------------------------
        
#Do dialogue in order this by continously calling the dialogue 'say' function
#Progress stories this way
        
#Win Conditions as a class to make sure that the person accomplished everything 
#before winning
#Series of red flags/conditionals to make sure that the tasks are completed        
        


#user_inventoryman

#Numerical Riddle (1982)

#Riddle

#user_inventoryman

#Riddle

#Numerical Riddle (Passcode = (0129))
    #- Tells you which digits you got correct and which you didn't
    #- 
    
#-------------------------------------------------------------------------------