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
    if len(temp_list) == 0:
        return
    else:
        temp.append(temp_list[0])
    x = temp[0][2]
    for i in range(len(temp_list)):
        if temp_list[i][2] == x and temp_list[i] not in temp:
            temp.append(temp_list[i])        
    return temp
    
node = 'HUB'
while len(first_delivery) != 0:
    for p in first_delivery:
        for e in edges:
            if e[1].strip() == node and pack[p]["address"] == e[0] and float(e[2]) > 0.0 and p not in first_delivery_sorted:
                temp.append((p,e[0],e[2]))
            elif e[0].strip() == node and pack[p]["address"] == e[1] and float(e[2]) > 0.0 and p not in first_delivery_sorted:
                temp.append((p,e[1],e[2]))
    min_pair = greedy_func(temp)
    if isinstance(min_pair, list):
        for i in min_pair:
            first_delivery_sorted.append(i)
            node = i[1]
            if i[0] in first_delivery:
                first_delivery.remove(i[0])
    temp.clear()
    
second_delivery_sorted = []

node = 'HUB'
while len(second_delivery_sorted) != 14:
    for p in second_delivery:
        for e in edges:
            if e[1].strip() == node and pack[p]["address"] == e[0] and float(e[2]) > 0.0 and p not in second_delivery_sorted:
                    temp.append((p,e[0],e[2]))
            elif e[0].strip() == node and pack[p]["address"] == e[1] and float(e[2]) > 0.0 and p not in second_delivery_sorted:
                    temp.append((p,e[1],e[2]))
        minimum_pair = greedy_func(temp)
    if isinstance(minimum_pair, list):
        for i in minimum_pair:
            second_delivery_sorted.append(i)
            node = i[1]
            if i[0] in second_delivery:
                second_delivery.remove(i[0])
    temp.clear()
    
third_delivery_sorted = []    
node = 'HUB'
while len(third_delivery_sorted) != 14:
    for p in third_delivery:
        for e in edges:
            if e[1].strip() == node and pack[p]["address"] == e[0] and float(e[2]) > 0.0 and p not in third_delivery_sorted:
                temp.append((p,e[0],e[2]))
            elif e[0].strip() == node and pack[p]["address"] == e[1] and float(e[2]) > 0.0 and p not in third_delivery_sorted:
                temp.append((p,e[1],e[2]))
    min_pair = greedy_func(temp)
    if isinstance(min_pair, list):
        for i in min_pair:
            third_delivery_sorted.append(i)
            node = i[1]
            if i[0] in third_delivery:
                third_delivery.remove(i[0])
    temp.clear()

print(second_delivery_sorted)

    
def get_first_delivery_sorted():
    return first_delivery_sorted

def get_second_delivery_sorted():
    return second_delivery_sorted

def get_third_delivery_sorted():
    return third_delivery_sorted
