import random
# import tkinter
restart = "Yes"

# removed [] to make more acssesable
state_capitals= {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Neveda': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakoda': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'  
} # sets name as input
player_name =  input("Ready to boogie what's your name? > ")
print("ready for this {}".format(player_name) + 'let us Boogie')


States=list(state_capitals.keys())# sets list with key
print ('Your bitch ass still needs to learn US States and Capitals. 50 mf rounds. Enter exit to punk out.')
point=0 
for i in range(5): # sets up rounds
    state=random.choice(States) 
    capital = state_capitals[state]
    user_guess = input('what is the capital of %s?'%state + 'your going to get it wrong {}. '.format(player_name))
    if user_guess.lower() == 'exit': # lets you to exit 
        break
    elif user_guess.title() == capital:
        point+=1
        print('Want A Cookie! point to player %d' %point)
    else:
        print('You suck, The capital of {} is {}.'.format(state,capital))
print('We are done here all you got right was %d, You are dead inside' %point) # end game
restart = input("Do you want to restart the game {}? Yes or No ".format(player_name))
if restart == 'yes':
    main()
# I changed the stucture of the data for easy acsess then removed the need for multipul
# list then set the hole thing up in a def to call it all back if user input is yes
# I liked this sulution best as it is easyer to understand with less steps
# then added player name so i could pass it in inputs with text
# i had planed on adding this to Tkinter gui but didn't want refactor for wigits insted of inputs
# also made use of the 42 of python %d place holder for whatever thats always fun
# also I set rounds using range to stop from having to play all 50 before game end 
# and set up an exit to the game if you give up early 