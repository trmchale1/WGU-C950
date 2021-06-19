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

def greedy_func(temp_list):
    temp = []
    temp_list.sort(key = lambda x: float(x[2]))
    print(temp_list)
    temp.append(temp_list[0])
    x = temp[0][2]
    for i in range(len(temp_list)):
        if temp_list[i][2] == x and temp_list[i] not in temp:
            temp.append(temp_list[i])        
    print('Subgraph: ')
    print(temp)
    return temp
    
node = 'HUB'
while len(first_delivery) != 0:

    for p in first_delivery:
        for e in edges:
            if e[1].strip() == node and pack[p]["address"] == e[0] and float(e[2]) > 0.0 and p not in first_delivery_sorted:
                print("Package number : " + str(p) + " Current Location : " + node + " loc: " + e[0] + " loc: " + e[1] + " dist: " + e[2])
                temp.append((p,e[0],e[2]))
            elif e[0].strip() == node and pack[p]["address"] == e[1] and float(e[2]) > 0.0 and p not in first_delivery_sorted:
                print("Package number : " + str(p) + " Current Location : " + node + " loc: " + e[0] + " loc: " + e[1] + " dist: " + e[2])
                temp.append((p,e[1],e[2]))
    min_pair = greedy_func(temp)
    if isinstance(min_pair, list):
        for i in min_pair:
            first_delivery_sorted.append(i)
            node = i[1]
            if i[0] in first_delivery:
                first_delivery.remove(i[0])
    temp.clear()
    print('Final List: ')
    print(first_delivery_sorted)

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