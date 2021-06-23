def sort_for_delivery(nested_dictionary):    
    dropoffs = []
    notes = []
    for key in nested_dictionary.keys():
        for k in nested_dictionary[key].keys(): 
            for values in nested_dictionary[key].values():
                if values == "9:00 AM":
                    dropoffs.append([key,values])
                elif values == "10:30 AM":
                    dropoffs.append([key,values])
    dropoffs = sorted(dropoffs)
    dropoffs = [dropoffs[i] for i in range(len(dropoffs)) if i == 0 or dropoffs[i] != dropoffs[i-1]]
    for key in nested_dictionary.keys():
        for k in nested_dictionary[key].keys():
            if k == "notes":
                notes.append([key,nested_dictionary[key][k]])
    dropoffs.extend(notes)
    return dropoffs 

WGUPS_PACK = { 1 : { "address" : "195 W Oakland Ave", "city":"Salt Lake City","zip":"84115","arrival" : "10:30 AM","weight" : "21"},
2 : {"address" : "2530 S 500 E", "city":"Salt Lake City","zip":"84106","arrival" : "EOD", "weight":"44"},
3 : {"address" : "233 Canyon Rd","city":"Salt Lake City","zip":"84103","arrival" : "EOD", "weight" : "2", "notes" : "Can only be on truck 2"} ,
4 : {"address" : "380 W 2880 S", "city":"Salt Lake City","zip":"84115","arrival" : "EOD", "weight" :     "4" },
5 :  { "address" : "410 S State St", "city":"Salt Lake City","zip":"84111","arrival" : "EOD", "weight" : "5" },
6 : { "address" : "3060 Lester St","city":"West Valley City","zip":"84119","arrival" : "10:30 AM", "weight" :"88","notes" : "Delayed on flight---will not arrive to depot until 9:05 am" },
7 : { "address" : "1330 2100 S", "city":"Salt Lake City","zip":"84106","arrival" : "EOD", "weight" : "8" } ,
8 : { "address" : "300 State St", "city":"Salt Lake City","zip":"84103", "arrival" : "EOD", "weight" : "9" } ,
9 : {"address" : "300 State St","city":"Salt Lake City","zip":"84103", "arrival" : "EOD", "weight" : "2", "notes" : "Wrong address listed" },
10 : {"address" : "600 E 900 South","city":"Salt Lake City","zip":"84105", "arrival" : "EOD", "weight" : "1" } ,
11 : { "address" : "2600 Taylorsville Blvd","city":"Salt Lake City","zip":"84118", "arrival" : "EOD", "weight" : "1" } ,
12 : {"address" : "3575 W Valley Central", "city":"West Valley City","zip":"84119","arrival" : "EOD", "weight" : "1" },
13 : {"address" : "2010 W 500 S","city":"Salt Lake City","zip":"84104", "arrival" : "10:30 AM", "weight" : "2" },
14 : {"address" : "4300 S 1300 E","city":"Millcreek","zip":"84117", "arrival" : "10:30 AM", "weight" : "88", "notes" : "Must be delivered with 15, 19" },
15 : {"address" : "4580 S 2300 E","city":"Holladay","zip":"84117", "arrival" : "9:00 AM", "weight" : "4"},
16 : {"address" : "4580 S 2300 E","city":"Holladay","zip":"84117", "arrival" : "10:30 AM", "weight" : "88", "notes" : "Must be delivered with 13, 19" },
17 : {"address" : "3148 S 1100 W","city":"Salt Lake City","zip":"84119", "arrival" : "EOD", "weight" : "2"},           
18 : {"address" : "1488 4800 S","city":"Salt Lake City","zip":"84123", "arrival" : "EOD", "weight" : "6", "notes" : "Can only be on truck 2" },
19 : {"address" : "177 W Price Ave","city":"Salt Lake City","zip":"84115", "arrival" : "EOD", "weight" : "37"},
20 : {"address" : "3595 Main St","city":"Salt Lake City","zip":"84115", "arrival" : "10:30 AM", "weight" : "37", "notes" : "Must be delivered with 13, 15" },
21 : {"address" : "3595 Main St","city":"Salt Lake City","zip":"84115", "arrival" : "EOD", "weight" : "3"},
22 : {"address" : "6351 South 900 East","city":"Murray","zip":"84121", "arrival" : "EOD", "weight" : "2"},
23 : {"address" : "5100 South 2700 West","city":"Salt Lake City","zip":"84118", "arrival" : "EOD", "weight" : "5"},
24 : {"address" : "5025 State St","city":"Murray","zip":"84107", "arrival" : "EOD", "weight" : "7"},
25 : {"address" : "5383 S 900 East #104","city":"Salt Lake City","zip":"84117", "arrival" : "10:30 AM", "weight" : "7", "notes" : "Delayed on flight---will not arrive to depot until 9:05 am"},
26 : {"address" : "5383 S 900 East #104", "city":"Salt Lake City","zip":"84117","arrival" : "EOD", "weight" : "25"},
27 : {"address" : "1060 Dalton Ave S", "city":"Salt Lake City","zip":"84104","arrival" : "EOD", "weight" : "5"},
28 : {"address" : "2835 Main St","city":"Salt Lake City","zip":"84115", "arrival" : "EOD", "weight" : "7", "notes" : "Delayed on flight---will not arrive to depot until 9:05 am"},
29 : {"address" : "1330 2100 S", "city":"Salt Lake City","zip":"84106","arrival" : "10:30 AM", "weight" : "2"},
30 : {"address" : "300 State St", "city":"Salt Lake City","zip":"84103","arrival" : "10:30 AM", "weight" : "1"},
31 : {"address" : "3365 S 900 W", "city":"Salt Lake City","zip":"84119","arrival" : "10:30 AM", "weight" : "1"},
32 : {"address" : "3365 S 900 W", "city":"Salt Lake City","zip":"84119","arrival" : "EOD", "weight" : "1", "notes" : "Delayed on flight---will not arrive to depot until 9:05 am"},
33 : {"address" : "2530 S 500 E", "city":"Salt Lake City","zip":"84106","arrival" : "EOD", "weight" : "1"},
34 : {"address" : "4580 S 2300 E","city":"Holladay","zip":"84117", "arrival" : "10:30 AM", "weight" : "2"},
35 : {"address" : "1060 Dalton Ave S","city":"Salt Lake City","zip":"84104", "arrival" : "EOD", "weight" : "88"},
36 : {"address" : "2300 Parkway Blvd","city":"West Valley City","zip":"84119", "arrival" : "EOD", "weight" : "88", "notes" : "Can only be on truck 2"},
37 : {"address" : "1060 Dalton Ave S","city":"Salt Lake City","zip":"84111", "arrival" : "10:30 AM", "weight" : "2"},
38 : {"address" : "410 S State St","city":"Salt Lake City","zip":"84111", "arrival" : "EOD", "weight" : "9", "notes" : "Can only be on truck 2"},
39 : {"address" : "2010 W 500 S", "city":"Salt Lake City","zip":"84104","arrival" : "EOD", "weight" : "9"},
40 : {"address" : "380 W 2880 S", "city":"Salt Lake City","zip":"84115","arrival" : "10:30 AM", "weight" : "45"}}
o = open('dist.csv')
addresses = []
edges = []
for line in o:
    word = line.split(',')
    for i in range(1,len(word)-1):
        addresses.append(word[0])
        edges.append(word[i])
