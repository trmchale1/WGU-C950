from model import get_distances, get_schedule_deets, packs
from hash_table import HashMap

distances = get_distances()
deets = get_schedule_deets()
packages = packs()
hash_ = HashMap()  
first_delivery = []  
second_delivery = [] # leaves at 9:05, pack 6
third_delivery = [] # leaves at 10:20, pack 9
fourth_delivery = [] # break 3 in half

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
        third_delivery.append(p)
    elif p == 18 or p == 25 or p == 28 or p == 32:
        second_delivery.append(p)
        for edge in distances:
            if address == edge[0] and edge[0] != edge[1] and float(edge[2]) < 5:
                for q in packages:
                    if edge[1] == packages[q]['address'] and not q in first_delivery and not q in second_delivery: 
                        second_delivery.append(q)

    elif p == 13 or p == 14 or p == 15 or p == 16 or p == 19 or p == 20:
        first_delivery.append(p)
        for edge in distances:
            if address == edge[0] and edge[0] != edge[1] and float(edge[2]) < 2.1:
                for q in packages:
                    if edge[1] == packages[q]['address'] and not q in first_delivery and not q in second_delivery:
                        first_delivery.append(q)
    


        #hash_.insert(id,value)     
            
first_delivery.remove(32)
second_delivery.append(30)
first_delivery.append(34)
first_delivery.append(37)
first_delivery.append(40)
second_delivery.append(38)
first_delivery.remove(37)
first_delivery.remove(28)


for i in range(1,40):
    if not i in first_delivery and not i in second_delivery:
        third_delivery.append(i)

third_delivery.remove(9)



        
def get_first_delivery():
    return first_delivery

def get_second_delivery():
    return second_delivery

def get_third_delivery():
    return third_delivery

def get_hash_map():
    return hash_