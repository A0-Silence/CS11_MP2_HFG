import pyglet
import interface, entities

#Ingredients = ['ham', 'cheese', 'mayonnaise', 'bread', 'chicken', 'fish', 
#    'soy sauce', 'garlic', 'salt & pepper', 'butter', 'leek', 'meat', 'parsley', 
#    'potatoes', 'onion', 'eggs', 'flour', 'sugar', 'milk', 'chocolate chips', 'pasta', 
#    'oranges', 'raspberries', 'strawberries', 'banana', 'lime', 'vanilla', 'mangoes']
Ingredients = ['ing1', 'ing2', 'ing3'] #removed 'null' for now
#########################################################################################
Drinks = ['orange juice', 'mango shake', 'four-fruit shake', 'strawberry cheesecake shake', 
    'home-made cola']
Food = ['test food']
#Food = ['ham sandwich', 'chicken sandwich', 'baked fish', 'salt crust', 'skillet steak', 
#    'pork chop', 'basic cupcakes', 'basic cookies', 'stir fry', 'mac and cheese']
#########################################################################################

Recipe = {
    #Format:
    #    <FOOD> : (COOKING PLACE , INGREDIENTS as tuple)

    #Salad
    'test food' : ('pot',
                  ('ing1', 'ing2', 'ing3')),
    #Sandwich
    'ham sandwich' : ('microwave',
                        ('bread', 'ham', 'cheese', 'mayonnaise')), 
    'chicken sandwich' : ('microwave',
                        ('bread', 'chicken', 'mayonnaise')), 

    #Fish
    'baked fish' : ('oven',
                        ('fish', 'soy sauce', 'garlic', 'salt & pepper')), 
    'salt crust' : ('oven',
                        ('fish', 'salt & pepper', 'salt & pepper', 'butter', 'garlic', 'leek')), 

    #Meat
    'skillet steak' : ('stove',
                        ('meat', 'garlic', 'salt & pepper', 'butter', ' parsley', 'potatoes')),
    'pork chop' : ('stove',
                        ('meat', 'garlic', 'salt & pepper', 'onion')), 

    #Pastries
    'basic cupcakes' : ('oven',
                        ('eggs', 'flour', 'sugar', 'butter', 'milk')), 
    'basic cookies' : ('oven',
                        ('eggs', 'flour', 'sugar', 'butter', 'chocolate chips')), 

    #Pasta
    'stir fry' : ('stove',
                        ('pasta', 'chicken', 'soy sauce', 'garlic', 'parsley')), 
    'mac and cheese' : ('stove',
                        ('pasta', 'milk', 'cheese')), 

    #Drinks
    'orange juice' : ('blender',
                        ('sugar', 'oranges')),
    'mango juice' : ('blender',
                        ('sugar', 'milk', 'mangoes')),
    'strawberry cheesecake shake' : ('blender',
                        ('sugar', 'cheese', 'strawberries', 'vanilla')),
    'four-fruit shake' : ('blender',
                        ('oranges', 'raspberries', 'strawberries', 'banana', 'sugar')),
    'home-made cola' : ('blender',
                        ('sugar', 'sugar', 'lime', 'lime', 'vanilla', 'oranges'))
}

def itemEat(item):
    if(item in Drinks or item in Food):
        entities.player.satiety += 40
        interface.actionText.text = "Finally. Some good fucking food."
    elif(item in Ingredients):
        entities.player.satiety += 5
        interface.actionText.text = "Needs lamb sauce. And other ingredients."
    else:
        interface.actionText.text = "You ate it. Nothing happened."

def itemCook(item):
    if(item in Drinks or item in Food):
        entities.player.satiety += 40
        interface.actionText.text = "You ate the thing, instead of cooking it more."
    elif(item in Ingredients):
        interface.actionText.text = "You added the {} into the cooking device."
        del interface.Craving.Ingredients[interface.Craving.Ingredients.index(item)]
        if(len(interface.Craving.Ingredients) == 0):
            intergace.Craving.crave()
    else:
        interface.actionText.text = "The {} burned out of existence."