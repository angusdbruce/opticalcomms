import csv
import numpy as np

amps = 300
normalise = 1

gap = 50
data = []
dataArray = []

a, b = "", ""


# print("gap = ", gap)
with open("./CTLM/{}.txt".format(gap)) as file:
    data = np.asarray(file.readlines())

data = np.asarray(data[1:])
# print(data)
# print('len= ', len(data))
resistance = np.zeros(0)
for j in range(len(data)):
    # print("j = ", j)
    dataArray.append(data[j].split('\t'))
    # print("here")
    # print(dataArray[j])
    if float(dataArray[j][0]) != 0:
        resistance = np.append(resistance, (float(dataArray[j][1])/(0.001*float(dataArray[j][0]))))
        # print(float(dataArray[j][1]), float(dataArray[j][0]), resistance)
    dataArray[j][1] = dataArray[j][1][:-1]
    a = "({},{})\n".format(dataArray[j][0], dataArray[j][1])
    b += a

print(resistance)
finalResistance = np.median(resistance)
print(finalResistance)

counter = 0
for i in range(len(resistance)):
    if resistance[i] > 1.1*finalResistance or resistance[i] < 0.9*finalResistance:
        resistance[i] = 0
        counter += 1
print("counter =", counter)
print(np.max(resistance))
finalResistance = np.average(resistance)
print(finalResistance)
finalResistance = np.average(resistance)*(len(resistance)/(len(resistance)-counter))
print((len(resistance)/(len(resistance)-counter)))
print(finalResistance)



# squaredError = np.square(finalResistance-resistance)
# # print(squaredError)
# meanSquared = 0
# for i in range(len(resistance)):
#     meanSquared += squaredError[i]

# # print(meanSquared, np.max(squaredError))
# meanSquared = (np.sum(squaredError))/len(squaredError)
# # print(meanSquared)

# counter = 0
# for i in range(len(squaredError)):
#     if squaredError[i] > 0.1*meanSquared:
#         squaredError[i] = 0
#         counter += 1
    
# # print("counter ={}".format(counter))
# meanSquared = (np.sum(squaredError))/(len(squaredError)-counter)

# print('here')
# print(len(squaredError))
# print(meanSquared)

b = "({},{})\n".format(gap, finalResistance)
file1 = open("./angus_bruce/processed/CTLM_res_output.txt".format(gap),mode="a")#append mode 
file1.write(b) 
file1.close()
        
        # data0, data1 = np.hsplit(data[i],)


# with open('./angus_bruce/spectrum_{}mA.csv'.format(amps), newline='') as csvfile:
#     data = list(csv.reader(csvfile))

# if data:
#     numberRows = len(data)

# semiFinder = [-1] * numberRows
# counter = 0

# for i in range(numberRows):
#    semiFinder[i] = data[i][0].find(';')
#    if semiFinder[i] == 16:
#        counter += 1

# a = []
# b = []

# for i in range(numberRows):
#     if semiFinder[i] == 16:
#         try:
#             # a = "({},{})\n".format(float(data[i][0].split(";")[0]), float(data[i][0].split(";")[1]))
#             a = [float(data[i][0].split(";")[0]), float(data[i][0].split(";")[1])]
#             b.append(a)
#         except ValueError:
#             print("On line {}, not a number, skipping...".format(i))

# b = np.asarray(b)

# if normalise == 1:
#     print("Normailising")
#     b0, b1 = np.hsplit(b, 2)
#     print(b0)
#     print(b1)
#     b1 /= np.max(b1)
#     b = np.column_stack((b0, b1))
#     print("Normailised")
#     print(b)

# output = ""

# print(np.shape(b))
# print(len(b))

# for i in range(len(b)):
#     a = "({},{})\n".format(b[i][0], b[i][1])
#     output += a

# file1 = open("./angus_bruce/processed/spectrum_{}mA_output.txt".format(amps),"w")#write mode 
# file1.write(output) 
# file1.close()