input_data = open('input.txt', 'r')
data = input_data.read()
data_split = data.split()

krs_5 = 0
krs_3 = 0
krs_1 = 0

for i in range(1, len(data_split)):
    krs_5 += int(data_split[i]) + krs_5
for i in range(len(data)-1, 1, -1):
    krs_3 += int(data[i]) + krs_3
    print(data[i])
for i in range(1, len(data)):
    data_for_1 = data.sort()
    print(data_for_1)
    print(data)
    krs_1 += int(data_for_1[i]) + krs_1
print(krs_1, krs_3, krs_5)
    
input_data.close()