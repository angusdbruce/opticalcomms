import csv

temp = 200
gap = 6
number = 2

with open('./angus_bruce/LIV_excel.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))



#print(data)


a = "hello"
b = ""



for i in range(len(data)):
    #print(data[i][0], data[i][1])
    #a = "(",data[i][0],",", data[i][1]")\n"
    a = "({},{})\n".format(data[i][0], 1000.0*float(data[i][2]))
    #print(a)
    b += a

# file1 = open("./{}C_output/{}um_{}C.txt".format(temp, gap, temp, number),"w")#write mode 
# file1 = open("./diamond_b/diamond_b_afm_metal_depth_output.txt".format(temp, gap, temp),"w")#write mode 
file1 = open("./angus_bruce/processed/LIV_excel_output_current_o_power.txt","w")#write mode 

# file1 = open("./{}C_output/{}um_low_{}C({}).txt".format(temp, gap, temp, number),"w")#write mode 

file1.write(b) 
file1.close()
