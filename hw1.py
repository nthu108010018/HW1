import csv
import os

cwb_filename = '108010018.csv'

C0A880 = []
C0F9A0 = []
C0G640 = []
C0R190 = []
C0X260 = []

with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   for row in mycsv:
       if(row['station_id'] ==  'C0A880' and row['TEMP']!=-999.000 and row['TEMP']!=-99.000):
           C0A880.append(row['TEMP'])
       elif(row['station_id'] ==  'C0F9A0'and row['TEMP']!=-999.000 and row['TEMP']!=-99.000):
           C0F9A0.append(row['TEMP'])
       elif(row['station_id'] ==  'C0G640'and row['TEMP']!=-999.000 and row['TEMP']!=-99.000):
           C0G640.append(row['TEMP'])
       elif(row['station_id'] ==  'C0R190'and row['TEMP']!=-999.000 and row['TEMP']!=-99.000):
           C0R190.append(row['TEMP'])
       elif(row['station_id'] ==  'C0X260'and row['TEMP']!=-999.000 and row['TEMP']!=-99.000):
           C0X260.append(row['TEMP'])

print("C0A880", max(C0A880))
print("C0F9A0", max(C0F9A0))
print("C0G640", max(C0G640))
print("C0R190", max(C0R190))
print("C0X260", max(C0X260))

os.system('pause')