add_dedup = [] 
[add_dedup.append(x) for x in addresses if x not in add_dedup]

del add_dedup[0]
del add_dedup[0]


edge_dedup = []
for e in edges:
    if not e:
        pass
    else:
        edge_dedup.append(e)
        

del edge_dedup[0]
del edge_dedup[0]
del edge_dedup[0]
del edge_dedup[0]
del edge_dedup[0]
del edge_dedup[0]
del edge_dedup[0]
del edge_dedup[0]
del edge_dedup[0]
del edge_dedup[0]
del edge_dedup[0]
del edge_dedup[0]
del edge_dedup[0]
del edge_dedup[0]
del edge_dedup[0]
del edge_dedup[0]
del edge_dedup[0]
del edge_dedup[0]
del edge_dedup[0]
del edge_dedup[0]
del edge_dedup[0]
del edge_dedup[0]
del edge_dedup[0]
del edge_dedup[0]
del edge_dedup[0]
del edge_dedup[0]
del edge_dedup[0]


edge_list = []
count = 1
index = 0

for e in edge_dedup:
    temp = (add_dedup[count],add_dedup[index],e)
    edge_list.append(temp)
    index = index + 1
    if e == str(0.0):
        count = count + 1
        index = 0

scheduling_details = sort_for_delivery(WGUPS_PACK)
#print(edge_list)
#print(scheduling_details)
def get_distances():
    return edge_list
def get_schedule_deets():
    return scheduling_details
def packs():
    return WGUPS_PACK
