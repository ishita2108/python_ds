list = [85,45,96,75,23,1,20,23,656,91]

def selection_sort(list):
    for i in range(len(list)):
        min = i
        for j in range(i+1,len(list)):
            if list[j] < list[min]:
                min = j
        temp = list[i]
        list[i] = list[min]
        list[min]= temp
    return list
val = selection_sort(list)
print(val)