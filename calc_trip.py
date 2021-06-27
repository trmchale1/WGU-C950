import datetime
from calc_routes import get_first_delivery_sorted, get_second_delivery_sorted, get_third_delivery_sorted
import time
from model import get_distances, get_schedule_deets, packs
from hash_table import HashMap

first = get_first_delivery_sorted()
second = get_second_delivery_sorted()
third = get_third_delivery_sorted()


# •   package ID number
#•   delivery address
#arrival•   delivery deadline
#•   delivery city
#•   delivery zip code
#•   package weight
#•   delivery status (e.g., delivered, en route)
# pull in packages, use in loops, save data to a list and hash

hash_map = HashMap()

pack = packs()

s = datetime.timedelta(hours=8,minutes=0,seconds=0)

dist1 = 0
mps = .005 
d = 0
print(' START --- HUB ', s)
past = 'x'
calc_time = s
for i in range(len(first)):    
    if first[i][1] != past:
        time = float(first[i][2]) / mps
        calc_time = calc_time + datetime.timedelta(seconds=time)
        d = d + 1
        dist1 = dist1 + float(first[i][2])
    print('Destination: ' + str(d) + ' --- Package ' + str(first[i][0]) +' --- Address: ' + str(first[i][1]) + ' --- Distance: ' + str(first[i][2]) + ' Time to Destination: ' + str(calc_time))
    pack_id = first[i][0]
    del_add = first[i][1]
    arr = pack[first[i][0]]["arrival"]
    city = pack[first[i][0]]["city"]
    z = pack[first[i][0]]["zip"]
    pack_w = pack[first[i][0]]["weight"]
    del_status = 'DELIVERED'
    del_time = calc_time
    past = first[i][1]
    value = [pack_id,del_add,arr,city,z,pack_w,del_status,str(calc_time),'1']
    hash_map.insert(pack_id,value)
print(dist1)    
dist2 = 0    
s2 = datetime.timedelta(hours=9,minutes=5,seconds=0)    
mps = .005 
d = 0
print(' START --- HUB ', s2)
past = 'x'
calc_time = s2
for i in range(len(second)-1):    
    if second[i][1] != past:
        time = float(second[i][2]) / mps
        calc_time = calc_time + datetime.timedelta(seconds=time)
        d = d + 1
        dist2 = dist2 + float(second[i][2])
    print('Destination: ' + str(d) + ' --- Package ' + str(second[i][0]) +' --- Address: ' + str(second[i][1]) + ' --- Distance: ' + str(second[i][2]) + ' Time to Destination: ' + str(calc_time))
    pack_id = second[i][0]
    del_add = second[i][1]
    arr = pack[second[i][0]]["arrival"]
    city = pack[second[i][0]]["city"]
    z = pack[second[i][0]]["zip"]
    pack_w = pack[second[i][0]]["weight"]
    del_status = 'DELIVERED'
    del_time = calc_time
    past = second[i][1]
    value = [pack_id,del_add,arr,city,z,pack_w,del_status,str(calc_time),'2']
    hash_map.insert(pack_id,value)
    past = second[i][1]    

print(dist2)        
dist3 = 0    
s3 = datetime.timedelta(hours=10,minutes=20,seconds=0)    
mps = .005 
d = 0
print(' START --- HUB ', s3)
past = 'x'
calc_time = s3
for i in range(len(third)-1):    
    if third[i][1] != past:
        time = float(third[i][2]) / mps
        calc_time = calc_time + datetime.timedelta(seconds=time)
        d = d + 1
        dist3 = dist3 + float(third[i][2])
    print('Destination: ' + str(d) + ' --- Package ' + str(third[i][0]) +' --- Address: ' + str(third[i][1]) + ' --- Distance: ' + str(third[i][2]) + ' Time to Destination: ' + str(calc_time))
    pack_id = third[i][0]
    del_add = third[i][1]
    arr = pack[third[i][0]]["arrival"]
    city = pack[third[i][0]]["city"]
    z = pack[third[i][0]]["zip"]
    pack_w = pack[third[i][0]]["weight"]
    del_status = 'DELIVERED'
    del_time = calc_time
    past = third[i][1]
    value = [pack_id,del_add,arr,city,z,pack_w,del_status,str(calc_time),'3']
    hash_map.insert(pack_id,value)
    past = third[i][1]      
print(dist3)    

def get_hash_map():
        return hash_map