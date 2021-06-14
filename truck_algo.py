from model import get_distances, get_schedule_deets, packs
from hash_table import HashTable

distances = get_distances()
deets = get_schedule_deets()
packages = packs()

print(deets)

hash_ = HashTable()  

first_delivery = []  
second_delivery = [] # leaves at 9:05, pack 6
final_delivery = [] # leaves at 10:20, pack 9

for p in packages:
    id_ = p
    address = packages[p]["address"]
    deadline = packages[p]["arrival"]
    city = packages[p]["city"]
    zip_ = packages[p]["zip"]
    weight = packages[p]["weight"]
    status = 'At HUB'

    value = [id_,address,deadline,city,zip_,weight,status]
    
    
    if p == 3:
        second_delivery.append(p)
    elif p == 6:
        second_delivery.append(p)
    elif p == 9:
        final_delivery.append(p)
    elif p == 13 or p == 14 or p == 15 or p == 16 or p == 19 or p == 20:
        first_delivery.append(p)
    elif p == 18 or p == 25 or p == 28 or p == 32:
        second_delivery.append(p)
    elif packages[p]["arrival"] == '10:30 AM':
        first_delivery.append(p)

        
print("First Truck inv: " + str(len(first_delivery)))
print("Second Truck inv: " + str(len(second_delivery)))
print("Third Truck inv: " + str(len(final_delivery)))

