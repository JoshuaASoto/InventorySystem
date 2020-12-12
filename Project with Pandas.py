import os
import csv
from datetime import datetime
import pandas as pd
from pandas import DataFrame

MainList = []
PriceList = []
ServList = []
with open('ManufacturerList.csv','r') as csvfile1:
    MainList_reader = csv.reader(csvfile1)
    for i in MainList_reader:
        MainList.append(i)
with open('PriceList.csv','r') as csvfile2:
    PriceList_reader = csv.reader(csvfile2)
    for i in PriceList_reader:
        PriceList.append(i)
with open('ServiceDatesList.csv','r') as csvfile3:
    ServList_reader = csv.reader(csvfile3)
    for i in ServList_reader:
        ServList.append(i)

# 1.A) Full Inventory CSV
# Combining CSVs
Full_List = MainList
for i in Full_List:
    for y in PriceList:
        if i[0] == y[0]:
            i.insert(3, y[1])
    for z in ServList:
        if i[0] == z[0]:
            i.insert(4, z[1])

# Converts full_list to dataframe
FullFrame = DataFrame(Full_List,columns=['ID','Brand','Type','Price','Service Date','Status'])



InventoryList = []

InventoryFrame = FullFrame.sort_values(by=['Brand'])
InventoryList = InventoryFrame.values.tolist()
with open('FullInventory.csv', 'w') as f:
    for row in InventoryList:
        InventoryList = csv.writer(f)
        InventoryList.writerow(row)



TypeFrame = FullFrame.sort_values(by=['ID'])

LaptopList = []
PhoneList = []
TowerList = []

LaptopFrame = TypeFrame.loc[TypeFrame['Type'] == 'laptop']
LaptopList = LaptopFrame.values.tolist()
with open('LaptopInventory.csv', "w") as f:
    for row in LaptopList:
        LaptopList = csv.writer(f)
        LaptopList.writerow(row)

PhoneFrame = TypeFrame.loc[TypeFrame['Type'] == 'phone']
PhoneList = PhoneFrame.values.tolist()
with open('PhoneInventory.csv', "w") as f:
    for row in PhoneList:
        PhoneList = csv.writer(f)
        PhoneList.writerow(row)

TowerFrame = TypeFrame.loc[TypeFrame['Type'] == 'tower']
TowerList = TowerFrame.values.tolist()
with open('TowerInventory.csv', "w") as f:
    for row in TowerList:
        TowerList = csv.writer(f)
        TowerList.writerow(row)


today = datetime.today()
date_time = today.strftime("%m/%d/%Y")

PastServiceDateList = []


PastServiceFrame = FullFrame
PastServiceFrame['Service Date'] = pd.to_datetime(PastServiceFrame['Service Date'])
PastServiceFrame = PastServiceFrame.loc[PastServiceFrame['Service Date'] < today]
PastServiceFrame = PastServiceFrame.sort_values(by=['Service Date'], ascending=False)
PastServiceFrame['Service Date'] = PastServiceFrame['Service Date'].dt.strftime("%m/%d/%Y")

PastServiceDateList = PastServiceFrame.values.tolist()

with open('PastServiceDateInventory.csv', "w") as f:
    for row in PastServiceDateList:
        PastServiceDateList = csv.writer(f)
        PastServiceDateList.writerow(row)


DamagedFrame = FullFrame.sort_values(by=['Price'])

DamagedList = []

DamagedFrame = DamagedFrame.loc[DamagedFrame['Status']=='damaged']
DamagedList = DamagedFrame.values.tolist()
with open('DamagedInventory.csv', "w") as f:
    for row in DamagedList:
        DamagedList = csv.writer(f)
        DamagedList.writerow(row)





