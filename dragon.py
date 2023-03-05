import random
import time

def display_intro():
    print('''Hi,Group C
You are in the Kingdom of Dragons.  In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is hungry and will eat you on sight.''')



def choose_cave(): #will return 1 or 2
    cave='' #local variable with empty string
    while cave!='1' and cave!='2':
        print('(Which cave will you go into),Enter cave 1 or 2 : ')
        cave=input()
    return cave
display_intro()
        
cave_number=choose_cave()#will return 1 or 2

print('You are entering cave',cave_number)

def check_cave(chosen_cave):
    print('You approach the cave...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! ')
    print('He opens his jaws and...')
    time.sleep(2)
    friendlyCave = random.randint(1, 2) # 1 or 2
    if int(chosen_cave)==friendlyCave:
        print("Gives you his treasure!")
    else:
        print("Gobbles you down!")
check_cave(cave_number)

display_intro()
cave_number = choose_cave()   # will return 1 or 2
print('You are entering cave ', cave_number)
check_cave(cave_number)
        

    
    
