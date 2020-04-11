import csv
import numpy as np

amps = 300
normalise = 1

with open('./angus_bruce/spectrum_{}mA.csv'.format(amps), newline='') as csvfile:
    data = list(csv.reader(csvfile))

if data:
    numberRows = len(data)

semiFinder = [-1] * numberRows
counter = 0

for i in range(numberRows):
   semiFinder[i] = data[i][0].find(';')
   if semiFinder[i] == 16:
       counter += 1

a = []
b = []

for i in range(numberRows):
    if semiFinder[i] == 16:
        try:
            # a = "({},{})\n".format(float(data[i][0].split(";")[0]), float(data[i][0].split(";")[1]))
            a = [float(data[i][0].split(";")[0]), float(data[i][0].split(";")[1])]
            b.append(a)
        except ValueError:
            print("On line {}, not a number, skipping...".format(i))

b = np.asarray(b)

if normalise == 1:
    print("Normailising")
    b0, b1 = np.hsplit(b, 2)
    print(b0)
    print(b1)
    b1 /= np.max(b1)
    b = np.column_stack((b0, b1))
    print("Normailised")
    print(b)

output = ""

print(np.shape(b))
print(len(b))

for i in range(len(b)):
    a = "({},{})\n".format(b[i][0], b[i][1])
    output += a

file1 = open("./angus_bruce/processed/spectrum_{}mA_output.txt".format(amps),"w")#write mode 
file1.write(output) 
file1.close()