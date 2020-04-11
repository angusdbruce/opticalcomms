import numpy as np

with open("./angus_bruce/processed/CTLM_res_corr_output.txt") as file:
    data = np.asarray(file.readlines())

a, b = np.zeros(len(data)), np.zeros(len(data))

print(data[0])

for i in range(len(data)):
    data[i] = data[i][1:-2]
    a[i], b[i] = data[i].split(",")

print(a, b)

y = np.polyfit(a, b, 1)
print(y)