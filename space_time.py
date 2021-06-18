from model import get_distances, get_schedule_deets, packs
from hash_table import HashMap
from fill_trucks import get_first_delivery, get_second_delivery, get_third_delivery

first_delivery = get_first_delivery()
second_delivery = get_second_delivery()
third_delivery = get_third_delivery()

edges = get_distances()

pack = packs()
first_delivery_sorted = []
temp = []
ind = []

#get the distances from the hub and choose the min as the fist destination
node = 'HUB'
#while not first_delivery:
for p in first_delivery:
    for e in edges:
        if e[1].strip() == node:
            print(p,pack[p]["address"],e[0],e[2])
            temp.append((p,e[0],e[2]))
min_pair = min(temp, key = lambda t: t[2])
first_delivery_sorted.append(min_pair[2])
print(min_pair[0])

'''   
print(first_delivery)
print(first_delivery_sorted)
temp.clear()    
count = 0
# iterate over edges to match the next first_delivery index to build a list, then find the min, the next destination, then add to the sorted list
for i in first_delivery_sorted:
    for e in edges:
        if (i[1] == e[0] or i[1] == e[1]) and e[2] > i[2]:
            print(count)
            print(i,e[0],e[1],e[2])
            count = count + 1
             and e[1].strip() == node
'''