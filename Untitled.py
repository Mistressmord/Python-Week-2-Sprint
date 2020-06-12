#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def die_roll():
    import random
    print ('Welcome to our Dice Rolling Simulator')
        play_game = input('Are you ready to roll the dice? Enter Yes or No').lower()
        if play_game == 'yes' or play_game == 'y':
            roll_dice = input('How many die do you want to roll?')
            while roll_dice != 0:
                player_roll = random.randint(1, 6)
                print(player_roll)
                roll_dice = (roll_dice-1)
        else:
            print('You chose not to start the game. Type Yes if you want to start' )
die_roll()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




