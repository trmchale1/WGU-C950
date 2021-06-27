from model import get_distances, get_schedule_deets
import datetime
from calc_trip import get_hash_map

distances = get_distances()
deets = get_schedule_deets()

class Main:
    print('------------------------------')
    print('WGUPS Routing Program!')
    print('------------------------------\n')
    
    
    for i in range(0,40):
        print(get_hash_map().get_value(i))

    
    user_input = input("""
Get info for all packages at a particular time or type 'quit' to quit:
    1. 9:00 AM
    2. 10:00 AM
    3. 1:00 PM
""")

    while user_input is not 'quit':
        if user_input == '1':     
            print('Yay')
        elif user_input == 'quit':
            exit()
