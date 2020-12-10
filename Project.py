import os
import csv
import datetime

manlist = []
pricelist = []
servlist = []

# CSV files read and lists made
with open('ManufacturerList.csv', 'r') as csvfile1:
    manlist_reader = csv.reader(csvfile1)
    for i in manlist_reader:
        manlist.append(i)

with open('PriceList.csv', 'r') as csvfile2:
    pricelist_reader = csv.reader(csvfile2)
    for i in pricelist_reader:
        pricelist.append(i)

with open('ServiceDatesList.csv', 'r') as csvfile3:
    servlist_reader = csv.reader(csvfile3)
    for i in servlist_reader:
        servlist.append(i)

# 1.A) Full Inventory CSV
# Combining CSVs
full_list = manlist
for i in full_list:
    for y in pricelist:
        if i[0] == y[0]:
            i.insert(3, y[1])
    for z in servlist:
        if i[0] == z[0]:
            i.insert(4, z[1])

#print(full_list)

# Sorting by Brand
manlist.sort(key=lambda x: x[1])
#print(manlist)

with open('FullInventory.csv', 'w') as f:
    for row in manlist:
        manlist = csv.writer(f)
        manlist.writerow(row)

# 1.B)Item Type List CSVs
partlist = full_list
laptoplist = []
phonelist = []
towerlist = []

for i in partlist:
    if i[2] == 'laptop':
        laptoplist.append(i)
laptoplist.sort(key=lambda x: x[0])
with open('LaptopInventory.csv', "w") as f:
    for row in laptoplist:
        laptoplist = csv.writer(f)
        laptoplist.writerow(row)

for i in partlist:
    if i[2] == 'phone':
        phonelist.append(i)
phonelist.sort(key=lambda x: x[0])
with open('PhoneInventory.csv', "w") as f:
    for row in phonelist:
        phonelist = csv.writer(f)
        phonelist.writerow(row)

for i in partlist:
    if i[2] == 'tower':
        towerlist.append(i)
towerlist.sort(key=lambda x: x[0])
with open('TowerInventory.csv', "w") as f:
    for row in towerlist:
        towerlist = csv.writer(f)
        towerlist.writerow(row)

# 1.C) Past Service Date CSV

today = datetime.datetime.now()

# print(now)


date_list=[]

date_list = datetime.datetime.strptime(full_list[4], "%m/%d/%y").date_list()


# print(date_list)
# print(type(date_list[0][4]))


# 1.D) Damaged Inventory CSV
# dmglist = []
#
# for i in full_list:
#     if i[5] == 'damaged':
#         dmglist.append(i)
# dmglist.sort(key=lambda x: x[3])
# with open('DamagedInventory.csv', "w") as f:
#     for row in dmglist:
#         dmglist = csv.writer(f)
#         dmglist.writerow(row)