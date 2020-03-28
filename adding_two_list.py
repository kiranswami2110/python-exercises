NumList1 = [10, 20, 30]
NumList2 = [15, 25, 35]
total = []
 
for j in range(3):
    total.append( NumList1[j] + NumList2[j])
 
print("\nThe total Sum of Two Lists =  ", total)

# sub
NumList1 = [10, 20, 30,40]
NumList2 = [15, 25, 35]
total = []
 
for k in range(3):
    
    total.append( NumList1[k] - NumList2[k])
 
print("\nThe total Subtraction of Two Lists =  ", total)

# NumList2[1]=45 add new value
NumList1 = [10, 20, 30,40]
NumList2 = [15, 25, 35]
total = []
NumList2.insert(1,45)
for l in range(3):
    total.append( NumList1[l] + NumList2[l])
 
print("\nThe total Sum of Two Lists =  ", total)

#mul
NumList1 = [10, 20, 30,40]
NumList2 = [15, 25, 35]
total = []
 
for m in range(3):
    total.append( NumList1[m] * NumList2[m])
 
print("\nThe total Multiplication of Two Lists =  ", total)

# 6*(NumList1) + 7*(Numlist2)
NumList1 = [10, 20, 30,40]
NumList2 = [15, 25, 35]
total = []
 
for n in range(3):
    total.append([6* (NumList1[n])] + [7* NumList2[n]])
 
print("\nThe total Sum of Two Lists =  ", total)
