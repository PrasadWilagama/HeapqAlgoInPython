import  heapq

grades = [110,25,37,48,19,96,34,87,92]

print(min(grades),max(grades))

print(heapq.nlargest(2,grades))
print(heapq.nsmallest(3,grades))