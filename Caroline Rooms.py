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

front_yard = Room('Mansion\'s Front Yard', 'A lush green lawn spreads like a blanket in front of a massive and ornately structured mansion, the view only marred by splashes of trash.\n\
From here you can go to:\n\
    - study\n\
    - kitchen\n\
    - bedroom\n\
    - living room\n\
    - garden\n\
    - police office\n\
    - lab', pill_bottle, None, None, None)

global node 
node = police_office 